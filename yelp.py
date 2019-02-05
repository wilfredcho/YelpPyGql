import requests

from config import *
from itertools import product
from query import make_search, check_location
from util import to_csv


class Yelp(object):

    def __init__(self, api_key):
        self.headers = {
            "Authorization": 'Bearer ' + api_key,
            "Content-Type": "application/graphql"}
        self.url = "https://api.yelp.com/v3/graphql"

    def _file_namer(self, rating, term, location, radius, price, category, attribute):
        latitude, longitude, location = check_location(location)
        if location:
            name = str(category) + '-' + str(term) + '-' + str(location) + '-' + str(radius)+ 'm' + \
                    '-' + str(price * '$') + '-' + str(attribute) + '-' + str(rating[0]) + '-' + str(rating[1])
        else:
            name = str(category) + '-' + str(term) + '-' + str(latitude) + '-' + str(longitude) + '-' + str(radius) + 'm' + \
                    '-' + str(price * '$') + '-' + str(attribute) + '-' + str(rating[0]) + '-' + str(rating[1])

        name = name.replace(' ', '_')
        name = name.replace(',', '_')
        name = name.replace('.', '#')
        return name

    def search(self, term, location, radius, price, category, attribute, limit):
        search_query = make_search(term, location, radius, price, category, attribute, limit)
        request = requests.post(
            self.url,
            headers=self.headers,
            data=search_query)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Request: " + str(request.status_code) + "\n"
                            + str(request.content))
    
    def run(self, ratings, term, location, radius, price, category, attribute, limit=50):
        print("Total csv: " + str(len(list(product(ratings, term, location, radius, price, category, attribute)))))
        for combo in product(term, location, radius, price, category, attribute):
            result = yelp.search(combo[0], combo[1], combo[2], combo[3], combo[4], combo[5], limit)
            business = result['data']['search']['business']
            for rating in ratings:
                short_list = yelp.key_filter(business, 'rating', rating[0], rating[1])
                name = self._file_namer(rating, combo[0], combo[1], combo[2], combo[3], combo[4], combo[5])
                if short_list:
                    import pdb; pdb.set_trace()
                    to_csv(name + ".csv", short_list)
                else:
                    print('No match for ' + name)

    @staticmethod
    def key_filter(result, key, lower, upper):
        return list(filter(lambda x: lower <= x[key] < upper, result))


if __name__ == "__main__":
    yelp = Yelp(KEY)
    yelp.run(ratings, term, location, radius, price, category, attribute)
