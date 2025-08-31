const chat = document.getElementById('chat');
const msg = document.getElementById('msg');
const send = document.getElementById('send');
const mic = document.getElementById('mic');
const tts = document.getElementById('tts');

const API = 'http://127.0.0.1:8000/api/chat';
const SID = 'local-dev';

function addBubble(role, text) {
  const wrap = document.createElement('div');
  wrap.className = role === 'user' ? 'flex justify-end' : 'flex justify-start';
  const bubble = document.createElement('div');
  bubble.className = role === 'user'
    ? 'max-w-[85%] bg-indigo-600 text-white rounded-lg px-3 py-2 my-1'
    : 'max-w-[85%] bg-slate-800 text-slate-100 border border-slate-700 rounded-lg px-3 py-2 my-1';
  bubble.textContent = text;
  wrap.appendChild(bubble);
  chat.appendChild(wrap);
  chat.scrollTop = chat.scrollHeight;
}

async function sendText(text) {
  if (!text) return;
  addBubble('user', text);
  msg.value = '';
  try {
    const res = await fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, session_id: SID })
    });
    const data = await res.json();
    const reply = data.reply || '(aucune réponse)';
    addBubble('assistant', reply);
    if (tts.checked) speak(reply);
  } catch (e) {
    addBubble('assistant', 'Erreur de connexion au backend.');
  }
}

send.addEventListener('click', () => sendText(msg.value));
msg.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendText(msg.value);
});

// Expose for voice.js
window.__sendText = sendText;

// Basic TTS using browser Speech Synthesis
function speak(text) {
  if (!('speechSynthesis' in window)) return;
  const u = new SpeechSynthesisUtterance(text);
  u.lang = 'fr-FR';
  speechSynthesis.speak(u);
}
