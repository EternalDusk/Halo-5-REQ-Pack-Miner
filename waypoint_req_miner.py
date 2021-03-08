#selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from colorama import Fore, Back, Style, init

import time

init(autoreset=True)

#==INPUTS==
#microsoft email
email = 
#microsoft password
password = 
#==========



def click_button(name, xpath):
    print(Fore.YELLOW + "Clicked: " + name)
    name = browser.find_element_by_xpath(xpath)
    name.click()
    time.sleep(1)

def enter_info(name, xpath, sent):
    print(Fore.YELLOW + "Sent: " + Style.RESET_ALL + sent + " to " + name)
    name = browser.find_element_by_xpath(xpath)
    name.clear()
    name.send_keys(sent)
    
    time.sleep(1)




browser = webdriver.Chrome(executable_path=r"chromedriver.exe")

browser.get("https://www.halowaypoint.com/en-us")
#let website load
time.sleep(3)


#==LOGGING IN==
#sign in
click_button("Sign In", "/html/body/div[2]/header/div/div/div/a[2]")

#enter sign in info
enter_info("email", "/html/body/div/form[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]", email)
#press next
click_button("submit", "/html/body/div/form[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input")

#enter password
enter_info("password", "/html/body/div/form[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input", password)
#press login
click_button("submit", "/html/body/div/form[1]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input")
#==============



#==DAILY REQ PACKS==
try:
    #go to req packs
    browser.get("https://www.halowaypoint.com/en-us/games/halo-5-guardians/xbox-one/requisitions/unopened-packs")

    #let packs load
    time.sleep(1)

    #find daily packs
    click_button("Daily REQ Pack", "/html/body/div[2]/main/div[2]/div/div/div/div/div[2]/div/div/button")
    click_button("YES", "/html/body/div[3]/div/div/div/div/footer/div/ul/li[1]/button")

    #let reqs load
    time.sleep(2)

    #close window
    click_button("Close", "/html/body/div[3]/div/div/div/button")
except:
    print(Fore.RED + "REQ CLAIM FAILED")
#===================



#==SELL REQS==
#POWER WEAPONS
browser.get("https://www.halowaypoint.com/en-us/games/halo-5-guardians/xbox-one/requisitions/categories/powerandvehicle?ownedOnly=True")

try:
    click_button("More Power Weapons", "/html/body/div[2]/main/div[2]/div[1]/div/div/div[11]/ul/li/a")
except:
    print("Power Weapons Button not found")
try:
    click_button("More Vehicles", "/html/body/div[2]/main/div[2]/div[2]/div/div/div[8]/ul/li/a")
except:
    print("Vehicles Button not found")


reqs_owned = browser.find_elements_by_class_name("card.have-owned.have-inventory")

print(Fore.BLUE + "Number of REQs found: " + str(len(reqs_owned)))
for i in reqs_owned:
    print(i)
    i.click()
    weapon_sold = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]").text
    print(Fore.GREEN + "Selling REQ: " + weapon_sold)
    time.sleep(1)
    click_button("Sell Card", "/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/button")
    time.sleep(1)
    click_button("Yes", "/html/body/div[4]/div/div/div/div/footer/div/ul/li[1]/button")
    time.sleep(1)
    click_button("Close", "/html/body/div[3]/div/div/div/button")



#ARENA BOOSTS
browser.get("https://www.halowaypoint.com/en-us/games/halo-5-guardians/xbox-one/requisitions/categories/boost?ownedOnly=True")

try:
    click_button("More Arena", "/html/body/div[2]/main/div[2]/div[1]/div/div/div[4]/ul/li/a")
except:
    print("Arena Button not found")
try:
    click_button("More Warzone", "/html/body/div[2]/main/div[2]/div[2]/div/div/div[4]/ul/li/a")
except:
    print("Warzone Button not found")

reqs_owned = browser.find_elements_by_class_name("card.have-owned.have-inventory")

print(Fore.BLUE + "Number of REQs found: " + str(len(reqs_owned)))
for i in reqs_owned:
    print(i)
    i.click()
    req_sold = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[2]/div[1]").text
    print(Fore.GREEN + "Selling REQ: " + req_sold)
    time.sleep(1)
    click_button("Sell Card", "/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/button")
    time.sleep(1)
    click_button("Yes", "/html/body/div[4]/div/div/div/div/footer/div/ul/li[1]/button")
    time.sleep(1)
    click_button("Close", "/html/body/div[3]/div/div/div/button")
#=============



#==UPDATE REQ POINTS==
browser.refresh()

req_points = browser.find_element_by_xpath("/html/body/div[2]/main/div[2]/div/div/a/div/div[1]").text
print(Fore.BLUE + "Current REQ Points: " + req_points)

if (int(req_points) > 10000):
    print(Fore.YELLOW + "YOU CAN PURCHASE A GOLD PACK")
#=====================