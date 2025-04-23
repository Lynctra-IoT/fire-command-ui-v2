import { useEffect, useRef } from "react";
export default function useWs(token, onMsg) {
  const wsRef = useRef(null);

  useEffect(() => {
    if (!token) return;
    const ws = new WebSocket(`ws://${location.host.replace(/:5173$/,":8000")}/ws/updates`);
    wsRef.current = ws;
    ws.onmessage = (e) => onMsg(JSON.parse(e.data));
    const ping = setInterval(() => ws.readyState === 1 && ws.send("ping"), 10000);
    return () => {
      clearInterval(ping);
      ws.close();
    };
  }, [token, onMsg]);
}
