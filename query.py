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
                        categories{\
                            parent_categories{\
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
def make_gps_search(term, latitude, longitude, radius, price, category, limit=50):
    return '\
    {\
        search(term: "' + str(term) + '",\
               latitude: ' + str(latitude) + ',\
               longitude: ' + str(longitude) + ',\
               radius: ' + str(radius) + ',\
               price: "' + str(price) + '",\
               categories: "' + str(category) + '",\
               limit: ' + str(limit) + ') {\
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