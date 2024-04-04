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

upload.deleteAllFilesInFolderIfFilesExist()

# Time to sleep in seconds for the break
break_duration = 3 * 60 * 60

numbers = 0
while True:
    upload.deleteAllFilesInFolderIfFilesExist()
    upload.driver.get("https://www.tiktok.com/creator-center/upload?lang=sv-SE")
    time.sleep(6)  # Simplified redundant sleeps

    if not upload.uploadAnotherButton():
        print("No Upload another button located")
    else:
        print("Button Clicked")

    # Assuming the popup handling and other interactions are correctly implemented in your upload.upload() method
    # and that successful_uploads is correctly updated in your publishButton method

    while upload.successful_uploads < 10:
        time.sleep(10)
        if not upload.uploadAnotherButton():
            print("No Upload another button located")
        else:
            print("Button Clicked")

        upload.publishButton(upload.getFirstFile())  # Assuming this correctly handles the file upload

        movieMaking.makeTxtFile()
        movieMaking.ConvertToMp3()
        movieMaking.CreateAImageWithTheDailyQuoteWrittenOnIt()
        movieMaking.CombineImageWithMp3(numbers)
        numbers += 1
        print(f"Movies built: {numbers}")

        print("Starting upload")
        upload.upload()  # This should encapsulate the upload logic and update successful_uploads
        print(f"Videos uploaded: {upload.successful_uploads}")
        time.sleep(10)

        if upload.getFirstFile() is False:
            upload.deleteAllFilesInFolderIfFilesExist()

        # Additional check to ensure we break out of the loop if 10 videos have been uploaded
        if upload.successful_uploads >= 10:
            print(f"Uploaded 10 videos, taking a break.")
            upload.successful_uploads = 0  # Reset the counter
            break  # Break out of the while loop to take a break

    print(f"Taking a break for {break_duration / 3600} hours...")
    time.sleep(break_duration)