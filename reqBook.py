from loginTest import *
from selenium.webdriver.common.by import By
import time

bookName = ['java']
bookWrite = ['unknown']
bookDis = ['for java']

def test_Req(bookName,bookWrite,bookDis,i):

    # Navigate to the url
    driver.get("http://localhost/www/userView/req_book.php")
    time.sleep(3)
    #  setWindowSize | 1920x1040 |
    # driver.set_window_size(1920, 1040)
    # Maximize
    driver.maximize_window()

    driver.find_element(By.NAME, "book_name").send_keys(bookName)
    time.sleep(3)

    driver.find_element(By.NAME, "writer_name").send_keys(bookWrite)
    time.sleep(3)

    driver.find_element(By.NAME, "book_detail").send_keys(bookDis)
    time.sleep(3)

    driver.find_element(By.ID, "req_book").click()
    # wait for 3 sec
    time.sleep(3)

    get_url = driver.current_url
    if(get_url=="http://localhost/www/userView/req_book_info.php"):
        print("test- "+str(i)+" successfully book requested")
        # Adding the anchor element with a link to my_req.php
        anchor_element = driver.find_element(By.XPATH, "/html/body/section/div/b/a")
        anchor_text = anchor_element.text
        anchor_link = anchor_element.get_attribute("href")
        print(f"Link: {anchor_text} - {anchor_link}")
        anchor_element.click()
        # Wait for some time (you can uncomment the line below if needed)
        # time.sleep(3)
    elif(get_url=="http://localhost/www/userView/req_book.php?errcode=1"):
        print("test- "+str(i)+" failed to request")
    else:
        print("something else happened")

lenofList=len(bookName)
for i in range(0,lenofList):
    test_Req(bookName[i],bookWrite[i],bookDis[i], i+1)
#close the window'
driver.close()