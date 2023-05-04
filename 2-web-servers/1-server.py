import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1327))
s.listen(0)

while True:
  conn, addr = s.accept()
  response = "HTTP/1.1 200 OK\r\n"
  response += "Content-Type: text/html\r\n"
  response += "\r\n"
  response += "<h1>Hello, world!</h1>\r\n"
  conn.sendall(response.encode())
  conn.close()
