import requests
from bs4 import BeautifulSoup 
import pandas as bd
r = requests.get("https://www.timeanddate.com/weather/pakistan/lahore/ext")
print(r.text)
soup = BeautifulSoup(r.text,'html.parser')