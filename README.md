# YelpPyGql

Generates a csv file base on your yelp query

## Installation
Clone this repository, install the packages in the requirement.txt

## How to use?
- git clone and cd to repo.
- Obtain Yelp API Key and join Yelp GraphQL Beta
- create your config.py with the following format
example
KEY = 'YOUR API KEY' 
term = ['italian']
category = ['restaurants']
city = ['San Francisco']
radius = [5000]
price = [1, 2, 3, 4]
ratings = [(2,3), (3,4), (4,5)]
- run `python yelp.py`
- A csv file will be generated with the settings.

## Contribute
Feel free to add and improve

## Credits
Empty for now.

## License
See the license file.
