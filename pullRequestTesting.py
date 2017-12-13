from urllib2 import Request, urlopen, URLError

request = Request('http://api.guildwars2.com/v2/commerce/listings/19684')

testfile <- open("testfile.txt", "w")

try:
	response = urlopen(request)
	pull1 = response.read()
	testfile.write(pull1)
except URLError, e:
    testfile.write("Error")
