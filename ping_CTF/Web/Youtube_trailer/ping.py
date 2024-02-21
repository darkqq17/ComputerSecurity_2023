import socket

# URL from the user
url = "www.youtube.com"

# Getting the IP address
ip_address = socket.gethostbyname(url)
print(ip_address)
