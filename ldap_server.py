import socketserver
import threading
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class LDAPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).decode('utf-8')
        logger.info(f"Received LDAP request: {data}")
        self.request.sendall(b"LDAP response")
        self.request.close()

def start_ldap_server():
    server = socketserver.TCPServer(('localhost', 1389), LDAPRequestHandler)
    logger.info("LDAP server started on localhost:1389")
    server.serve_forever()

if __name__ == "__main__":
    try:
        server_thread = threading.Thread(target=start_ldap_server)
        server_thread.daemon = True
        server_thread.start()
        server_thread.join()
    except KeyboardInterrupt:
        logger.info("Shutting down LDAP server")