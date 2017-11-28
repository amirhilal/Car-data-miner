from bs4 import BeautifulSoup
import requests
import re

# PART 1
url = requests.get("https://www.drivearabia.com/carprices/ksa/")
fullData = url.text

soup = BeautifulSoup(fullData, 'html.parser')

brands = []
names = []

print("-----Fetching Car brands available in KSA----")
for link in soup.find_all("span", class_= "brand-name"):
    brands.append(link.text.replace(" ", "-"))

print("----Finished----")
print("A total of "+str(len(brands))+" Brands fetched")

#End of Part 1

#Part 2

print("----Fetching Car names---")
i = 1
while (i < len(brands)):
    print("----"+brands[i-1]+"----")
    carUrl = requests.get("https://www.drivearabia.com/carprices/ksa/"+str(brands[i-1]))
    carData = carUrl.text
    carSoup = BeautifulSoup(carData, 'html.parser')
    for link in carSoup.select("h2.featured-title a"):
        print(str.lstrip(str.rstrip(re.sub(" +", ' ', link.text))))
        name = str.lstrip(str.rstrip(re.sub(" +", ' ', link.text)))
        names.append(name)
    i += 1
