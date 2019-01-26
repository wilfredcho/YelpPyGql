import requests

from config import *
from itertools import product
from query import make_search
from util import to_csv


class Yelp(object):

    def __init__(self, api_key):
        self.headers = {
            "Authorization": 'Bearer ' + api_key,
            "Content-Type": "application/graphql"}
        self.url = "https://api.yelp.com/v3/graphql"

    def search(self, term, location, radius, price, category, limit=50):
        search_query = make_search(term, location, radius, price, category, limit=5)
        request = requests.post(
            self.url,
            headers=self.headers,
            data=search_query)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Request: " + str(request.status_code) + "\n"
                            + str(request.content))
    
    def run(self, term, category, city, radius, price, ratings):
        print("Total csv: " + str(len(list(product(term, city, radius, price, category, ratings)))))
        for combo in product(term, city, radius, price, category, ratings):
            result = yelp.search(combo[0], combo[1], combo[2], combo[3], combo[4], limit=50)
            business = result['data']['search']['business']
            short_list = yelp.key_filter(business, 'rating', combo[5][0], combo[5][1])
            name = combo[4] + '-' + combo[0] + '-' + combo[1] + '-' + str(combo[2]) + \
            '-' + str(combo[3]) + '-' + str(combo[5][0]) + '-' + str(combo[5][1])
            name = name.replace(' ', '_')
            to_csv(name + ".csv", short_list)

    @staticmethod
    def key_filter(result, key, lower, upper):
        return list(filter(lambda x: lower <= x[key] < upper, result))


if __name__ == "__main__":
    yelp = Yelp(KEY)
    yelp.run(term, category, city, radius, price, ratings)
