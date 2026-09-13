import os
import shutil

# Ask user for folder location
folder_location = input("Enter the folder location: ")

# Check if folder exists
if not os.path.exists(folder_location):
    print("Folder does not exist.")
else:

    # File extensions and their folder names
    file_types = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",

        ".pdf": "PDF Files",

        ".mp4": "Videos",
        ".mkv": "Videos",

        ".docx": "Documents",
        ".txt": "Documents",

        ".mp3": "Music"
    }

    # Get all files and folders
    for filename in os.listdir(folder_location):

        file_path = os.path.join(folder_location, filename)

        # Only process files, not folders
        if os.path.isfile(file_path):

            # Get file extension
            extension = os.path.splitext(filename)[1].lower()

            # Check whether extension is in dictionary
            if extension in file_types:

                # Get destination folder name
                folder_name = file_types[extension]

                # Create destination folder path
                destination_folder = os.path.join(
                    folder_location, folder_name
                )

                # Create folder if it doesn't exist
                os.makedirs(destination_folder, exist_ok=True)

                # Destination file path
                destination_path = os.path.join(
                    destination_folder, filename
                )

                # Move the file
                shutil.move(file_path, destination_path)

                print(f"Moved {filename} to {folder_name}")

    print("\nAll files organized successfully!")