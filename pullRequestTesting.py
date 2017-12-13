from urllib2 import Request, urlopen, URLError

request = Request('http://api.guildwars2.com/v2/commerce/listings/19684')

try:
	response = urlopen(request)
	pull1 = response.read()
	write(pull1)
except URLError, e:
    print 'No kittez. Got an error code:', e
