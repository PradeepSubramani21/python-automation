
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime


queries = ["apple","samsung","realme","mi","oppo","vivo","motorola"]
url = f"https://www.flipkart.com/search?q="
row_list=[["Product", "Price"]]

# outputs the  prduct name and price as a list
def populate_data_as_list(parsed_response):
    product_detail = []
    for child in parsed_response.findChildren("div", { "class": "_3pLy-c row"}):
        product_detail.append([child.find("div", {"class": "_4rR01T"}).text, child.find("div",{"class":"_30jeq3 _1_WHN1"}).text.replace("₹","")])
        
    return product_detail
    
# loops throught the available queries and outputs the data in csv file
def get_parsed_response(url,queries,row_list):

    for query in queries:
        response = urllib.request.urlopen(url+query).read()
        row_list.extend(populate_data_as_list(BeautifulSoup(response,"html.parser")))
    print(row_list)
    
    now = datetime.now()    

    #writing the name and price of the product  in csc file
    with open(f'product_report {now.strftime("%d.%m.%Y@%H %M")}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

get_parsed_response(url, queries, row_list)

# _3pLy-c row - for component div
# _4rR01T - for product name
# _30jeq3 _1_WHN1 - for product price



    






