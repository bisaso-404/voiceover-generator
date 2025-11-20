<a name="readme-top"></a>

<!--
!!! IMPORTANT !!!
This README is an example of how you could professionally present your codebase. 
Writing documentation is a crucial part of your work as a professional software developer and cannot be ignored. 

You should modify this file to match your project and remove sections that don't apply.

REQUIRED SECTIONS:
- Table of Contents
- About the Project
  - Built With
  - Live Demo
- Getting Started
- Authors
- Future Features
- Contributing
- Show your support
- Acknowledgements
- License

OPTIONAL SECTIONS:
- FAQ

After you're finished please remove all the comments and instructions!

For more information on the importance of a professional README for your repositories: https://github.com/microverseinc/curriculum-transversal-skills/blob/main/documentation/articles/readme_best_practices.md
-->

<div align="center">
  <!-- You are encouraged to replace this logo with your own! Otherwise you can also remove it. -->
  <img src="https://github.com/user-attachments/assets/a862d06c-626a-4460-9540-1218ca01a0f4" alt="logo" width="140"  height="auto" />

  <br/>

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
- [❓ FAQ (OPTIONAL)](#faq)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [Voiceover Generator] <a name="about-project"></a>

**[The Voiceover Generator]** is an automated Python tool that converts text from Google Sheets into MP3 voiceovers using OpenAI’s Text-to-Speech API, then uploads the generated audio files to Google Drive. It is built for animation studios, educators, content creators, and developers who need fast, automated, scalable voiceover production.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details> <summary>Client</summary> <ul> <li>Google Sheets UI (used as the input interface)</li> </ul> </details> <details> <summary>Server</summary> <ul> <li>Python 3</li> <li>OpenAI TTS API</li> <li>Google APIs (Sheets + Drive)</li> </ul> </details> <details> <summary>Database</summary> <ul> <li>Google Sheets (acts as structured data storage)</li> </ul> </details>

<!-- Features -->

### Key Features <a name="key-features"></a>

- **Automated voiceover generation directly from Google Sheets rows**
- **MP3 generation using OpenAI TTS with high-quality neural voices**
- **Automatic upload to Google Drive, organized into a target folder**
- **Configurable sheet ranges, folder IDs, and script logic**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

This project is used locally, but a sample workflow explanation is available here:

Demo Documentation Link (coming soon)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

You need:

> Python 3.10+

> Google Cloud Project with

> Google Sheets API enabled

> Google Drive API enabled

> OpenAI API key

<!--
Example command:

```sh
 gem install rails
```
 -->

### Setup

Clone this repository to your desired folder:
 ```
git clone https://github.com/yourusername/voiceover-generator.git
cd voiceover-generator

```
Place your Google OAuth credentials:
```
credentials.json  →  project root
```

<!--
Example commands:

```sh
  cd my-folder
  git clone git@github.com:myaccount/my-project.git
```
--->

### Install

Install this project with:
```
pip install -r requirements.txt

```

Set your environment variables:
```
export OPENAI_API_KEY=your_key_here

```
Windows:
```
set OPENAI_API_KEY=your_key_here
```
<!--
Example command:

```sh
  cd my-project
  gem install
```
--->

### Usage

To run the project, execute the following command:
```
python src/main.py
```

The script will:
```

Read the Google Sheet (Scenario + Script columns)

Generate MP3 voiceovers using OpenAI TTS

Upload the MP3 files to your Google Drive folder
```

Run tests
```
(Currently no automated tests — to be added in future versions.)
```
Deployment

This project can be deployed using:
```

Local cron jobs

Cloud Run

GitHub Actions

Any Python execution environment
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--
Example command:

```sh
  rails server
```
--->


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

> Mention all of the collaborators of this project.

👤 **Author1**

- GitHub: [@bisaso-404](https://github.com/bisaso-404)
- Twitter: [@bisaso_r](https://x.com/bisaso_r)
- LinkedIn: [ronnie-bisaso/](https://linkedin.com/in/ronnie-bisaso/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>


- [ ] **Web dashboard for managing sheets and audio outputs**
- [ ] **Support for multiple languages & custom voices**
- [ ] **Background job processing + email notifications**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you find this project useful, please give it a ⭐ on GitHub — it helps a lot!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>
 Special thanks to:

 > OpenAI for the TTS API

 > Google Cloud Platform for Sheets & Drive APIs

 > Microverse for the professional README structure

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ (optional) -->

## ❓ FAQ (OPTIONAL) <a name="faq"></a>

- **Can this generate multiple voice-overs at once?**

  - Yes. Every row in the Google Sheet creates its own MP3 file.

- **Can I use a different TTS provider like Google or Azure?**
 
  - Yes — you can extend voiceover_generator.py to add more providers.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
