import requests

from config import KEY
from query import business_details, make_search
from util import to_csv


class Yelp(object):

    def __init__(self, api_key):
        self.headers = {
            "Authorization": 'Bearer ' + api_key,
            "Content-Type": "application/graphql"}
        self.url = "https://api.yelp.com/v3/graphql"

    def search(self, term, location, radius, price, limit=50):
        """
        term: "indian food"
        price: "1" - "4"
        radius: 1000 (meters)
        """
        search_query = make_search(term, location, radius, price, limit=5)
        #search_query = business_details('garaje-san-francisco')
        request = requests.post(
            self.url,
            headers=self.headers,
            data=search_query)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Request: " + str(request.status_code) + "\n"
                            + str(request.content))

    @staticmethod
    def key_filter(result, key, lower, upper):
        return list(filter(lambda x: lower < x[key] <= upper, result))

    @staticmethod
    def get_info(result, key):
        return list(map(lambda x: x[key], result))


if __name__ == "__main__":

    yelp = Yelp(KEY)
    result = yelp.search('chinese food', 'San Francisco', 5000, 1, limit=50)
    business = result['data']['search']['business']
    short_list = yelp.key_filter(business, 'rating', 2, 4)
    #short_list = yelp.get_info(short_list, 'display_phone')
    #print(short_list)
    to_csv("result.csv", short_list)
