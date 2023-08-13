# Setup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)

print(driver.title)

time.sleep(3)
driver.get("https://www.tiktok.com/upload?lang=sv-SE")

def getFirstFile():
    # Set the path to the folder you want to get the first item from
    folder_path = "C:\\Users\\FelixEdenborgh\\Documents\\PythonPrograms\\CreateTiktokVideosAndAutoUpload\\movie" # <-- your folder where the videos are in.

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Get the first file in the folder
    first_file = files[0]

    # Get the name of the first file
    first_file_name = os.path.basename(first_file)

    first_file_path = os.path.join(folder_path, first_file)

    print("First file in folder:", first_file)
    print("Name of first file:", first_file_name)
    return first_file_path


def deleteTheFile(nameOfFileAndPath):
    # delete the film from folder
    time.sleep(2)
    print("Deleting the movie from folder")
    os.remove(nameOfFileAndPath)


def find_element_and_send(method, value):
    try:
        element = None
        if method == "xpath":
            element = driver.find_element(By.XPATH, value)
        elif method == "fullXpath":
            element = driver.find_element(By.XPATH, value)
        elif method == "selector":
            element = driver.find_element(By.CSS_SELECTOR, value)
        elif method == "className":
            element = driver.find_element(By.CLASS_NAME, value)
        elif method == "contenteditableAttribute":
            element = driver.find_element(By.CSS_SELECTOR, value)
        elif method == "ariaRole":
            element = driver.find_element(By.CSS_SELECTOR, value)
        elif method == "ariaExpandedAttribute":
            element = driver.find_element(By.CSS_SELECTOR, value)

        if element:
            element.clear()
            time.sleep(2)
            element.send_keys("Motivational Quote. Check my profile :)")
            time.sleep(2)
            element.send_keys("#motivation" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#inspiration" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#mindset" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#selfimprovement" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#growthmindset" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#positivity" + Keys.ENTER)
            time.sleep(2)
            element.send_keys("#determination" + Keys.ENTER)
            time.sleep(2)
            print(f"Clicked element using {method}: {value}")
            return True
        else:
            print(f"Element not found using {method}: {value}")
            return False
    except NoSuchElementException:
        print(f"Element not found using {method}: {value}")
        return False
    except Exception as e:
        print(f"An error occurred while finding element using {method}: {e}")
        return False

def publishButton(video_path):
    try:
        try:
            time.sleep(15)
            PublishButton = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[7]/div[2]/button')
            PublishButton.click()

            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Xpath dont work")

        try:
            PublishButton = driver.find_element(By.CSS_SELECTOR,
                                                '#root > div > div > div > div.jsx-2907531398.container-v2 > div.jsx-2907531398.contents-v2 > div.jsx-3073379498.form-v2 > div.jsx-3073379498.button-row > div.jsx-3073379498.btn-post > button')
            PublishButton.click()

            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Stylesheet dont work")

        try:
            PublishButton = driver.find_element(By.CLASS_NAME, "css-y1m958")
            PublishButton.click()

            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Class dont work")


    except:
        print("Error")
        return print("Cant find PublishButton")

def upload():
    video_path = getFirstFile()

    print("New upload started")
    driver.get("https://www.tiktok.com/upload?lang=sv-SE")
    try:
        try:
            # uploading video
            # Assuming you have already logged in to TikTok using Selenium and have navigated to the upload page
            time.sleep(5)

            # There is an iframe on the page...
            iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
            driver.switch_to.frame(iframe)

            # Wait until page loads...
            time.sleep(3)

            # Select the input file and send the filename...
            upload = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            upload.send_keys(video_path)
        except:
            print("Cant upload a new video")
        while True:
            try:
                if find_element_and_send("xpath",
                                         "//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div"):
                    break
                time.sleep(10)
                if find_element_and_send("fullXpath",
                                         "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div"):
                    break
                time.sleep(10)
                if find_element_and_send("selector",
                                         "#root > div > div > div > div.jsx-2977532431.container-v2 > div.jsx-2977532431.contents-v2 > div.jsx-3366794632.form-v2 > div.jsx-3366794632.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1768246377.margin-t-4 > div > div > div > div > div > div"):
                    break
                time.sleep(10)
                if find_element_and_send("className", "notranslate"):
                    break
                time.sleep(10)
                if find_element_and_send("contenteditableAttribute", "[contenteditable='true']"):
                    break
                time.sleep(10)
                if find_element_and_send("ariaRole", "[role='combobox']"):
                    break
                time.sleep(10)
                if find_element_and_send("ariaExpandedAttribute", "[aria-expanded='false']"):
                    break
            except:
                print("Error")
                break

        publishButton(video_path)
        """
        try:
            try:
                time.sleep(15)
                PublishButton = driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[7]/div[2]/button')
                PublishButton.click()

                time.sleep(15)
                deleteTheFile(video_path)
            except:
                print("Xpath dont work")

            try:
                PublishButton = driver.find_element(By.CSS_SELECTOR,
                                                    '#root > div > div > div > div.jsx-2907531398.container-v2 > div.jsx-2907531398.contents-v2 > div.jsx-3073379498.form-v2 > div.jsx-3073379498.button-row > div.jsx-3073379498.btn-post > button')
                PublishButton.click()

                time.sleep(15)
                deleteTheFile(video_path)
            except:
                print("Stylesheet dont work")

            try:
                PublishButton = driver.find_element(By.CLASS_NAME, "css-y1m958")
                PublishButton.click()

                time.sleep(15)
                deleteTheFile(video_path)
            except:
                print("Class dont work") 


        except:
            print("Cant find PublishButton")
            print("Error") """

        time.sleep(15)

        try:
            time.sleep(15)
            UploadnewVideoButton = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div/div[2]/div[1]')
            UploadnewVideoButton.click()
        except:
            print("Cant click on adding new video")
        try:
            # Wait for the pop-up to appear and find the button
            popup_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button-selector"))
            )

            # Click the button to dismiss the pop-up
            popup_button.click()
        except:
            print("No popup window")
    except:
        print("Error")
