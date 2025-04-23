import React from "react";

export default function AlarmList({ alarms }) {
  if (!alarms.length) return <p>No active alarms 🚀</p>;
  return (
    <ul className="space-y-2">
      {alarms.map((a) => (
        <li key={a.id} className="p-2 rounded bg-red-100 text-red-800">
          [{a.level}] {a.message}
        </li>
      ))}
    </ul>
  );
}
