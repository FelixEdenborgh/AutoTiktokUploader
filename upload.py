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

successful_uploads = 0

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)

print(driver.title)

time.sleep(3)

def getFirstFile():
    # Set the path to the folder you want to get the first item from
    folder_path = "C:\\Users\\FelixEdenborgh\\Documents\\PythonPrograms\\CreateTiktokVideosAndAutoUpload\\movie" # <-- your folder where the videos are in.

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Get the first file in the folder
    if files:
        first_file = files[0]
    else:
        return False

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


def deleteAllFilesInFolderIfFilesExist():
    folder_path = "C:\\Users\\FelixEdenborgh\\Documents\\PythonPrograms\\CreateTiktokVideosAndAutoUpload\\movie"  # <-- your folder where the videos are in.

    # Get a list of all files in the folder
    files_in_folder = os.listdir(folder_path)

    # Check if the list is not empty
    if files_in_folder:
        for filename in files_in_folder:
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
    else:
        print(f"The folder '{folder_path}' is empty.")


def popup():
    try:
        time.sleep(5)
        # Wait for the pop-up to appear and find the button
        popup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button-selector"))
        )

        # Click the button to dismiss the pop-up
        popup_button.click()
    except:
        print("No popup window")

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
            element.send_keys("Check my profile <3 Motivational Quote.")
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


def uploadAnotherButton():
    try:
        uab = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[10]/div/div[2]/div[1]')
        uab.click()
        return print("upload another video button clicked")
    except:
        print("Full xpath dident work")
    try:
        uab = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[10]/div/div[2]/div[1]')
        uab.click()
        return print("upload another video button clicked")
    except:
        print("Xpath dident work")
    try:
        uab = driver.find_element(By.CLASS_NAME, 'tiktok-modal__modal-button is-highlight')
        uab.click()
        return print("upload another video button clicked")
    except:
        print("Class not found")
    try:
        uab = driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.jsx-2977532431.container-v2 > div.jsx-2977532431.contents-v2 > div.jsx-3366794632.form-v2 > div.tiktok-modal__modal-mask > div > div.tiktok-modal__modal-footer.is-horizontal > div.tiktok-modal__modal-button.is-highlight')
        uab.click()
        return print("upload another video button clicked")
    except:
        print("Cant find by selector")



def publishButton(video_path):
    global successful_uploads
    try:
        try:
            time.sleep(15)
            PublishButton = driver.find_element(By.XPATH,
                                                '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div[8]/button[2]')
            PublishButton.click()
            successful_uploads += 1
            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Xpath dont work")

        try:
            time.sleep(15)
            PublishButton = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[8]/button[2]')
            PublishButton.click()
            successful_uploads += 1
            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Full Xpath dont work")

        try:
            PublishButton = driver.find_element(By.CSS_SELECTOR,
                                                '#root > div > div > div > div.jsx-480949468.container-v2.form-panel.flow-opt-v1 > div > div.jsx-2745626608.form-v2.reverse.flow-opt-v1 > div.jsx-2745626608.button-group > button.TUXButton.TUXButton--default.TUXButton--large.TUXButton--primary')
            PublishButton.click()
            successful_uploads += 1
            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Stylesheet dont work")

        try:
            PublishButton = driver.find_element(By.CLASS_NAME, "TUXButton TUXButton--default TUXButton--large TUXButton--primary")
            PublishButton.click()
            successful_uploads += 1
            time.sleep(15)
            deleteTheFile(video_path)
            return print("PublishButton clicked")
        except:
            print("Class dont work")


    except:
        print("Error")
        return print("Cant find PublishButton")


def uploadAnother():
    try:
        try:
            uploadAnother = driver.find_element(By.XPATH, "//*[@id=':r29:']/div[3]/button[2]/div/div")
            return print("Upload another video Xpath vorked")
        except:
            print("Xpath not working for upload another")

        try:
            uploadAnother = driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[3]/button[2]/div/div")
            return print("Upload another video Full Xpath vorked")
        except:
            print("Full Xpath not working for upload another")

        try:
            uploadAnother = driver.find_element(By.CSS_SELECTOR, "#\:r29\: > div.jsx-2656507978.common-modal-footer > button.TUXButton.TUXButton--default.TUXButton--medium.TUXButton--primary > div > div")
            return print("Upload another video Css Selector vorked")
        except:
            print("Selector not working for upload another")

        try:
            uploadAnother = driver.find_element(By.CLASS_NAME, "TUXButton-label")
            return print("Upload another video Class name vorked")
        except:
            print("Class name not working for upload another")

    except:
        print("Unable to find Upload Another button")
        driver.get("https://www.tiktok.com/creator-center/upload?lang=sv-SE")
        return print("Cant find upload another button")

def upload():
    driver.get("https://www.tiktok.com/creator-center/upload?lang=sv-SE")
    video_path = getFirstFile()

    print("New upload started")


    if uploadAnotherButton is False:
        print("No Upload another button located")
    else:
        uploadAnotherButton()
        print("Button Clicked")
    try:

        while True:
            if uploadAnotherButton is False:
                print("No Upload another button located")
            else:
                uploadAnotherButton()
                print("Button Clicked")

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
                break


            try:
                if find_element_and_send("xpath",
                                         "//*[@id='root']/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div"):
                    break
                time.sleep(10)
                if find_element_and_send("fullXpath",
                                         "/html/body/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div"):
                    break
                time.sleep(10)
                if find_element_and_send("selector",
                                         "#root > div > div > div > div.jsx-480949468.container-v2.form-panel.flow-opt-v1 > div > div.jsx-2745626608.form-v2.reverse.flow-opt-v1 > div.jsx-2745626608.caption-wrap-v2 > div > div.jsx-4128635239.caption-markup > div.jsx-4128635239.caption-editor > div > div > div"):
                    break
                time.sleep(10)
                if find_element_and_send("className", "notranslate public-DraftEditor-content"):
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

        time.sleep(15)

        try:
            time.sleep(15)
            UploadnewVideoButton = driver.find_element(By.XPATH,
                                                       '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[8]/div/div[2]/div[1]')
            UploadnewVideoButton.click()
        except:
            print("Cant click on adding new video")

        try:
            time.sleep(15)
            uploadAnother()
        except:
            print("Issue with uploading another button")
        #popup()
    except:
        print("Error")
