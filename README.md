# YelpPyGql

Generates a csv file base on your yelp query

## Installation
Clone this repository, install the packages in the requirement.txt

## How to use?
- git clone and cd to repo.
- Obtain Yelp API Key and join Yelp GraphQL Beta
- create your config.py with the following format
- example: <br />
`KEY = 'YOUR API KEY' ` <br />
`term = ['italian']` <br />
`category = ['restaurants']` <br />
`city = ['San Francisco']` <br />
`radius = [5000]` <br />
`price = [1, 2, 3, 4]` <br />
`ratings = [(2,3), (3,4), (4,5)]` <br />
- modify query.py the way you want =) <br />
refer to [https://www.yelp.com/developers/graphql/query/search]
- run `python yelp.py`
- A csv file will be generated with the settings.

## Contribute
Feel free to add and improve

## Credits
Empty for now.

## License
See the license file.
