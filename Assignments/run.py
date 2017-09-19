# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import json
company_details=[]
url=requests.get("https://www.yellowpages.com/search?search_terms=computer&geo_location_terms=Los+Angeles%2C+CA")
#To get the data from web page  
#print(r.content)//to print the content
soup=BeautifulSoup(url.content,"lxml")
#To convert the content in some readable form
#print (soup.prettify())
#To cleanup code and make easier to read

data= soup.find_all("div",{"class":"info"})
#To find the content from class info
#print(data)

for item in data:
         name=(item.contents[0].find_all("a",{"class":"business-name"})[0].text)
        #To print the content from class business name
         
         try:
          postal=(item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text)
         except:
            pass
         try:
          phone=(item.contents[1].find_all("li",{"class":"primary"})[0].text)
         except:
            pass
        
        
        
         company={}
         company['name']=name
         company['postal']=postal
         company['phone']=phone
         company_details.append(company)
#print(emp_details)
with open('output.json', 'w') as f:                             # write data into json file
    output=json.dumps(company_details,indent=1)
    f.write(output)     
print(company_details)
            