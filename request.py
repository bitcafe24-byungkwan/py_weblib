from urllib.parse import urlencode
from urllib.request import urlopen, Request

http_response = urlopen('http://www.example.com')

body = http_response.read()
print(body)


# post
data = {
    'email': '123@4.5',
    'password': '1234',
    'name': 'dh ahn'
}
data = urlencode(data).encode('utf-8')

request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')
request.add_header('cookies:jsessionid=asdfnsdifno')
http_response = urlopen(request)
print(http_response.read())