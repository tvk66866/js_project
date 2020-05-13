# import http.server
# import socketserver
#
# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

import requests

url = "https://my.api.mockaroo.com/patient_record_json.json?min_age=65&max_age=70&key=ce6f7640"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.get(url, headers=headers, data = payload)

print(response.text.encode('utf8'))