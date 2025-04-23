# backend/api/v1/endpoints/events.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime

from backend.api.deps import get_db          # ← add get_current_user if you re-enable auth
from backend.models.device_status import DeviceStatus
from backend.models.alarm import Alarm
from backend.core.ws_manager import ws_manager

router = APIRouter(prefix="/events")


@router.post("/", summary="Ingest device telemetry & alarms")
async def ingest_event(
    payload: dict,
    db: AsyncSession = Depends(get_db),
    # _user = Depends(get_current_user),      # <-- re-add for JWT auth
):
    """
    Accepts JSON like:
    ```json
    {
      "device_id": 1,
      "level": "warning",        // "info" | "warning" | "critical"
      "message": "Smoke detected zone 3"
    }
    ```
    * Upserts `device_status` (last_seen, last_msg)
    * Inserts an `Alarm` row if level != "info"
    * Broadcasts the event to all WebSocket clients (`/ws/updates`)
    """
    dev_id = payload.get("device_id")
    if dev_id is None:
        return {"ok": False, "error": "device_id missing"}

    msg   = payload.get("message", "")
    level = payload.get("level", "info")

    # ── UPSERT device_status ────────────────────────────────────────
    res = await db.execute(
        select(DeviceStatus).where(DeviceStatus.device_id == dev_id)
    )
    status = res.scalar_one_or_none()

    if status:
        status.last_seen = datetime.utcnow()
        status.last_msg  = msg
    else:
        status = DeviceStatus(device_id=dev_id, last_msg=msg)
        db.add(status)

    # ── Create alarm for non-info levels ────────────────────────────
    if level != "info":
        db.add(Alarm(device_id=dev_id, level=level, message=msg))

    await db.commit()

    # ── Push to WebSocket clients ───────────────────────────────────
    await ws_manager.broadcast({"type": "event", "payload": payload})

    return {"ok": True}
