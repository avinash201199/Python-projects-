import requests
from bs4 import BeautifulSoup
import webbrowser


while True:
    a = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(a)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_ = "firstHeading").text
    print(title + "\nDo You want to view it? (Y/N)")
    ans = str(input(""))
    if (ans.lower() == "y"):
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        break
    elif (ans.lower() == "n"):
        print("ok\nTrying again!")
        continue
    else:
        print("Wrong Choice!!!")
        break
