import os
import shutil
import re

# Insert your folder path here
folder_path = r"C:\Users\USER\Desktop\JMAX\PAID\JIMI\AI-training\2025\30102010 V2-20250108T103618Z-001\30102010 V2"

# Ensure the folder path exists
if not os.path.exists(folder_path):
    print(f"Folder path {folder_path} does not exist.")
else:
    # Regex pattern to match two-letter language abbreviations (e.g., EN, ES, AR)
    pattern = r"\b[A-Z]{2}\b"

    # Get all files in the folder
    files = os.listdir(folder_path)

    # Track detected abbreviations
    detected_abbreviations = set()

    # Loop through the files
    for file in files:
        # Check if it's a file (not a folder)
        if os.path.isfile(os.path.join(folder_path, file)):
            # Search for language abbreviation in the filename
            match = re.search(pattern, file)
            if match:
                abbr = match.group(0)
                detected_abbreviations.add(abbr)

                # Create a folder for the abbreviation if it doesn't exist
                abbr_folder = os.path.join(folder_path, abbr)
                if not os.path.exists(abbr_folder):
                    os.makedirs(abbr_folder)

                # Move the file to the respective folder
                shutil.move(os.path.join(folder_path, file), abbr_folder)
                print(f"Moved {file} to {abbr} folder.")

    if detected_abbreviations:
        print(f"File organization complete! Detected abbreviations: {', '.join(detected_abbreviations)}")
    else:
        print("No language abbreviations were detected in the filenames.")
