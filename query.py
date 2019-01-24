def make_search(term, location, radius, price, limit=50):
    """
    radius: ' + str(radius) + ',\

    url\
    hours{\
                open{\
                    start\
                    end\
                    day\
                }\
            }\
    """
    return '\
    {\
        search(term: "' + str(term) + '",\
               location: "' + str(location) + '",\
               price: "' + str(price) + '",\
               limit: ' + str(limit) + ') {\
                    total\
                    business{\
                        name\
                        rating\
                        review_count\
                        display_phone\
                        location{\
                            address1\
                            city\
                            state\
                            postal_code\
                            country\
                        }\
                    }\
                }\
    }\
    '


def business_details(id):
    return '\
    {\
            business(id: "' + id + '"){\
                name\
                id\
                location {\
                    city\
                }\
            }\
        }\
    '
