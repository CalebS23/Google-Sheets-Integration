import pygsheets
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests
from bs4 import BeautifulSoup, element
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

#driver = webdriver.Chrome(executable_path=r"C:\Python\Projects\Google Sheets Integration\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://ubet.ag/')
#driver.maximize_window()


username = driver.find_element(By.NAME, 'Account')
username.clear()
username.send_keys('ZO15')
password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys('CS25')
loginButton = driver.find_element(By.ID, 'login-account')
loginButton.click()



#New BeatifulSoup shit

soup = BeautifulSoup(driver.page_source, 'html.parser')

usdOrange = soup.find("span", id= "ctl00_AccountFiguresLeftMenu_lblRealAvailBalance")
usdOrange2 = soup.find("span", id= "ctl00_AccountFiguresLeftMenu_lblCurrentBalance")






#print(set([t.parent.name for t in text])) # Seeing what parents are in the HTML file

output = ''
blacklist = [
  'div', 'html', 'ul', 'aside', 'form', 'br', 'div', 'title', 'body', 
  'figure', 'main', 'h3', 'article', 'strong', 'noscript', 'ol', 'header', 'em', 
  'section', 'span', 'li', 'blockquote', 'footer', 'nav', '[document]', 'h4', 'label', 'meta', 'h5', 'link',
   'head', 'style', 'script', 'h6', 'input',  'time'
    # there may be more elements you don't want, such as "style", etc.
]

test_array = []
text = soup.find_all(text=True)
for t in text:
  if t.parent.name not in blacklist:
    output += '{} '.format(t)
    test_array.append(t)

print(test_array)

gc = pygsheets.authorize(service_file="C:\Python\Projects\Google Sheets Integration\creds.json")

# Open spreadsheet and then worksheet
sh = gc.open('Python Integration')
sheet = sh.sheet1

# Update a cell with value (just to let him know values is updated ;) )
sheet.update_value('A8', "Output: " + test_array[10])
sheet.update_value('A9', usdOrange.text)
sheet.update_value('A10', usdOrange2.text)
#example_users = np.random.randint
my_nparray = np.random.randint(5, size=(3, 4))

# update the sheet with array
sheet.update_values('A2', my_nparray.tolist())



# share the sheet with your friend
#sh.share("myFriend@gmail.com")






