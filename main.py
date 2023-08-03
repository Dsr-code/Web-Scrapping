# Reqirements needed
import requests
from bs4 import BeautifulSoup

# Entering the url of the website to be scraped

url="https://codewithharry.com"

# Getting the html
r=requests.get(url)
htmlcontent= r.content
# print(htmlcontent)


# Then parse the html
soup=BeautifulSoup(htmlcontent,"html.parser")
# print(soup.prettify)


# Then html tree traversal
title=soup.title
print(title.string)

# Commonly used Objects in  Beautiful Soup
'''
1. Tag
print(type(title))

2.NavigableString
print(type(title.string))

3.BeautifulSoup
print(type(soup))

4.Comment
'''
# markup = "<p><!--This is a comment--></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)


title=soup.title

# to get all the paragraphs from the page
paras= soup.find_all('p')


# to get the only first paragraph
firstpara= soup.find('p')



# to get the class of this para 
firstpara= soup.find('p')['class']

# NOTE- "key error" if the element is not present in the html page

# to find a element with desire class we can use this 

leadClass = soup.find_all('p',class_="lead")   #this will print the elements of the page with class = lead

# to get the text from the tags/soup 
text = soup.find('p').get_text()

# to get the text from the whole page 
alltext= soup.get_text()

# * to get all the links from the web page 
anchors= soup.find_all('a')

# to get all the anchor tags from the page
'''
for link in anchors:
    print(link.get('href'))
'''
# NOTE - BUT THIS WILL PRINT ALL THE LINKS EVEN IF THEY ARE REPEATED, TO SOLVE THIS WE HAVE TO 

all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linktxt="https://codewithharry.com" + link.get('href')
        all_links.add(linktxt)
        print(linktxt)                                             #this will print all the links except pounds

'''
for i in all_links:
    print(i)
'''
# NOTE - this will print all the links which are not repeated and are redirectable
     

# .content - A Tag's children are available as a list 
# .children - A tag's children are available as a generator 

navbarSupportedContent = soup.find(id='navbarSupportedContent') 

# prints all the strings present in the navbarSupportedContent id 
for items in navbarSupportedContent.strings:
    print(items)

# to print all the strings present in the navbarSupportedContent id with a formatted manner 
for itms in navbarSupportedContent.stripped_strings:
    print(itms)


# to get the parent tag of the element 
parentOfnavbarSupportedContent = (navbarSupportedContent.parent)

# to get all the parents of the element 
AllparentOfnavbarSupportedContent = (navbarSupportedContent.parents)   # this is a generator and we have to iterate it with for loop to get the parent structure
#like
for items in AllparentOfnavbarSupportedContent:
    print(items.name)

# to print the next sibling of the parent that means the next element with same parent 
print(navbarSupportedContent.next_sibling.next_sibling)

# to print the previous sibling of the parent that means the next element with same parent 
print(navbarSupportedContent.previous_sibling.previous_sibling)


# to get the whole element code we can use the css selector - here, id 
elem = soup.select('#login-modal')


# to get the whole element code we can use the css selector - here, class
elem = soup.select('.modal-footer')
print(elem)

# This prints a list of element codes that have the same class as "modal-footer"




#********************************* Its all about practice not about memorising *********************************




# NOTE - Go through the documentation to know more 