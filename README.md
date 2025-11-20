<a name="readme-top"></a>

<div align="center">
  <h3><b>Voiceover Generator</b></h3>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [❓ FAQ](#faq)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 Voiceover Generator <a name="about-project"></a>

> Automated voiceover generation system that converts Google Sheets data into MP3 audio files.

**Voiceover Generator** is a Python automation tool that reads scenario scripts from Google Sheets, generates high-quality MP3 voiceovers using Groq's PlayAI TTS, and automatically uploads the audio files to Google Drive for easy access and sharing.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Backend</summary>
  <ul>
    <li><a href="https://www.python.org/">Python 3.8+</a></li>
    <li><a href="https://console.groq.com/">Groq API (PlayAI TTS)</a></li>
  </ul>
</details>

<details>
  <summary>APIs & Services</summary>
  <ul>
    <li><a href="https://developers.google.com/sheets/api">Google Sheets API</a></li>
    <li><a href="https://developers.google.com/drive/api">Google Drive API</a></li>
  </ul>
</details>

<!-- Features -->

### Key Features <a name="key-features"></a>

- **Automated TTS Generation**: Convert text scripts to high-quality MP3 voiceovers using Groq's PlayAI
- **Google Sheets Integration**: Read scenario data directly from Google Sheets
- **Google Drive Upload**: Automatically upload generated audio files to specified Drive folders

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

> This is a desktop automation tool - no live demo available.

- See the [Usage](#usage) section for running instructions

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python 3.8 or higher
- pip (Python package installer)
- Google Cloud Console account
- Groq API account

### Setup

Clone this repository to your desired folder:

```sh
  cd my-folder
  git clone <repository-url>
  cd voiceover-generator
```

### Install

Install this project with:

```sh
  pip install -r requirements.txt
```

**Setup Google API credentials:**
1. Create a project in Google Cloud Console
2. Enable Google Sheets API and Google Drive API
3. Create OAuth 2.0 credentials (Desktop application)
4. Download as `credentials.json` and place in project root

**Setup Groq API:**
1. Get your API key from Groq Console
2. Create `.env` file: `GROQ_API_KEY=your_key_here`

**Configure your data:**
- Update `SHEET_ID` in `src/main.py` with your Google Sheet ID
- Update `PARENT_FOLDER_ID` with your Google Drive folder ID

### Usage

To run the project, execute the following command:

```sh
  python src/main.py
```

**Sheet Format:**
- Column A: Scenario name
- Column B: Script text
- First row should be headers (range starts from A2)

### Run tests

To test TTS functionality:

```sh
  python src/test_tts.py
```

### Deployment

This is a desktop automation tool. No deployment needed - run locally as needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Bronn**

- GitHub: [@bronn](https://github.com/bronn)
- LinkedIn: [LinkedIn](https://linkedin.com/in/bronn)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] **Multiple Voice Options**: Support for different PlayAI voices
- [ ] **Batch Processing**: Process multiple sheets simultaneously
- [ ] **Audio Quality Settings**: Configurable bitrate and format options

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

> If this project helps automate your voiceover workflow, please give it a star!

If you like this project and find it useful for your automation needs, please consider giving it a ⭐️!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

> Thanks to the amazing APIs and services that make this automation possible.

I would like to thank:
- Groq for their excellent PlayAI TTS service
- Google for their robust Sheets and Drive APIs
- The Python community for excellent libraries

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ -->

## ❓ FAQ <a name="faq"></a>

- **What voice options are available?**

  - Currently using "Aaliyah-PlayAI". Check Groq's PlayAI documentation for more voice options.

- **Can I use different Google accounts for Sheets and Drive?**

  - The OAuth flow uses one Google account for both services. Ensure your account has access to both the sheet and drive folder.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>