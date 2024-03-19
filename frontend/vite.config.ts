import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
 base: "/",
 plugins: [react()],
 server: {
  port: 3000,
  strictPort: true,
  host: true,
  hmr: {
    port: 3010,
  },
  watch: {
    usePolling: true,
    // useFsEvents: true,
    // interval: 100,
  },
 },
});