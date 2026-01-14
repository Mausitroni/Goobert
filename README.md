> Some parts are required to download outside of this github repostitory

# 🧪 Goobert (v1.0 Demo Release)

> Fully offline, rude, sarcastic voice assistant.  
> Powered by **Vosk** (offline speech recognition) and **GPT4All** (offline LLM).  


## ⚠️ Content Warning

Goobert is intentionally **rude, offensive, and swearing**.  
Do **NOT run this project** if you are sensitive to profanity or toxic behavior.


## 🏢 Ownership & Usage

**Goobert is created and owned by Mausi Studios (Mausitroni).**

- ❌ Do **NOT steal, rebrand, or resell** this project
- ❌ Do **NOT remove credit**
- ❌ Do **NOT claim this as your own**
- ✅ You may fork **for educational or personal use**
- ✅ You may modify **locally** for learning

This project is **FREE** and offline.  
Any commercial misuse is **strictly prohibited**.


## 🖥️ System Requirements

- Windows 10 or 11  
- Python 3.12.10 (⚠️ REQUIRED)  
- Microphone + Speakers or Headphones  
- Basic knowledge of Python and PowerShell  


## 📦 Dependencies

Install using `pip` inside a virtual environment:

```powershell
pip install numpy sounddevice pygame edge-tts vosk gpt4all
```


## 📁 Project Structure
goobert_windows_v1/

├─ goobert.py

├─ models/

│ └─ orca_mini_v3_7b.Q2_K.gguf

├─ vosk/

│ └─ vosk-model-en-us-0.22/

├─ README.md


## ⚠️ Models are too large for GitHub. Download them here:
### GPT model: [Download Orca Mini](https://drive.google.com/file/d/14V26yTFP3f5ZKqTpLDDhB0bMwGoFSyjz/view?usp=sharing)
### Vosk model: [Download Vosk](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip)
> Place them in the `models/` and `vosk/` folders as shown in project structure.



> ⚠️ Important:  
> The virtual environment (`venv/`) is **not included**. Users will create it locally.  


## 📥 Models

### GPT Model
Place your GPT4All model and replace the existing model in: models/orca_mini_v3_7b.Q2_K.gguf (not necessary)


## 🚀 Setup Instructions

1. **Install Python 3.12.10**  
   [Download here](https://www.python.org/downloads/release/python-31210/)

2. **Open PowerShell in project folder**

3. **Create a virtual environment**:

```powershell
python -m venv venv

3. Create a virtual environment:
venv\Scripts\Activate.ps1

5. Install dependencies:
pip install --upgrade pip
pip install numpy sounddevice pygame edge-tts vosk gpt4all

6. Edit paths in goobert.py
GPT_MODEL_PATH = r".\models\orca_mini_v3_7b.Q2_K.gguf" # MAKE SURE TO DOWNLOAD THE MODELS FROM THE LINK
VOSK_MODEL_PATH = r".\vosk\vosk-model-en-us-0.22" # MAKE SURE TO DOWNLOAD THE MODELS FROM THE LINK
MIC_INDEX = 1

7. Run goobert
python goobert.py
```
## 🎙️ How It Works

- Goobert speaks first upon startup  
- Microphone **automatically disables** while Goobert is speaking  
- After speaking, mic stays **OFF**  
- Press **P** to re-enable mic  
- Speak clearly: Goobert responds  
- Mic disables automatically again


## ⌨️ Controls

| Key | Action |
|---|---|
| P | Enable microphone |
| Ctrl + C | Quit program |

## 🟢 Console Color Codes

| Color | Meaning |
|---|---|
| 🟢 Green | Success / mic toggled / model loaded |
| 🟡 Yellow | Warning / non-fatal error |
| ⚪ White | Normal logs / dialogue |
| 🔴 Red | Fatal error / crash |


## 📌 Future Releases

- **v1.2**: `activate_goobert.bat` (one-click launcher)  
- **v1.2**: `venv_access.bat` (quick access to virtual environment)  


## ❗ Disclaimer

You run this software at your **own risk**.  

Mausi Studios is **not responsible** for:
- Offensive output
- Hardware issues
- Misuse or trouble
- Emotional or social consequences





## © Mausi Studios — All Rights Reserved

This software, including all code, assets, and models included in this repository, 
is owned by Mausi Studios (Mausitroni).  

- You may fork or modify **for personal or educational use only**.
- Commercial use, redistribution, or rebranding is **strictly prohibited**.
- No part of this software may be sold, resold, or claimed as your own work.
- Attribution to Mausi Studios is required for any public mention.

