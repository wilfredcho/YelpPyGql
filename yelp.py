import requests
from config import KEY
from query import make_search, business_details

class Yelp(object):

    def __init__(self, api_key):
        self.headers = {"Authorization": 'Bearer ' + api_key, "Content-Type": "application/graphql"}
        self.url = "https://api.yelp.com/v3/graphql"
    
    def search(self, term, location, radius, price, limit=50):
        """
        term: "indian food"
        price: "$" - "$$$$"
        radius: 1000 (meters)
        """
        search_query = make_search(term, location, radius, price, limit=5)
        #search_query = business_details('garaje-san-francisco')
        request = requests.post(self.url, headers=self.headers, data=search_query)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Request: " + str(request.status_code) + "\n"
                            + str(request.content))
    
    #def filter(self, result):

    #def csv(self, result):

if __name__ == "__main__":

    test = Yelp(KEY)
    print(test.search('fast food', 'San Francisco', 10000, '$', limit=2))
