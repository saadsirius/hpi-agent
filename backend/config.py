import os

# Toggle Ollama on/off
USE_OLLAMA = os.getenv("USE_OLLAMA", "False").lower() == "true"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_ENDPOINT = os.getenv("OLLAMA_ENDPOINT", "http://127.0.0.1:11434/api/generate")
