from loginTest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

testSearch = ['java']

def test_Search(search, i):
    # Navigate to the URL
    driver.get("http://localhost/www/userView/all_req.php")
    time.sleep(3)
    # Maximize the window
    driver.maximize_window()

    # Find and fill the search input field
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()  # Clear any previous input
    search_input.send_keys(search)

    # Click the search button
    search_button = driver.find_element(By.NAME, "search_submit")
    search_button.click()
    time.sleep(3)

    get_url = driver.current_url

    # Check if the search results are displayed
    if "all_req.php" in driver.current_url:
        print("test- " + str(i) + " successfully in request page")

        # Locate all the "VIEW" links on the page
        try:

            view_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'view')]")
            print(f"Found {len(view_links)} VIEW links.")
            # Click on each "VIEW" link
            for j, view_link in enumerate(view_links, start=1):
                view_link.click()
                print(view_link)
                print(f"Clicked on VIEW link {j}.")

                # Wait for the page to load (you can use a specific condition here)
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//element-you-expect-on-the-new-page")))

                # Perform actions on the request page
                # ...
                time.sleep(2)  # Add a delay if needed
                # Go back to the search results page
                driver.back()


        except:
            print("VIEW links not found or empty. Skipping.")

    elif get_url == "http://localhost/www/userView/all_req.php?errcode=1":
        print("test- " + str(i) + " failed to log in")
    else:
        print("something else happened")

lenofList = len(testSearch)
for i in range(lenofList):
    test_Search(testSearch[i], i + 1)

# Close the window
driver.close()
