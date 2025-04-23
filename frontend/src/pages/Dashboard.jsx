import React from 'react';
import useSWR from 'swr';
import { useApi } from '../lib/api';

export default function Dashboard() {
  const api = useApi();
  const { data, error } = useSWR('/health', api, { refreshInterval: 5000 });

  return (
    <div className="p-6">
      <h2 className="text-xl font-bold mb-4">System Health</h2>
      {error && <p className="text-red-600">Error: {error.message}</p>}
      {!data && !error && <p>Loading...</p>}
      {data && (
        <div className="bg-green-100 text-green-800 p-4 rounded shadow">
          Backend status: {data.status}
        </div>
      )}
    </div>
  );
}
