from restkit import request

CENSUS_URL = "http://api.census.gov/data"
SOURCE = "2012/acs3/profile"
# Sample request
# http://api.census.gov/data/2012/acs3/profile?get=DP02_0001PE&for=state:*&key=...

def initialize(url, source, options):
  path = url + "/" + source + "?" + toParams(options)
  return request(path)


# Returns the para
def toParams(options):
  counter = 0
  toRet = ""
  for opt_key, opt_val in options:
    counter = counter + 1
    toRet = toRet + str(opt_key) + "=" + str(opt_val)
    if (counter < len(options)):
      toRet = toRet + "&"
  return toRet

#if __name__ =='__main__':
#  params = [('get', 'DP02_0001PE'), ('for', 'state:*'), ('key', '3e111b82ed8486dd1077c9f40a376c996a4a4993')]
#  print initialize(CENSUS_URL, SOURCE, params)
