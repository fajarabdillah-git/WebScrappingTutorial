import requests
import bs4

print('''========================================================
Hello! This is my documentation on learning web scrapping using python from "2021 Complete Python Bootcamp From Zero to Hero in Python" on Section 15
========================================================
''')

print("\n+++++++++++++++++++++++++++++++++++++++++++++")
print("Video 118. Web Scrapping - Grabbing a Title")
print("+++++++++++++++++++++++++++++++++++++++++++++")
result = requests.get("http://www.example.com")

print("\n==> Implementing 'requests' library <==")
#check the data type of result 
print("\nresult data type: " + str(type(result)))

#check the content of the website
print("\n-----------------------------------------------")
print("Below is the content of the website (same as if you do inspect element on the website)")
print("-----------------------------------------------")
print(result.text)

print("\n==> Implementing 'BeautifulSoup4' or 'bs4' library <==")
print("\n-----------------------------------------------")
print("Below is the content of the website (same as if you do inspect element on the website) using BeautifulSoup4")
print("-----------------------------------------------")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

print("\n-----------------------------------------------")
print("Grab the elements using 'select()' method")
print("=> returns a list of all elements")
print("-----------------------------------------------")

print("\n> Grab <title> element(s)")
site_titles=soup.select('title')
print(site_titles)

print("\n> Grab <h1> element(s)")
site_heading1=soup.select('h1')
print(site_heading1)

print("\n> Grab <p> element(s)")
site_paragraphs=soup.select('p')
print(site_paragraphs)