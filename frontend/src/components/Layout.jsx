import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Layout() {
  const { logout } = useAuth();
  return (
    <div className="flex min-h-screen">
      <aside className="w-60 bg-gray-800 text-white p-4">
        <h1 className="text-2xl font-bold mb-6">Fire Command</h1>
        <nav className="space-y-2">
          <Link to="/" className="block hover:text-gray-300">Dashboard</Link>
        </nav>
        <button
          onClick={logout}
          className="mt-10 text-sm text-red-400 hover:text-red-300"
        >
          Logout
        </button>
      </aside>
      <main className="flex-1 bg-gray-50">
        <Outlet />
      </main>
    </div>
  );
}
