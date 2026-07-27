import os
import re
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class RangeHTTPRequestHandler(SimpleHTTPRequestHandler):
    """
    Multi-threaded HTTP Server Handler with:
    1. HTTP 206 Partial Content Range Request support for HTML5 MP4 video streaming.
    2. HTTP POST handler for contact form testing.
    """
    protocol_version = 'HTTP/1.1'

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"\n[Contact Form Submission Received]: {post_data}\n")
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"OK - Form Submission Received")

    def send_head(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) or os.path.isdir(path):
            return super().send_head()

        ctype = self.guess_type(path)
        f = None
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        file_size = fs[6]
        
        range_header = self.headers.get('Range')
        if range_header:
            match = re.search(r'bytes=(\d+)-(\d*)', range_header)
            if match:
                first_byte = int(match.group(1))
                last_byte = int(match.group(2)) if match.group(2) else file_size - 1
                if last_byte >= file_size:
                    last_byte = file_size - 1
                length = last_byte - first_byte + 1
                
                self.send_response(206)
                self.send_header('Content-Type', ctype)
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Content-Range', f'bytes {first_byte}-{last_byte}/{file_size}')
                self.send_header('Content-Length', str(length))
                self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
                self.end_headers()
                
                f.seek(first_byte)
                return f

        self.send_response(200)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(file_size))
        self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

def run(port=8085):
    server_address = ('', port)
    httpd = ThreadingHTTPServer(server_address, RangeHTTPRequestHandler)
    print(f"Multi-Threaded Server running on http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
