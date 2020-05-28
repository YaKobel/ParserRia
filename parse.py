# # import requests
# # from bs4 import BeautifulSoup
# #
# # URL = 'https://auto.ria.com/newauto/marka-honda/'
# # HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0', 'accept': '*/*'}
# #
# # def get_html(url, params=None):
# #     r = requests.get(url, headers=HEADERS, params=params)
# #     return r
# #
# # def parse():
# #     html = get_html(URL)
# #     print(html)
# #
# # parse()
#
#
# def get_content (html) :
#
#     soup = BeautifulSoup(html, 'html.parser')
#
#     items = soup.find_all('div', class_='proposition')
#
#
#
#     cars = []
#
#     for item in items:
#
#         uah_price = item.find('span', class_='grey size13')
#
#         if uah_price:
#
#             uah_price = uah_price.get_text()
#
#         else:
#
#             uah_price = 'Цена в гривнах не указана'
#
#         cars.append({
#
#             'titel': item.find ('h3', class_='proposition_name').get_text(strip=True),
#
#             'link': HOST + item.find('a').get('href'),
#
#             'usd_price': item.find('span', class_='green').get_text(),
#
#             'uah_price': uah_price,
#
#             'citi': item.find('svg', class_='svg svg-i16_pin').find_next('strong').get('title'),
#
#         })
#
#         print (cars)
#
#
#
#
#
#
#
#
#
#
#
#
#
# import requests
# from bs4 import BeautifulSoup
#
# URL = 'https://auto.ria.com/newauto/marka-jeep'
# HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0', 'accept': '*/*'}
# HOST = 'https://auto.ria.com'
#
#
# def get_html(url, params=None):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# def get_pages_count(html):
#
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='proposition_photo')
#
#     cars = []
#     for item in items:
#         uah_price = item.find('span', class_="grey size13")
#         if uah_price:
#             uah_price = uah_price.get_text()
#             uah_price = uah_price.get_text().replace(' • ', '')
#         else:
#             uah_price = 'Уточняйте цену'
#
#         cars.append({
#             # 'title': item.find('div', class_='proposition_title').get_text(strip=True),
#             # 'title': item.find('h3', class_='proposition_name').find_next('a', 'strong').get_text(),
#             # 'title': item.find('h3', class_='proposition_name').find_next('h3', class_='proposition_name').find_next('strong').get_text(),
#             # 'link': HOST + item.find('div', class_="proposition_equip").get('href'), #mt-5
#             # 'usd_price': item.find('span', class_="green").get_text(), #tooltip-price
#             'uah_price': uah_price,
#             # 'city': item.find('svg', class_="svg svg-i16_pin").find_next('strong').get_text(),
#         })
#     return cars
#     # print(cars)
#
#
# def parse():
#     html = get_html(URL)
#     if html.status_code == 200:
#         cars = get_content(html.text)
#     else:
#         print('Error')
#
# parse()