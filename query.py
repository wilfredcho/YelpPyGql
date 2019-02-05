def check_location(location):
    if isinstance(location, tuple):
        latitude = location[0]
        longitude = location[1]
        location = ""
    elif isinstance(location, str):
        latitude = ""
        longitude = ""
        location = location
    else:
        raise TypeError("Check config.py for location info")
    return latitude, longitude, location

def make_search(term, location, radius, price, category, attribute, limit=50):
    latitude, longitude, location = check_location(location)
    return '\
    {\
        search(term: "' + str(term) + '",\
            location: "' + str(location) + '",\
            latitude: ' + str(latitude) + ',\
            longitude: ' + str(longitude) + ',\
            radius: ' + str(radius) + ',\
            price: "' + str(price) + '",\
            categories: "' + str(category) + '",\
            attributes: "' + str(attribute) + '",\
            limit: ' + str(limit) + ')\
            {\
            total\
            business{\
                name\
                rating\
                price\
                review_count\
                display_phone\
                url\
                location{\
                    address1\
                    city\
                    state\
                    postal_code\
                }\
                categories {\
                    parent_categories {\
                        title\
                    }\
                }\
                hours{\
                    open{\
                            start\
                            end\
                        }\
                }\
            }\
        }\
    }\
    '