import os
import pandas as pd

# Function to process the folders
def process_translation_folders(english_folder, other_folder, output_folder, language_abbr):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the folders
    en_files = [f for f in os.listdir(english_folder) if f.endswith('.xlsx')]
    other_files = [f for f in os.listdir(other_folder) if f.endswith('.xlsx')]

    # Process matching files
    for en_file in en_files:
        # Extract the "something" part of the English file name
        base_name = en_file.replace('EN', '').replace('.xlsx', '').strip('_').strip()
        
        # Find the corresponding file in the other folder
        matching_file = None
        for other_file in other_files:
            if base_name in other_file:  # Match if "something" is in the other file name
                matching_file = other_file
                break
        
        if not matching_file:
            print(f"No match found for {en_file} in {other_folder}")
            continue

        # Read the English and other language files
        en_path = os.path.join(english_folder, en_file)
        other_path = os.path.join(other_folder, matching_file)

        en_df = pd.read_excel(en_path, header=None, usecols=[0])  # Column A
        other_df = pd.read_excel(other_path, header=None, usecols=[0])  # Column A

        # Combine the data
        combined_df = pd.DataFrame({
            "EN": en_df[0],
            f"{language_abbr}": other_df[0]
        })

        # Define the output file name
        output_file_name = f"EN_{language_abbr}_{base_name}.xlsx"
        output_path = os.path.join(output_folder, output_file_name)

        # Save the combined data to a new Excel file
        combined_df.to_excel(output_path, index=False)
        print(f"Created file: {output_path}")

# Example usage
english_folder = r"C:\Users\USER\Desktop\JMAX\PAID\JIMI\AI-training\30102010 V2\EN"
other_folder = r"C:\Users\USER\Desktop\JMAX\PAID\JIMI\AI-training\30102010 V2\CN"
output_folder = r"C:\Users\USER\Desktop\JMAX\PAID\JIMI\AI-training\DONE"
language_abbr = "AR"  # Replace with appropriate language abbreviation (e.g., "ar", "el", etc.)

process_translation_folders(english_folder, other_folder, output_folder, language_abbr)
