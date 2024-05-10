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
numbers = 0  # Counter for created videos
MAX_UPLOADS = 5  # Maximum number of uploads before taking a break
MAX_CREATIONS = 10  # Maximum number of videos to create

while True:
    upload.deleteAllFilesInFolderIfFilesExist()
    upload.driver.get("https://www.tiktok.com/creator-center/upload?lang=sv-SE")

    while upload.successful_uploads < MAX_UPLOADS and numbers < MAX_CREATIONS:
        if not upload.uploadAnotherButton():
            print("Upload another button clicked.")
            upload.publishButton(upload.getFirstFile())  # Handle file upload

            # Assuming these methods are correctly creating a video
            movieMaking.makeTxtFile()
            movieMaking.ConvertToMp3()
            movieMaking.CreateAImageWithTheDailyQuoteWrittenOnIt()
            movieMaking.CombineImageWithMp3(numbers)
            numbers += 1
            print(f"Movies built: {numbers}")

            print("Starting upload")
            upload.upload()  # Handle the upload logic
            print(f"Videos uploaded: {upload.successful_uploads}")

        time.sleep(10)  # Wait before next action/check

    if upload.successful_uploads >= MAX_UPLOADS:
        print("Maximum uploads reached, taking a break.")
        upload.successful_uploads = 0  # Reset the counter for successful uploads

    if numbers >= MAX_CREATIONS:
        print("Maximum number of videos created, stopping.")
        break  # Exit the main loop if the max number of videos has been created

    # Define break_duration somewhere in your script
    print(f"Taking a break for {break_duration / 3600} hours...")
    time.sleep(break_duration)  # Take a break before the next batch