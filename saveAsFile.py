import pandas as pd


def save_as_csv(restaurants, duplicated_restaurants, city_name):
    df = pd.DataFrame(columns=['address', 'rid', 'name', 'category', 'lat', 'lng', 'phone', 'img', 'score'])
    for restaurant_summary in restaurants.values():
        restaurant_df = pd.DataFrame(data=[restaurant_summary['address'], restaurant_summary['rid'],
                                           restaurant_summary['name'], restaurant_summary['category'],
                                           restaurant_summary['latitude'], restaurant_summary['longitude'],
                                           restaurant_summary['phone'], restaurant_summary['imgSrc'],
                                           restaurant_summary['score']], columns=['address', 'rid', 'name', 'category',
                                                                                  'lat', 'lng', 'phone', 'img', 'score'],
                                     )
        df.append(restaurant_df)
    df.to_csv(path_or_buf="static/restaurant-summary" + city_name)
    return

def save_as_text(restaurants, duplicated_restaurants):
    f = open("static/scrap.txt", 'w')
    for rid in restaurants:
        print(rid)
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
    print('-----------duplicated----------')
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
