import re
import json
import requests
import random
from bs4 import BeautifulSoup

# sets up empty list to store wine data
wines = []


# list of vinovore eagle rock urls to parse
vinovoreeaglerock_urls = [
	"https://vinovoreeaglerock.com/collections/red",
	"https://vinovoreeaglerock.com/collections/red?page=2",
	"https://vinovoreeaglerock.com/collections/red?page=3",
	"https://vinovoreeaglerock.com/collections/red?page=4",
	"https://vinovoreeaglerock.com/collections/red?page=5",
	"https://vinovoreeaglerock.com/collections/red?page=6",
	"https://vinovoreeaglerock.com/collections/red?page=7",
	"https://vinovoreeaglerock.com/collections/red?page=8",
	"https://vinovoreeaglerock.com/collections/white",
	"https://vinovoreeaglerock.com/collections/white?page=2",
	"https://vinovoreeaglerock.com/collections/white?page=3",
	"https://vinovoreeaglerock.com/collections/white?page=4",
	"https://vinovoreeaglerock.com/collections/white?page=5",
	"https://vinovoreeaglerock.com/collections/white?page=6",
	"https://vinovoreeaglerock.com/collections/orange",
	"https://vinovoreeaglerock.com/collections/orange?page=2",
	"https://vinovoreeaglerock.com/collections/orange?page=3",
	"https://vinovoreeaglerock.com/collections/orange?page=4",
	"https://vinovoreeaglerock.com/collections/rose",
	"https://vinovoreeaglerock.com/collections/rose?page=2",
	"https://vinovoreeaglerock.com/collections/rose?page=3",
	"https://vinovoreeaglerock.com/collections/rose?page=4",
	"https://vinovoreeaglerock.com/collections/sparkling",
	"https://vinovoreeaglerock.com/collections/sparkling?page=2",
	"https://vinovoreeaglerock.com/collections/sparkling?page=3",
	"https://vinovoreeaglerock.com/collections/sparkling?page=4",
	"https://vinovoreeaglerock.com/collections/sparkling?page=5",
	"https://vinovoreeaglerock.com/collections/sparkling?page=6",
]

# code for parsing vinovore eagle rock urls
for url in vinovoreeaglerock_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="grid-product")

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
		if 'sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("div", class_="grid-product__title").text.replace(" ", "").lower()

		# ignore non-wine items
		if 'giftbox' in title_string:
			print()
		elif 'bouquet' in title_string:
			print()

		# parse wine items
		else:

			# title
			title = product.find("div", class_="grid-product__title").text.strip()

			# price
			pricesoup = product.find("div", class_="grid-product__price")
			if pricesoup.span:
				price = 'On Sale'
			else:
				price = pricesoup.text.strip()

			# link
			link = 'http://vinovoreeaglerock.com' + product.find("a")['href']

			# image
			imagesoup = product.find('noscript')
			imagecheck = imagesoup.find("img", class_="grid-product__image")
			if imagecheck is not None:
				imageurl = imagesoup.find("img", class_="grid-product__image")['src']
				image = 'https:' + imageurl
			else:
				image = 'assets/placeholder.png'

			# maker
			if 'lewandowski' in title_string:
				maker = 'Ruth Lewandowski'
			elif 'amevive' in title_string:
				maker = 'Amevive'
			elif 'amplify' in title_string:
				maker = 'Amplify'
			elif 'broc' in title_string:
				maker = 'Broc Cellars'
			elif 'cirelli' in title_string:
				maker = 'Cirelli'
			elif 'dueterre' in title_string:
				maker = 'Due Terre'
			elif 'folkmachine' in title_string:
				maker = 'Folk Machine'
			elif 'furlani' in title_string:
				maker = 'Furlani'
			elif 'gentle folk' in title_string:
				maker = 'Gentle Folk'
			elif 'goodboywine' in title_string:
				maker = 'Good Boy Wine'
			elif 'gutoggau' in title_string:
				maker = 'Gut Oggau'
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
			elif 'oldwestminster' in title_string:
				maker = 'Old Westminster'
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
			elif 'subjecttochange' in title_string:
				maker = 'Subject to Change'
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

			# add wine to list
			wines.append({
				'Title': title,
				'Maker': maker,
				'Price': price,
				'Link': link,
				'Image': image,
				'Type': type,
				'Type_class': type_class,
				'Store': 'Vinovore Eagle Rock',
				'Store_class': 'vinovoreeaglerock',
			})


# list of highland park wine urls to parse
highlandpark_urls = [
	"https://www.highlandparkwine.com/collections/usa-red-wines",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=2",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=3",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=4",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=5",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=6",
	"https://www.highlandparkwine.com/collections/usa-red-wines?page=7",
	"https://www.highlandparkwine.com/collections/french-reds",
	"https://www.highlandparkwine.com/collections/french-reds?page=2",
	"https://www.highlandparkwine.com/collections/french-reds?page=3",
	"https://www.highlandparkwine.com/collections/french-reds?page=4",
	"https://www.highlandparkwine.com/collections/french-reds?page=5",
	"https://www.highlandparkwine.com/collections/french-reds?page=6",
	"https://www.highlandparkwine.com/collections/french-reds?page=7",
	"https://www.highlandparkwine.com/collections/french-reds?page=8",
	"https://www.highlandparkwine.com/collections/italian-reds",
	"https://www.highlandparkwine.com/collections/italian-reds?page=2",
	"https://www.highlandparkwine.com/collections/italian-reds?page=3",
	"https://www.highlandparkwine.com/collections/italian-reds?page=4",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=2",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-reds?page=3",
	"https://www.highlandparkwine.com/collections/eastern-european-reds",
	"https://www.highlandparkwine.com/collections/eastern-european-reds?page=2",
	"https://www.highlandparkwine.com/collections/eastern-european-reds?page=3",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=2",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=3",
	"https://www.highlandparkwine.com/collections/reds-from-the-southern-hemisphere?page=4",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=2",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=3",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-usa?page=4",
	"https://www.highlandparkwine.com/collections/french-white-wine",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=3",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=4",
	"https://www.highlandparkwine.com/collections/french-white-wine?page=5",
	"https://www.highlandparkwine.com/collections/italian-white-wine",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=2",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=3",
	"https://www.highlandparkwine.com/collections/italian-white-wine?page=4",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites?page=2",
	"https://www.highlandparkwine.com/collections/spanish-portuguese-whites?page=3",
	"https://www.highlandparkwine.com/collections/eastern-european-whites",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=2",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=3",
	"https://www.highlandparkwine.com/collections/eastern-european-whites?page=4",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-southern-hemisphere",
	"https://www.highlandparkwine.com/collections/white-wines-from-the-southern-hemisphere?page=2",
	"https://www.highlandparkwine.com/collections/rose",
	"https://www.highlandparkwine.com/collections/rose?page=2",
	"https://www.highlandparkwine.com/collections/rose?page=3",
	"https://www.highlandparkwine.com/collections/rose?page=4",
	"https://www.highlandparkwine.com/collections/rose?page=5",
	"https://www.highlandparkwine.com/collections/orange-wine",
	"https://www.highlandparkwine.com/collections/orange-wine?page=2",
	"https://www.highlandparkwine.com/collections/orange-wine?page=3",
	"https://www.highlandparkwine.com/collections/orange-wine?page=4",
	"https://www.highlandparkwine.com/collections/sparkling-wine",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=2",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=3",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=4",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=5",
	"https://www.highlandparkwine.com/collections/sparkling-wine?page=6",
]

# code for parsing highland park wine urls
for url in highlandpark_urls:

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
		if 'sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://highlandparkwine.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Highland Park Wine',
			'Store_class': 'highlandpark',
		})


# list of heavens market wine urls to parse
heavensmarket_urls = [
	"https://www.heavensmarketla.com/collections/red",
	"https://www.heavensmarketla.com/collections/red?page=2",
	"https://www.heavensmarketla.com/collections/red?page=3",
	"https://www.heavensmarketla.com/collections/red?page=4",
	"https://www.heavensmarketla.com/collections/red?page=5",
	"https://www.heavensmarketla.com/collections/white",
	"https://www.heavensmarketla.com/collections/white?page=2",
	"https://www.heavensmarketla.com/collections/white?page=3",
	"https://www.heavensmarketla.com/collections/white?page=4",
	"https://www.heavensmarketla.com/collections/rose",
	"https://www.heavensmarketla.com/collections/rose?page=2",
	"https://www.heavensmarketla.com/collections/skin-contact",
	"https://www.heavensmarketla.com/collections/skin-contact?page=2",
	"https://www.heavensmarketla.com/collections/skin-contact?page=3",
	"https://www.heavensmarketla.com/collections/skin-contact?page=4",
	"https://www.heavensmarketla.com/collections/sparkling",
	"https://www.heavensmarketla.com/collections/sparkling?page=2",
	"https://www.heavensmarketla.com/collections/sparkling?page=3",
	"https://www.heavensmarketla.com/collections/sparkling?page=4",
]

# code for parsing heavens market urls
for url in heavensmarket_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'contact' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("span", class_="visually-hidden").text.replace(" ", "").lower()

		# title
		title = product.find("span", class_="visually-hidden").text.strip()

		# ignore non-wine items
		if 'wineclass' in title_string:
			print()

		# parse wine items
		else:

			#price
			price = product.find("span", class_="price-item").text.strip()

			#link
			link = 'http://heavensmarketla.com' + product.find("a", class_="grid-view-item__link")['href']

			# image
			imagesoup = product.find('noscript')
			imagecheck = imagesoup.find("img", class_="grid-view-item__image")
			if imagecheck is not None:
				imageurl = imagesoup.find("img", class_="grid-view-item__image")['src']
				image = 'https:' + imageurl
			else:
				image = 'assets/placeholder.png'

			# maker
			if 'lewandowski' in title_string:
				maker = 'Ruth Lewandowski'
			elif 'amevive' in title_string:
				maker = 'Amevive'
			elif 'amplify' in title_string:
				maker = 'Amplify'
			elif 'broc' in title_string:
				maker = 'Broc Cellars'
			elif 'cirelli' in title_string:
				maker = 'Cirelli'
			elif 'dueterre' in title_string:
				maker = 'Due Terre'
			elif 'folkmachine' in title_string:
				maker = 'Folk Machine'
			elif 'furlani' in title_string:
				maker = 'Furlani'
			elif 'gentle folk' in title_string:
				maker = 'Gentle Folk'
			elif 'goodboywine' in title_string:
				maker = 'Good Boy Wine'
			elif 'gutoggau' in title_string:
				maker = 'Gut Oggau'
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
			elif 'oldwestminster' in title_string:
				maker = 'Old Westminster'
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
			elif 'subjecttochange' in title_string:
				maker = 'Subject to Change'
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

			# add wine to list
			wines.append({
				'Title': title,
				'Maker': maker,
				'Price': price,
				'Link': link,
				'Image': image,
				'Type': type,
				'Type_class': type_class,
				'Store': 'Heaven&#39;s Market',
				'Store_class': 'heavensmarket',
			})


# list of wine + eggs wine urls to parse
wineandeggs_urls = [
	"https://wineandeggs.com/collections/red-wine",
	"https://wineandeggs.com/collections/white-wine",
	"https://wineandeggs.com/collections/wine-rose",
	"https://wineandeggs.com/collections/skin-contact-wine",
	"https://wineandeggs.com/collections/sparkling-wine",
	"https://wineandeggs.com/collections/co-fermented",
	"https://wineandeggs.com/collections/piquette-wine",
]

# code for parsing wine + eggs urls
for url in wineandeggs_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product-block")

	for product in products:

		# type
		if 'red' in url:
			type = 'Red'
		if 'white' in url:
			type = 'White'
		if 'contact' in url:
			type = 'Orange'
		if 'rose' in url:
			type = 'Ros&#233;'
		if 'sparkling' in url:
			type = 'Sparkling'
		if 'fermented' in url:
			type = 'Co-Fermented'
		if 'piquette' in url:
			type = 'Piquette'
		type_class = type.replace("&#233;", "e").lower()

		# title
		title_name = product.find("h3", class_="product-block__title").text.strip()
		title_maker = product.find("div", class_="italicized-text").text.strip()
		title = title_maker + " " + title_name

		# get title string (used for parsing)
		title_string = title.replace(" ", "")

		# price
		price = product.find("div", class_="product-block__price").text.strip()

		# link
		link = 'http://wineandeggs.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecode = imagesoup.find("div", class_="product-block__image")['style']
		if imagecode is not None:
			imageurl = imagecode.strip("background-image:url('").strip("');")
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Wine + Eggs',
			'Store_class': 'wineandeggs',
		})


# list of silverlake wine wine urls to parse
silverlake_urls = [
	"https://silverlakewine.com/collections/red",
	"https://silverlakewine.com/collections/red?page=2",
	"https://silverlakewine.com/collections/red?page=3",
	"https://silverlakewine.com/collections/red?page=4",
	"https://silverlakewine.com/collections/red?page=5",
	"https://silverlakewine.com/collections/red?page=6",
	"https://silverlakewine.com/collections/red?page=7",
	"https://silverlakewine.com/collections/red?page=8",
	"https://silverlakewine.com/collections/red?page=9",
	"https://silverlakewine.com/collections/red?page=10",
	"https://silverlakewine.com/collections/red?page=11",
	"https://silverlakewine.com/collections/red?page=12",
	"https://silverlakewine.com/collections/red?page=13",
	"https://silverlakewine.com/collections/red?page=14",
	"https://silverlakewine.com/collections/red?page=15",
	"https://silverlakewine.com/collections/red?page=16",
	"https://silverlakewine.com/collections/red?page=17",
	"https://silverlakewine.com/collections/red?page=18",
	"https://silverlakewine.com/collections/red?page=19",
	"https://silverlakewine.com/collections/red?page=20",
	"https://silverlakewine.com/collections/red?page=21",
	"https://silverlakewine.com/collections/red?page=22",
	"https://silverlakewine.com/collections/red?page=23",
	"https://silverlakewine.com/collections/red?page=24",
	"https://silverlakewine.com/collections/red?page=25",
	"https://silverlakewine.com/collections/red?page=26",
	"https://silverlakewine.com/collections/white",
	"https://silverlakewine.com/collections/white?page=2",
	"https://silverlakewine.com/collections/white?page=3",
	"https://silverlakewine.com/collections/white?page=4",
	"https://silverlakewine.com/collections/white?page=5",
	"https://silverlakewine.com/collections/white?page=6",
	"https://silverlakewine.com/collections/white?page=7",
	"https://silverlakewine.com/collections/white?page=8",
	"https://silverlakewine.com/collections/white?page=9",
	"https://silverlakewine.com/collections/white?page=10",
	"https://silverlakewine.com/collections/white?page=11",
	"https://silverlakewine.com/collections/white?page=12",
	"https://silverlakewine.com/collections/white?page=13",
	"https://silverlakewine.com/collections/white?page=14",
	"https://silverlakewine.com/collections/rose",
	"https://silverlakewine.com/collections/rose?page=2",
	"https://silverlakewine.com/collections/rose?page=3",
	"https://silverlakewine.com/collections/rose?page=4",
	"https://silverlakewine.com/collections/rose?page=5",
	"https://silverlakewine.com/collections/rose?page=6",
	"https://silverlakewine.com/collections/orange",
	"https://silverlakewine.com/collections/orange?page=2",
	"https://silverlakewine.com/collections/orange?page=3",
	"https://silverlakewine.com/collections/orange?page=4",
	"https://silverlakewine.com/collections/orange?page=5",
	"https://silverlakewine.com/collections/orange?page=6",
	"https://silverlakewine.com/collections/sparkling",
	"https://silverlakewine.com/collections/sparkling?page=2",
	"https://silverlakewine.com/collections/sparkling?page=3",
	"https://silverlakewine.com/collections/sparkling?page=4",
	"https://silverlakewine.com/collections/sparkling?page=5",
	"https://silverlakewine.com/collections/sparkling?page=6",
	"https://silverlakewine.com/collections/sparkling?page=7",
	"https://silverlakewine.com/collections/sparkling?page=8",
	"https://silverlakewine.com/collections/fruit-wine"
]

# code for parsing silverlake wine urls
for url in silverlake_urls:

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
		if 'sparkling' in url:
			type = 'Sparkling'
		if 'fruit' in url:
			type = 'Co-Fermented'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("div", class_="title").text.replace(" ", "").lower()

		# title
		title = product.find("div", class_="title").text.strip()

		# price
		price = product.find("div", class_="product-price").text.strip()

		# link
		link = 'http://silverlakewine.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Silverlake Wine',
			'Store_class': 'silverlake',
		})


# list of everson royce wine urls to parse
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

# code for parsing everson royce wine urls
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
		imagecheck = imagesoup.find("img", class_="rimage__image")
		if imagecheck is not None:
			imageurl = imagesoup.find("img", class_="rimage__image")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Everson Royce',
			'Store_class': 'eversonroyce',
		})


# list of kamp wine urls to parse
kamp_urls = [
	"https://shopkamp.com/collections/red",
	"https://shopkamp.com/collections/chillable-reds",
	"https://shopkamp.com/collections/white",
	"https://shopkamp.com/collections/rose",
	"https://shopkamp.com/collections/orange",
	"https://shopkamp.com/collections/sparkling",
]

# code for parsing kamp urls
for url in kamp_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("div", class_="product--root")

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
		if 'sparkling' in url:
			type = 'Sparkling'
		# if 'chillable' in url:
		# 	type = 'Chillable Red'
		type_class = type.replace("&#233;", "e").replace(" ", "").lower()

		# title
		title_name = product.find("p", class_="product--title").text.strip()
		title_maker = product.find("div", class_="product--vendor").text.strip()
		title = title_maker + " " + title_name

		# get title string (used for parsing)
		title_string = title.replace(" ", "")

		# price
		price = product.find("span", class_="product--price money").text.strip()

		# link
		link = 'http://shopkamp.com' + product.find("a")['href']

		# image
		imagesoup = product.find('noscript')
		imagecheck = imagesoup.find("img")
		if imagecheck is not None:
			imageurl = imagesoup.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'

		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Kamp',
			'Store_class': 'kamp',
		})


# list of flask + field wine urls to parse
flaskandfield_urls = [
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=2",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=3",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Red+Wine&page=4",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&page=2",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=White+Wine&page=3",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Ros%C3%A9+Wine",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Ros%C3%A9+Wine&page=2",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Skin+Contact+Wine&page=2",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine",
	"https://flaskandfield.com/collections/wine?filter.p.product_type=Sparkling+Wine&page=2",
]

# code for parsing field + flask urls
for url in flaskandfield_urls:

	# set up soup
	soup = BeautifulSoup(requests.get(url).content, 'html.parser')
	products = soup.find_all("li", class_="grid__item")

	for product in products:

		# type
		if 'Red' in url:
			type = 'Red'
		if 'White' in url:
			type = 'White'
		if 'Contact' in url:
			type = 'Orange'
		if 'Ros' in url:
			type = 'Ros&#233;'
		if 'Sparkling' in url:
			type = 'Sparkling'
		type_class = type.replace("&#233;", "e").lower()

		# get title string (used for parsing)
		title_string = product.find("h3", class_="card__heading").text.replace(" ", "").lower()

		# title
		title = product.find("h3", class_="card__heading").text.strip()

		# price
		price = product.find("span", class_="price-item").text.strip()

		# link
		link = 'http://flaskandfield.com' + product.find("a")['href']

		# image
		imagecheck = product.find("img")
		if imagecheck is not None:
			imageurl = product.find("img")['src']
			image = 'https:' + imageurl
		else:
			image = 'assets/placeholder.png'


		# maker
		if 'lewandowski' in title_string:
			maker = 'Ruth Lewandowski'
		elif 'amevive' in title_string:
			maker = 'Amevive'
		elif 'amplify' in title_string:
			maker = 'Amplify'
		elif 'broc' in title_string:
			maker = 'Broc Cellars'
		elif 'cirelli' in title_string:
			maker = 'Cirelli'
		elif 'dueterre' in title_string:
			maker = 'Due Terre'
		elif 'folkmachine' in title_string:
			maker = 'Folk Machine'
		elif 'furlani' in title_string:
			maker = 'Furlani'
		elif 'gentle folk' in title_string:
			maker = 'Gentle Folk'
		elif 'goodboywine' in title_string:
			maker = 'Good Boy Wine'
		elif 'gutoggau' in title_string:
			maker = 'Gut Oggau'
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
		elif 'oldwestminster' in title_string:
			maker = 'Old Westminster'
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
		elif 'subjecttochange' in title_string:
			maker = 'Subject to Change'
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

		# add wine to list
		wines.append({
			'Title': title,
			'Maker': maker,
			'Price': price,
			'Link': link,
			'Image': image,
			'Type': type,
			'Type_class': type_class,
			'Store': 'Flask + Field',
			'Store_class': 'flaskandfield',
		})




random.shuffle(wines)

# Write JSON file
with open("data.json", "w") as writeJSON:
	json.dump({'wine': wines}, writeJSON, ensure_ascii=False)

# prints data to terminal (only needed for troubleshooting)
# print(json.dumps(wines, indent=4))
print('success!')
