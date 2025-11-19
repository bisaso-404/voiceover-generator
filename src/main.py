from google_reader import read_sheet, upload_to_drive
from voiceover_generator import generate_voice
import os
from dotenv import load_dotenv

load_dotenv


SHEET_ID = os.getenv("SHEET_ID")
PARENT_FOLDER_ID = os.getenv("PARENT_FOLDER_ID")
RANGE = "'The Seven Signs of Life'!A1:B7"

def main():
    rows = read_sheet(SHEET_ID, RANGE)

    # Combine all scripts into one
    all_scripts = []
    for row in rows[1:]:
        if len(row) >= 2:
            all_scripts.append(row[1])

    combined_script = " ".join(all_scripts)

    # Generate one audio file
    filename = "VO_Complete_Biology-3.wav"
    output_path = os.path.join("output", filename)

    print("Generating:", filename)
    generate_voice(combined_script, output_path)

    print("Uploading to Drive…")
    file_id = upload_to_drive(output_path, PARENT_FOLDER_ID)
    print("Uploaded file ID:", file_id)

if __name__ == "__main__":
    main()
