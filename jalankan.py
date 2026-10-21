"""Peluncur lokal: melayani index.html di http://localhost agar kamera bisa dipakai."""
import http.server, os, socketserver, sys, threading, webbrowser

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Permissions-Policy", "camera=(self)")
        super().end_headers()
    def log_message(self, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
server = None
for port in range(8080, 8100):
    try:
        server = socketserver.TCPServer(("127.0.0.1", port), Handler)
        break
    except OSError:
        continue
if server is None:
    sys.exit("Port 8080-8099 sedang dipakai. Tutup aplikasi lain lalu coba lagi.")

url = f"http://localhost:{port}/index.html"
print(f"Penghitung jari berjalan di {url}")
print("Izinkan akses kamera saat browser bertanya. Tekan Ctrl+C untuk berhenti.")
if "--no-browser" not in sys.argv:
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nDihentikan.")
