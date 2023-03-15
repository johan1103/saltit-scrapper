

def save_as_text(menus, city_name):
    f = open("../static/menu/scrap-" + city_name + ".txt", 'w')
    for menu in menus:
        f.write('id : ')
        f.write(menu['rid'])
        f.write(', name : ')
        f.write(menu['name'])
        f.write(', price : ')
        f.write(menu['price'])
        f.write(', address : ')
        f.write(menu['address'])
        f.write('\n')
    f.close()
    return