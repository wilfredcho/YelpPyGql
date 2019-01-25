def make_search(term, location, radius, price, category, limit=50):
    return '\
    {\
        search(term: "' + str(term) + '",\
               location: "' + str(location) + '",\
               radius: ' + str(radius) + ',\
               price: "' + str(price) + '",\
               categories: "' + str(category) + '",\
               limit: ' + str(limit) + ') {\
                    total\
                    business{\
                        name\
                        rating\
                        review_count\
                        display_phone\
                        url\
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
