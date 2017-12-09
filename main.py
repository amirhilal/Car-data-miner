import os

from bs4 import BeautifulSoup
import requests
import re
import urllib.request

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
        name = str.lstrip(str.rstrip(re.sub(" +", ' ', link.text)))
        nameUrl = name.replace(' ', '-')
        print(name)
        imageUrl = requests.get("http://www.cars-data.com/en/"+str(brands[i-1].lower())+"/"+nameUrl.replace(str(brands[i-1]+"-"), "").lower())
        imageData = imageUrl.text
        imageSoup = BeautifulSoup(imageData, 'html.parser')

        for images in imageSoup.find_all("a", attrs={'title': name}, limit=1):
            id = images['href'].split('/')[5]
            folderName = nameUrl.lower()
            try:
                os.makedirs(folderName)
            except FileExistsError:
                print("Not created, already exists")

            for g in range (1, 5):
                fileName = str(nameUrl.lower())
                imageFileName = "http://www.cars-data.com/pictures/"+ str(brands[i-1].lower()) + "/"+nameUrl.lower()+"_"+id+"_"+str(g)+".jpg"
                imageFile = open(folderName+"/" + fileName+"_"+str(g)+".jpg", "wb")
                print(imageFileName)
                try:
                    imageFile.write(urllib.request.urlopen(imageFileName).read())
                    imageFile.close()
                    print(str(fileName)+ " Saved")
                except urllib.request.HTTPError:
                    print ('Image not found')

    i += 1
