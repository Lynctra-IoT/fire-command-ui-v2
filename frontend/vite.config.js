import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";

export default ({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");

  return defineConfig({
    plugins: [react()],
    server: {
      host: true,              // listen on 0.0.0.0
      port: 5173,
      proxy: {
        "/api": {
          target: env.VITE_API_BASE || "http://127.0.0.1:8000",
          changeOrigin: true,
        },
      },
    },
  });
};
