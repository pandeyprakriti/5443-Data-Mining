"""
Created on Wed Nov 29 12:30:39 2017

@author: prakritipandey
This program will get the name and firm name of lawyers from the website link given below in json format"
"""

import sys
import requests
import bs4
from bs4 import BeautifulSoup
import json



details = []
#website link
url ="https://www.superlawyers.com/texas/toplists/top-100-2017-texas-super-lawyers/96a83c96abbe6d0b40c72b279ebdf76e"            # the websit
#print(url)

# Beautiful soup way
html = requests.get(url).text
soup = BeautifulSoup(html,"html.parser")
data = soup.find_all('div',{'class':"top_list floating_lawyers container"})

for lawyer in data:
    
    
    # find name of lawyer
    names  = lawyer.findNext('p',{'class':"floating_lawyers full_name"})         
    names = names.findNext('a')
    name=names.text
    #find the firm name 
    firmnames=lawyer.findNext('p',{'class':"floating_lawyers firm_name"})
    firmname=firmnames.text
    lawyer_dict = {}                                            
    lawyer_dict['Name'] = name.strip()
    lawyer_dict['Address'] = firmname.strip()
    #append to list
    details.append(lawyer_dict)       
# to save the output file in json format
with open('output.json', 'w+') as f:                             
    output = json.dumps(details,indent=1)     
    f.write(output)
print(details)
