# HPI Agent (Local, Free, Tailwind UI + Voice)

A local, modular **HPI (Haut Potentiel Intégré)** agent you can run on your machine:
- 🧠 **LangGraph** backbone
- 🧰 **FastAPI** backend
- 🧼 **Frontend** single-file with **Tailwind CSS (CDN)** for a clean look
- 🔉 **Voice Activation** in the browser via **Web Speech API** (no cloud dependency)
- 🧩 Agents skeleton (HPI Core, ODIN, Neuro-sensorial, Learning, etc.)
- 🐳 Optional **Ollama** integration for a local LLM

> Minimal by design: no complex bundlers; you can later migrate to Vite/Next if you want.

---

## 1) Prérequis

- Python 3.10+
- `pip` (ou `uv`)
- (Optionnel) **Ollama** si tu veux un LLM local prêt à l’emploi
  ```bash
  # macOS / Linux
  curl -fsSL https://ollama.com/install.sh | sh
  # Exemple de modèle
  ollama pull mistral
  ```

---

## 2) Installation backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
uvicorn main:app --reload
```
Par défaut, l’API écoute sur `http://127.0.0.1:8000`.

---

## 3) Lancer le frontend (statique)

Ouvre `frontend/index.html` dans ton navigateur (double-clic suffit).  
Tu peux aussi servir le dossier via un serveur local si nécessaire (ex. `python -m http.server -d frontend 8080`).

Le frontend appelle le backend `http://127.0.0.1:8000/api/chat` par défaut.

---

## 4) Utiliser la voix 🎙️

- Clique sur 🎙️ **Micro** pour dicter (Chrome recommandé).  
- Le TTS utilise `speechSynthesis` intégré au navigateur.  
- **100% local** (pas de cloud requis).

---

## 5) Intégration LLM local

Par défaut, le backend renvoie des réponses factices (pour tester l’UI).  
Active **Ollama** en réglant `USE_OLLAMA=True` dans `backend/config.py` et choisis ton modèle.

```bash
# Exemple de test rapide côté terminal
curl -X POST http://127.0.0.1:8000/api/chat -H "Content-Type: application/json" -d '{"message":"Bonjour", "session_id":"dev"}'
```

---

## 6) Structure

```
hpi-agent/
├─ backend/
│  ├─ main.py
│  ├─ config.py
│  ├─ graph.py
│  ├─ agents/
│  │  ├─ hpi_core.py
│  │  ├─ odin.py
│  │  ├─ neuro.py
│  │  └─ learning.py
│  └─ requirements.txt
└─ frontend/
   ├─ index.html
   ├─ app.js
   └─ voice.js
```

---

## 7) Push sur GitHub

```bash
git init
git remote add origin https://github.com/saadsirius/hpi-agent.git
git branch -M main
git add .
git commit -m "Initial commit: HPI Agent skeleton (FastAPI + Tailwind + Voice)"
git push -u origin main
```

---

## 8) Prochaines étapes

- Remplacer la réponse factice par l’**HPI Graph** (voir `backend/graph.py`)
- Ajouter des sous-agents (ODIN, Neuro, Learning)
- (Optionnel) Migrer le frontend vers **Vite/React + Tailwind CLI**

Bon build 🚀
