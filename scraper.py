import requests
from bs4 import BeautifulSoup

def GetConsoles():
    cnt = 1
    page = 1 
    results = []

    while cnt > 0:
        response = requests.get("https://www.trademe.co.nz/gaming/playstation-4/consoles?buy=buynow&page=" + str(page))
        soup = BeautifulSoup(response.text,"html.parser")
        itemlist = soup.findAll("div", {"class":"supergrid-listing"})
        cnt = len(itemlist)

        for item in itemlist:
            try:
                item_title = item.find("div", {"class":"title"}).text.strip()
                item_price = item.find("div", {"class":"listingBuyNowPrice"}).text.strip()
                results.append({"title" : item_title, "price" : item_price})
            except:
                print("Fail")
    
        page += 1
    return results