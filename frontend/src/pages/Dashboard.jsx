import React, { useState, useCallback } from "react";
import useSWR from "swr";
import { useApi } from "../lib/api";
import { useAuth } from "../context/AuthContext";
import useWs from "../lib/useWs";
import AlarmList from "../components/AlarmList";

export default function Dashboard() {
  const api = useApi();
  const { token } = useAuth();
  const { data } = useSWR("/health", api, { refreshInterval: 5000 });

  const [lastMsg, setLastMsg] = useState(null);
  const [alarms, setAlarms] = useState([]);

  const onWs = useCallback((event) => {
    if (event.type === "event") {
      setLastMsg(event.payload.message);
      if (event.payload.level !== "info")
        setAlarms((prev) => [event.payload, ...prev].slice(0, 20));
    }
  }, []);

  useWs(token, onWs);

  return (
    <div className="p-6 space-y-6">
      <div className="p-4 rounded shadow bg-green-100 text-green-800">
        Backend: {data ? "ok" : "loading..."}
      </div>

      <div className="p-4 rounded shadow bg-gray-100">
        <h3 className="font-bold">Last Panel Message</h3>
        <p>{lastMsg || "—"}</p>
      </div>

      <div className="p-4 rounded shadow bg-gray-100">
        <h3 className="font-bold mb-2">Active Alarms</h3>
        <AlarmList alarms={alarms} />
      </div>
    </div>
  );
}
