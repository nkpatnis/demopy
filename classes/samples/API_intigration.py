__author__ = 'nikhil'

import http.client


# non working code
conn = http.client.HTTPSConnection("openweathermap.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.value)
# 200 OK
# data1 = r1.read()
# conn.request("GET", "/data/2.5/weather?q=London&appid=44db6a862fba0b067b1930da0d769e98")
# r2 = conn.getresponse()
# print(r2.status, r2.reason)
# 404 Not Found
# data2 = r2.read()
conn.close()
