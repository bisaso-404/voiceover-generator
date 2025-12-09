
from google_reader import read_sheet, upload_to_drive, get_sheet_names
from voiceover_generator import generate_voice
import os
from dotenv import load_dotenv
import re

load_dotenv()

SHEET_ID = os.getenv("SHEET_ID")
PARENT_FOLDER_ID = os.getenv("PARENT_FOLDER_ID")

def main():
    # Get all sheet names
    sheet_names = get_sheet_names(SHEET_ID)
    
    for sheet_name in sheet_names:
        print(f"Processing sheet: {sheet_name}")
        
        # Read data from current sheet
        range_name = f"'{sheet_name}'!B:B"  
        rows = read_sheet(SHEET_ID, range_name)
        
        # Combine all scripts (skip header)
        all_scripts = []
        for row in rows[1:]:
            if row:  # Check if row has data
                all_scripts.append(row[0])
        
        if not all_scripts:
            print(f"No data in {sheet_name}, skipping...")
            continue
            
        combined_script = " ".join(all_scripts)
        
        # Generate audio file
        # Clean filename - remove invalid characters
        clean_name = re.sub(r'[<>:"/\\|?*]', '', sheet_name).replace(' ', '_')
        filename = f"{clean_name}.wav"
        output_path = os.path.join("output", filename)
        
        print(f"Generating: {filename}")
        generate_voice(combined_script, output_path)
        
        print("Uploading to Drive...")
        file_id = upload_to_drive(output_path, PARENT_FOLDER_ID)
        print(f"Uploaded {filename}, file ID: {file_id}")

if __name__ == "__main__":
    main()

