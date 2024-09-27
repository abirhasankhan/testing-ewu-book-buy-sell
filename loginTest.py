from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Specify the path to the ChromeDriver executable
service = Service(executable_path="C:\chrome-win64\chrome.exe")

# Configure Chrome options
options = webdriver.ChromeOptions()
# chrome browser ------> chromedriver
# open the chrome browser
driver = webdriver.Chrome()

testSuiteUsername = ['2019-1-60-013@std.ewubd.edu']
testSuitePassword = ['123']

def test_localhostLogin(username,password,i):

    # Navigate to the url
    driver.get("http://localhost/www/userView/login.php")
    time.sleep(3)
    #  setWindowSize | 1920x1040 |
    # driver.set_window_size(1920, 1040)
    # Maximize
    driver.maximize_window()

    driver.find_element(By.ID, "s_email").send_keys(username)
    time.sleep(3)

    driver.find_element(By.ID, "s_password").send_keys(password)
    time.sleep(3)

    driver.find_element(By.ID, "signinbtn").click()
    # wait for 5 sec
    time.sleep(3)

    get_url = driver.current_url
    if(get_url=="http://localhost/www/userView/home.php"):
        print("test- "+str(i)+" successfully logged in")
        time.sleep(3)
    elif(get_url=="http://localhost/www/userView/login.php?errcode=1"):
        print("test- "+str(i)+" failed to logged in")
    else:
        print("something else happened")

lenofList=len(testSuiteUsername)
for i in range(0,lenofList):
    test_localhostLogin(testSuiteUsername[i],testSuitePassword[i],i+1)
#close the window'
#driver.close()
