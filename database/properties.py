import pymysql.cursors
import configparser as parser


def get_db_properties():
    properties = parser.ConfigParser()
    properties.read('../config.ini')
    cursor = pymysql.connect(
        host=properties['DB']['host'],  # host name
        user=properties['DB']['user'],  # user name
        password=properties['DB']['password'],  # password
        db=properties['DB']['db_name'],  # db name
    )
    return cursor
