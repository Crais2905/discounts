import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/static': {
        target: 'http://localhost:8000', // твій бекенд FastAPI
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
