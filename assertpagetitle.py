#Author: Kumar Prasad Dahal
#Date: 2/17/2018

import requests;
from random import shuffle
from selenium import webdriver

url='https://crossbrowsertesting.com/api/v3/selenium/browsers?format=json'
  
#get all data from json file in crossbrowser site.
def fetch_all_browsers(url):
    data = requests.get(url)
    json_response = data.json()
    return json_response
    
#find random browsers for three devices
def get_random_browsers(names, browser_name, edevice):
    #suffle for random browser names
    shuffle(names)
    for random_browser in names:
        device_type = random_browser.get("type")
        device = random_browser.get("device")
        if(browser_name == device_type or edevice == device):
            return random_browser
            
#run selenium test in local server and assert page title is correct or not       
def test_CBT():
    test_devices ={"Windows":"desktop","Mac":"desktop","mobile":"mobile"}
    all_browsers = fetch_all_browsers(url)
    for name,device in test_devices.items():
        #get random browser for only devices and type listed in test_devices dictionary
        random_browser = get_random_browsers(all_browsers, name, device)
        username = "<<user_name>>"
        password  = "<<password>>"
        api_session = requests.Session()
        api_session.auth = (username,password)
        
        caps = {}
        #get browername by extracting from caps key
        caps['browserName'] = random_browser.get("browsers")[0].get("caps").get("browserName")
        caps['platform'] = name
        
        #run test in local server
        #if login authentication is needed, then pass username and password in command_executor
        driver = webdriver.Remote(desired_capabilities=caps,command_executor="http://localhost:8000")
        driver.get("https://smartbear.com/")
        try:
            assert "Software Testing, Monitoring, Developer Tools | SmartBear" == driver.title
            print("Assertion test passed on device "+device+" for browser "+ caps['browserName'])
        
        except Exception as e:
           print("Assertion test failed on device "+device+" for browser "+ caps['browserName'],format(e))
        driver.quit()

print(test_CBT())
