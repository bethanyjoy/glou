import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []

# Everson Royce
eversonroyce_urls = [

	"https://www.eversonroyce.com/collections/red-wines-from-the-usa",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=2",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=3",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=4",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=5",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=6",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=7",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=8",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=9",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=10",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=11",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=12",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=13",
	"https://www.eversonroyce.com/collections/red-wines-from-the-usa?page=14",

	"https://www.eversonroyce.com/collections/french-reds",
	"https://www.eversonroyce.com/collections/french-reds?page=2",
	"https://www.eversonroyce.com/collections/french-reds?page=3",
	"https://www.eversonroyce.com/collections/french-reds?page=4",
	"https://www.eversonroyce.com/collections/french-reds?page=5",
	"https://www.eversonroyce.com/collections/french-reds?page=6",
	"https://www.eversonroyce.com/collections/french-reds?page=7",
	"https://www.eversonroyce.com/collections/french-reds?page=8",
	"https://www.eversonroyce.com/collections/french-reds?page=9",
	"https://www.eversonroyce.com/collections/french-reds?page=10",
	"https://www.eversonroyce.com/collections/french-reds?page=11",
	"https://www.eversonroyce.com/collections/french-reds?page=12",

	"https://www.eversonroyce.com/collections/italian-reds",
	"https://www.eversonroyce.com/collections/italian-reds?page=2",
	"https://www.eversonroyce.com/collections/italian-reds?page=3",
	"https://www.eversonroyce.com/collections/italian-reds?page=4",
	"https://www.eversonroyce.com/collections/italian-reds?page=5",

	"https://www.eversonroyce.com/collections/spanish-portuguese-reds",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=2",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=3",
	"https://www.eversonroyce.com/collections/spanish-portuguese-reds?page=4",

	"https://www.eversonroyce.com/collections/eastern-european-reds",
	"https://www.eversonroyce.com/collections/eastern-european-reds?page=2",

	"https://www.eversonroyce.com/collections/reds-from-the-southern-hemisphere",
	"https://www.eversonroyce.com/collections/reds-from-the-southern-hemisphere?page=2",

	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=2",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=3",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=4",
	"https://www.eversonroyce.com/collections/whites-wines-from-the-usa?page=5",

	"https://www.eversonroyce.com/collections/french-white-wine",
	"https://www.eversonroyce.com/collections/french-white-wine?page=2",
	"https://www.eversonroyce.com/collections/french-white-wine?page=3",
	"https://www.eversonroyce.com/collections/french-white-wine?page=4",
	"https://www.eversonroyce.com/collections/french-white-wine?page=5",

	"https://www.eversonroyce.com/collections/italian-white-wine",
	"https://www.eversonroyce.com/collections/italian-white-wine?page=2",
	"https://www.eversonroyce.com/collections/italian-white-wine?page=3",

	"https://www.eversonroyce.com/collections/spanish-portuguese-whites"
	"https://www.eversonroyce.com/collections/spanish-portuguese-whites?page=2"

	"https://www.eversonroyce.com/collections/eastern-european-whites",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=2",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=3",
	"https://www.eversonroyce.com/collections/eastern-european-whites?page=4",

	"https://www.eversonroyce.com/collections/white-wines-from-the-southern-hemisphere",
	"https://www.eversonroyce.com/collections/white-wines-from-the-southern-hemisphere?page=2",

	"https://www.eversonroyce.com/collections/rose",
	"https://www.eversonroyce.com/collections/rose?page=2",
	"https://www.eversonroyce.com/collections/rose?page=3",
	"https://www.eversonroyce.com/collections/rose?page=4",

	"https://www.eversonroyce.com/collections/orange-wine",
	"https://www.eversonroyce.com/collections/orange-wine?page=2",
	"https://www.eversonroyce.com/collections/orange-wine?page=3",
	"https://www.eversonroyce.com/collections/orange-wine?page=4",
	"https://www.eversonroyce.com/collections/orange-wine?page=5",

	"https://www.eversonroyce.com/collections/sparklin-wine",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=2",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=3",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=4",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=5",
	"https://www.eversonroyce.com/collections/sparklin-wine?page=6",

]
for url in eversonroyce_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="prod-block")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'orange' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparklin' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# region
		if 'usa' in url:
			region = 'United States'
		elif 'french' in url:
			region = 'France'
		elif 'italian' in url:
			region = 'Italy'
		elif 'spanish' in url:
			region = 'Spain + Portugal'
		elif 'portuguese' in url:
			region = 'Spain + Portugal'
		elif 'eastern' in url:
			region = 'Eastern Europe'
		elif 'hemisphere' in url:
			region = 'Southern Hemisphere'
		else:
			region = 'undefined'

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://eversonroyce.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imageurl = imagesoup.find("img", class_="rimage__image")['src']
		if 'no-image' in imageurl:
			image_type = 'noimage'
		elif imageurl is not None:
			image = 'https:' + imageurl
			image_type = 'hasimage'
		else:
			image_type = 'noimage'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		# elif 'amevive' in title_string:
		# 	maker = 'Amevive'
		# elif 'amplify' in title_string:
		# 	maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		# elif 'cantinagiardino' in title_string:
		# 	maker = 'Cantina Giardino'
		# elif 'cirelli' in title_string:
		# 	maker = 'Cirelli'
		# elif 'dueterre' in title_string:
		# 	maker = 'Due Terre'
		# elif 'florez' in title_string:
		# 	maker = 'Florez'
		# elif 'folkmachine' in title_string:
		# 	maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		# elif 'gentle folk' in title_string:
		# 	maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
		elif 'jumbotime' in title_string:
			maker = 'Jumbo Time Wines'
		elif 'kopptisch' in title_string:
			maker = 'Kopptisch'
		elif 'koehnen' in title_string:
			maker = 'Koehnen'
		elif 'lasjaras' in title_string:
			maker = 'Las Jaras'
		elif 'marigny' in title_string:
			maker = 'Marigny'
		elif 'marthastoumen' in title_string:
			maker = 'Martha Stoumen'
		elif 'meinklang' in title_string:
			maker = 'Meinklang'
		elif 'nestarec' in title_string:
			maker = 'Nestarec'
		# elif 'oldwestminster' in title_string:
		# 	maker = 'Old Westminster'
		elif 'patricksullivan' in title_string:
			maker = 'Patrick Sullivan'
		elif 'purity' in title_string:
			maker = 'Purity'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		elif 'scottyboy' in title_string:
			maker = 'Scotty Boy'
		elif 'scotty-boy' in title_string:
			maker = 'Scotty Boy'
		elif 'stagiaire' in title_string:
			maker = 'Stagiaire'
		# elif 'subjecttochange' in title_string:
		# 	maker = 'Subject to Change'
		elif 'swick' in title_string:
			maker = 'Swick'
		elif 'wavywines' in title_string:
			maker = 'Wavy Wines'
		elif 'wildarcfarm' in title_string:
			maker = 'Wild Arc Farm'
		elif 'wonderwerk' in title_string:
			maker = 'Wonderwerk'
		else:
			maker ='undefined'

		maker_class = maker.strip().lower()

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Maker_class': maker_class,
			'Price': price,
			'Link': link,
			'Image': image,
			'Image_type': image_type,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Everson Royce',
			'Store_class': 'eversonroyce',
			'Region': region,
		})

# Print
print(wines)
