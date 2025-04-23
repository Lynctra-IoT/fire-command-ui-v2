from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped
from backend.db.base import Base

class DeviceStatus(Base):
    __tablename__ = "device_status"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"), unique=True)
    last_seen: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_msg: Mapped[str] = mapped_column(String, nullable=True)
