from loginTest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

testSearch = ['King Of Wrath', 'java', 'of']

def test_Search(search, i):
    # Navigate to the URL
    driver.get("http://localhost/www/userView/bookBuy.php")
    time.sleep(3)
    # Maximize the window
    driver.maximize_window()

    my_el = driver.find_element(By.ID, "search").send_keys(search)
    time.sleep(3)

    driver.find_element(By.ID, "search_submit").click()
    time.sleep(3)

    get_url = driver.current_url
    if get_url == "http://localhost/www/userView/bookBuy.php":
        print("test- " + str(i) + " successfully in bookBuy page")

        # Locate all the "VIEW" links on the page
        try:
            view_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'VIEW')]")
            print(f"Found {len(view_links)} VIEW links.")

            # Click on each "VIEW" link
            for j, view_link in enumerate(view_links, start=1):
                view_link.click()
                print(f"Clicked on VIEW link {j}.")

                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.XPATH, "//element-you-expect-on-the-new-page")))

                # Perform actions for each item, e.g., view details
                # ...
                time.sleep(2)  # Adjust the sleep duration as needed
                # Go back to the search results page
                driver.back()

        except:
            print("VIEW links not found or empty. Skipping.")

    elif get_url == "http://localhost/www/userView/bookBuy.php?errcode=1":
        print("test- " + str(i) + " failed to log in")
    else:
        print("something else happened")

lenofList = len(testSearch)
for i in range(lenofList):
    test_Search(testSearch[i], i + 1)

# Close the window
driver.close()
