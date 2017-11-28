from bs4 import BeautifulSoup
import requests
import re

#Brand/Name
imageUrl = requests.get("http://www.cars-data.com/en/bmw/x4")
imageData = imageUrl.text
imageSoup = BeautifulSoup(imageData, 'html.parser')

for link in imageSoup.find_all("a", attrs= {'title': 'BMW X4'}, limit=1):
    print(link['href'].split("/")[5])
    print("pic link : http://www.cars-data.com/pictures/bmw/bmw-x4_"+link['href'].split("/")[5]+"_1.jpg")
    print("pic link : http://www.cars-data.com/pictures/bmw/bmw-x4_" + link['href'].split("/")[5] + "_2.jpg")
    print("pic link : http://www.cars-data.com/pictures/bmw/bmw-x4_" + link['href'].split("/")[5] + "_3.jpg")
