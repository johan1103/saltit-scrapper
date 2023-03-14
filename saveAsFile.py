import pandas as pd


def save_as_csv(restaurants, duplicated_restaurants, city_name):
    dict_for_pd = []
    for restaurant_summary in restaurants.values():
        dict_for_pd.append({'address': restaurant_summary['address'], 'rid': restaurant_summary['rid'],
                            'name': restaurant_summary['name'], 'category': restaurant_summary['category'],
                            'score': restaurant_summary['score'], 'lat': restaurant_summary['latitude'],
                            'lng': restaurant_summary['longitude'], 'phone': restaurant_summary['phone'],
                            'img': restaurant_summary['imgSrc']})
    df = pd.DataFrame(data=dict_for_pd,
                      columns=['address', 'rid', 'name', 'category', 'score', 'lat', 'lng', 'phone', 'img'])
    df.to_csv(path_or_buf="static/restaurant-summary-" + city_name + ".csv")
    return


def save_as_text(restaurants, duplicated_restaurants):
    f = open("static/scrap.txt", 'w')
    for rid in restaurants:
        f.write('id : ')
        f.write(restaurants[rid]['rid'])
        f.write(', name : ')
        f.write(restaurants[rid]['name'])
        f.write(', location : {')
        f.write(str(restaurants[rid]['latitude']))
        f.write(', ')
        f.write(str(restaurants[rid]['longitude']))
        f.write('}')
        f.write('\n')
    f.close()
    f = open("static/duplicated.txt", 'w')
    for rid in duplicated_restaurants:
        print(rid)
        f.write('id ')
        f.write(duplicated_restaurants[rid]['rid'])
        f.write(' name ')
        f.write(duplicated_restaurants[rid]['name'])
        f.write('\n')
    f.close()
    return
