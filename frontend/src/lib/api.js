import { useAuth } from '../context/AuthContext';
import { useMemo } from 'react';

export function useApi() {
  const { token } = useAuth();
  return useMemo(() => {
    return async (path, options = {}) => {
      const res = await fetch(`/api${path}`, {
        ...options,
        headers: {
          'Content-Type': 'application/json',
          ...(options.headers || {}),
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
        },
      });
      if (!res.ok) throw new Error(await res.text());
      return res.json();
    };
  }, [token]);
}
