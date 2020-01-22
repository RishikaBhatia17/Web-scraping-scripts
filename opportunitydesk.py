# need to create excel sheet
import csv

import requests
from bs4 import BeautifulSoup

csv_file = open('jobs.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'headline', 'Deadline', 'Para', 'readmore'])

for i in range(1, 50):
	res = requests.get('https://opportunitydesk.org/category/jobs-and-internships/page/' + str(i))
	soup = BeautifulSoup(res.text, 'html.parser')

	#image of the opportunity 
	try:
		article_image = soup.find('div', class_='blogposts-inner')
		image = article_image.a.get('href')
		print(image)

	except AttributeError as e:
		print("opportunity image")
		print(str(e))

	# headline of the opportunity
	try: 
		article_headline = soup.find('div', class_='blogposts-inner')
		headline = article_headline.h3('a')
		print(headline)

	# deadline of the opportunity
		deadline_date = soup.find('li', class_='full-left clearfix')
		date = deadline_date.p
		print(date)

	except AttributeError as e:
		print("opportunity deadline")
		print(str(e))

	# para of the opportnity
		article_para = soup.find('div', class_='list-block clearfix')
		para_a = article_para.a.get('href')
		res = requests.get(para_a)
		print(para_a)

	# read more option for opportunity
		article_readmore = soup.find('div', class_='list-block clearfix')
		readmore = article_readmore.a.get('href')
		print(readmore)

	csv_writer.writerow(['image', 'headline', 'date', 'para_a', 'readmore'])

csv_file.close()

