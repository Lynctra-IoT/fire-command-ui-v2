import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const tokenInStorage = localStorage.getItem('fc_jwt');
  const [token, setToken] = useState(tokenInStorage);

  const login = (jwt) => {
    localStorage.setItem('fc_jwt', jwt);
    setToken(jwt);
  };

  const logout = () => {
    localStorage.removeItem('fc_jwt');
    setToken(null);
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
