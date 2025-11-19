# Voiceover Generator

Generates MP3 voiceovers from Google Sheets data using OpenAI's TTS API and uploads them to Google Drive.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up Google API credentials:
   - Create a project in Google Cloud Console
   - Enable Google Sheets API and Google Drive API
   - Create OAuth 2.0 credentials and download as `credentials.json`
   - Place `credentials.json` in the project root

3. Set up OpenAI API:
   - Get your API key from OpenAI
   - Set environment variable: `OPENAI_API_KEY=your_key_here`

4. Configure main.py:
   - Replace `YOUR_SHEET_ID` with your Google Sheet ID
   - Replace `GOOGLE_DRIVE_FOLDER_ID` with your target folder ID
   - Adjust the range if needed (default: `Sheet1!A2:E`)

## Usage

Run the script:
```
python src/main.py
```

The script will:
1. Read scenarios and scripts from your Google Sheet
2. Generate MP3 voiceovers using OpenAI TTS
3. Upload the files to your specified Google Drive folder

## Sheet Format

Your Google Sheet should have:
- Column A: Scenario name
- Column B: Script text
- First row should be headers (skipped by default range A2:E)