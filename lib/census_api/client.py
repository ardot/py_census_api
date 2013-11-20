from restkit import request

class client:
  api_key
  api_dataset

  def __init__(self, key, dataset):

      if (!key):
        raise ArgumentError("You must set an API key!")

      # Use RestClient directly to determine the validity of the API Key
      path = "http://api.census.gov/data/2010/sf1?key=" + api_key + "&get=P0010001&for=state:01"
      response = request(path)

      if (response.body.include? "Invalid Key"):
        raise ArgumentError("Not a valid API key!")

      self.api_key = key
      self.api_dataset = dataset
