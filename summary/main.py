from city_scrapping import scrapping_city
from restaurant_scrapping import scrapping_restaurants
from save_file import save_as_text
from save_file import save_as_csv

if __name__ == '__main__':
    result_cities = scrapping_city()
    food_types = ['한식', '중식', '양식', '일식']
    for city_name, city_detail in result_cities.items():
        restaurants = {}
        duplicated_restaurants = {}
        for detail_name in city_detail:
            for food_type in food_types:
                scrapping_restaurants(restaurants, duplicated_restaurants, detail_name, food_type)
        save_as_text(restaurants, duplicated_restaurants, city_name)
        save_as_csv(restaurants, duplicated_restaurants, city_name)
