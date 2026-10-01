"""Local static server for the 1-10-2026 3D site scene. Requires Python 3; no third-party packages."""
import argparse
import functools
import http.server
import pathlib
import threading
import webbrowser

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=18792)
parser.add_argument('--no-browser', action='store_true')
args = parser.parse_args()
root = pathlib.Path(__file__).resolve().parent

http.server.SimpleHTTPRequestHandler.extensions_map.update({
    '.glb': 'model/gltf-binary', '.webp': 'image/webp', '.json': 'application/json',
})
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))

# If the requested port is busy, try the next ones.
server = None
for port in range(args.port, args.port + 10):
    try:
        server = http.server.ThreadingHTTPServer(('127.0.0.1', port), handler)
        break
    except OSError as error:
        print(f'Port {port} is busy ({error}); trying {port + 1}.', flush=True)
if server is None:
    raise SystemExit(f'No free port between {args.port} and {args.port + 9}.')
url = f'http://127.0.0.1:{port}/'
print(f'3D scene: {url}\nKeep this window open. Ctrl+C stops the server.', flush=True)
if not args.no_browser:
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
