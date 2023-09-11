import movieMaking
import upload
import time

# settings + data
# ---------------------------------------------------------
# Steg 1: Öppna cmd och skriv in cd C:\Program Files (x86)\Google\Chrome\Application
# Steg 2: skriv in detta: chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Selenium\Chrome_Test_Profile
# Steg 3: gå till tiktok.com och logga in
# name: jokingboxer@gmail.com
# pass: Hinsaringen39


# Number of iterations to perform before taking a break
iterations_before_break = 10

# Time to sleep in seconds for the break
break_duration = 3 * 60 * 60  # 5 hours in seconds

numbers = 0
howManyMade = 0
while(True):
    upload.driver.get("https://www.tiktok.com/upload?lang=sv-SE")
    time.sleep(3)

    upload.deleteAllFilesInFolderIfFilesExist()

    time.sleep(10)

    if upload.uploadAnotherButton is False:
        print("No Upload another button located")
    else:
        upload.uploadAnotherButton()
        print("Button Clicked")

    if upload.popup() is False:
        print("No popup")
    else:
        upload.popup()
        print("Popup handled")

    for i in range(iterations_before_break):
        time.sleep(10)

        if upload.uploadAnotherButton is False:
            print("No Upload another button located")
        else:
            upload.uploadAnotherButton()
            print("Button Clicked")

        time.sleep(5)
        upload.publishButton(upload.getFirstFile())

        if upload.popup() is False:
            print("No popup")
        else:
            upload.popup()
            print("Popup handled")

        time.sleep(10)
        movieMaking.makeTxtFile()
        movieMaking.ConvertToMp3()
        movieMaking.CreateAImageWithTheDailyQuoteWrittenOnIt()
        movieMaking.CombineImageWithMp3(numbers)
        numbers = numbers + 1
        howManyMade = howManyMade + 1
        print(f"Movies built: {howManyMade}")

        print("Starting upload")
        time.sleep(10)
        upload.upload()
        print(f"Videos uploaded: {howManyMade}")
        time.sleep(10)



        if iterations_before_break >= 10:
            upload.deleteAllFilesInFolderIfFilesExist()
            time.sleep(10)
            if upload.getFirstFile() is False:
                print("Nothing to upload")
            else:
                upload.publishButton(upload.getFirstFile())

            if upload.popup() is False:
                print("No popup")
            else:
                upload.popup()
                print("Popup handled")

        time.sleep(10)
        print(f"Iteration {i + 1} - Doing something...")

        # Take a break
    print(f"Taking a break for {break_duration / 60 / 60} hours...")
    time.sleep(break_duration)