from bs4 import BeautifulSoup
import requests as rqs
url_link = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"

#get HTML code by url_link
resp = rqs.get(url_link)

#initialize bs4 html parser
soup = BeautifulSoup(resp.text, "html.parser")

#link_name get all span elements, which containts some class name
for link_name in soup.find_all("span", class_="section--previewable-lecture-title--cRADT"):
    print(link_name.get_text())
