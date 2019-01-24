def make_search(term, location, radius, price, limit=50):
    return '\
    {\
        search(term: "'+ str(term) + '",\
               location: "' + str(location) +'",\
               radius: ' + str(radius) + ',\
               price: "' + str(price) + '",\
               limit: ' + str(limit) + '){\
            total\
            business {\
            name\
            rating\
            review_count\
            url\
            display_phone\
            hours{\
                open{\
                    start\
                    end\
                }\
            }\
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
            business(id: "'+ id + '"){\
                name\
                id\
                location {\
                    city\
                }\
            }\
        }\
    '