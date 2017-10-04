import urllib
import urllib2

values = {"userName":"15xhliu","pwd":"lXH971111"}
data = urllib.urlencode(values)
url = "http://1.1.1.2/ac_portal/20170602150308/pc.html?template=20170602150308&tabs=pwd&vlanid=0&url="

request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print(response.read())