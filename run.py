import time
from selenium import webdriver
import mysql.connector

cnx = mysql.connector.connect(
  user= '',
  password= '',
  host= '',
  database= '',
  raise_on_warnings= True
)

mycursor = cnx.cursor()

#Do not foreget to change your driver HERE 
driver = webdriver.Safari()

driver.get("https://www.amazon.fr")

#Make a pause of 1 seconds
time.sleep(1)

#Click on accept cookies html element
driver.find_element_by_id('sp-cc-accept').click()

time.sleep(1)

#Select the first child of the class nav-xshop
menu_items = driver.find_element_by_css_selector('#nav-xshop:nth-child(1)').text
#Replace line break by semicolon
menu_items = menu_items.replace("\n", ";")
#Create an array by the <menu_items> variable, who semicolon is the charactere to separate cells
menu_items = menu_items.split(";")

#Define a function which return False if variable var is an empty varchar , otherwise True 
def filtered(var):
    if var == '':
        return False
    else:
        return True

#Make a new array by making a Filter which call filtered function for each value in menu_items array
menu_items = filter(filtered, menu_items)
#Change list'object' to list 
menu_items = list(menu_items)

#remove the two last items in menu_items list
del menu_items[-2:]
#remove the first item in menu_items list
del menu_items[0]

for item in menu_items:
    print(item)
    query = "INSERT INTO titles (content, page) VALUES (%s, %s)"
    values = (item, 0)
    mycursor.execute(query, values)

    cnx.commit()

    print(mycursor.rowcount, "record inserted.")

#Close mysql connexion
cnx.close() 
#Close Selenium driver
driver.close()
