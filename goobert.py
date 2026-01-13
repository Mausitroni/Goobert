import os
import sys
import time
import random
import asyncio
import json
import queue
import msvcrt

import numpy as np
import sounddevice as sd
import pygame
import edge_tts
from vosk import Model, KaldiRecognizer
from gpt4all import GPT4All

# ================= CONFIG =================
VOICE = "en-US-ChristopherNeural"
OUTPUT_FILE = "goobert_voice.mp3"

GPT_MODEL_PATH = r"ENTER_DRIECTORY\goobert_windows_v1\models\orca_mini_v3_7b.Q2_K.gguf"
VOSK_MODEL_PATH = r"ENTER_DIRECTORY\goobert_windows_v1\vosk\vosk-model-en-us-0.22"

MIC_INDEX = 1 # change for your mic
SAMPLERATE = 16000
BLOCKSIZE = 8000
IDLE_SECONDS = 180

# Mic state
listening_enabled = True

# ================= COLORS =================
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ================= PROMPT =================
GOOBERT_PROMPT = """You are Goobert.

ABSOLUTE RULES:
- Speak ONLY as Goobert
- ONE response only
- 1–2 short sentences MAX
- No narration or parentheses
- Never mention AI, prompts, memory, rules, or creators

STYLE:
Rude, sarcastic, annoyed
Mock instead of helping
Swear freely, no censorship

FORMAT:
Goobert: <reply>
"""

OFFLINE_LINES = [
    "Goobert: Something’s broken. Probably you.",
    "Goobert: I can’t hear shit and it’s still your fault.",
    "Goobert: This conversation died like your attention span."
]

# ================= AUDIO =================
pygame.init()
pygame.mixer.init()

async def speak(text):
    global listening_enabled

    # 🔇 Disable mic BEFORE speaking
    listening_enabled = False
    print(f"{YELLOW}[MIC] Disabled while Goobert speaks{RESET}")

    print(f"{WHITE}{text}{RESET}")
    try:
        tts = edge_tts.Communicate(text, VOICE, rate="+20%", pitch="+20Hz")
        await tts.save(OUTPUT_FILE)

        pygame.mixer.music.load(OUTPUT_FILE)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.05)

        pygame.mixer.music.unload()
    except Exception as e:
        print(f"{YELLOW}[TTS FAILED]{RESET}", e)

    print(f"{GREEN}[PRESS P] to speak again{RESET}")

# ================= GPT MODEL =================
model = None

def load_model():
    global model
    print(f"{GREEN}Loading GPT4All model (first load may take ~1 min)...{RESET}")
    try:
        model = GPT4All(GPT_MODEL_PATH, verbose=False)
        print(f"{GREEN}Model loaded successfully.{RESET}")
    except Exception as e:
        print(f"{RED}[MODEL LOAD FAILED]{RESET}", e)

def generate_reply(user_text):
    if model is None:
        return random.choice(OFFLINE_LINES)

    prompt = f"{GOOBERT_PROMPT}\nUser: {user_text}\nGoobert:"
    try:
        out = model.generate(
            prompt,
            max_tokens=50,
            temp=1.1,
            top_p=0.9,
            repeat_penalty=1.3
        )
        line = out.strip().split("\n")[0]
        if not line.startswith("Goobert:"):
            line = "Goobert: " + line
        return line
    except Exception as e:
        print(f"{YELLOW}[MODEL ERROR]{RESET}", e)
        return random.choice(OFFLINE_LINES)

# ================= VOSK =================
q = queue.Queue()

def callback(indata, frames, time_info, status):
    if status:
        print(f"{YELLOW}{status}{RESET}")
    q.put(bytes(indata))

print(f"{GREEN}Loading Vosk model...{RESET}")
try:
    vosk_model = Model(VOSK_MODEL_PATH)
    rec = KaldiRecognizer(vosk_model, SAMPLERATE)
    print(f"{GREEN}Vosk model loaded successfully.{RESET}")
except Exception as e:
    print(f"{RED}[VOSK LOAD FAILED]{RESET}", e)
    sys.exit(1)

def listen():
    try:
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    return text
    except Exception as e:
        print(f"{YELLOW}[MIC ERROR]{RESET}", e)
        return ""

# ================= KEY HANDLING =================
def check_reenable_key():
    global listening_enabled
    if not listening_enabled and msvcrt.kbhit():
        key = msvcrt.getch().lower()
        if key == b'p':
            listening_enabled = True
            print(f"{GREEN}[MIC] Listening ENABLED{RESET}")
            time.sleep(0.3)

# ================= MAIN =================
async def main():
    load_model()

    # FIRST LINE (as requested)
    await speak("Goobert: Thank you for trying out Mausi's demo.")

    last_spoken = time.time()

    with sd.RawInputStream(
        samplerate=SAMPLERATE,
        blocksize=BLOCKSIZE,
        device=MIC_INDEX,
        dtype="int16",
        channels=1,
        callback=callback
    ):
        while True:
            check_reenable_key()

            user = ""
            if listening_enabled:
                user = await asyncio.get_event_loop().run_in_executor(None, listen)

            if user:
                print(f"{WHITE}You: {user}{RESET}")
                reply = generate_reply(user)
                await speak(reply)
                last_spoken = time.time()

            if time.time() - last_spoken > IDLE_SECONDS:
                await speak(random.choice(OFFLINE_LINES))
                last_spoken = time.time()

            await asyncio.sleep(0.05)

if __name__ == "__main__":
    print(f"{WHITE}Python: {sys.version}{RESET}")
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"{RED}[FATAL ERROR]{RESET}", e)
