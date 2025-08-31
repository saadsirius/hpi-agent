const micBtn = document.getElementById('mic');

let recognizing = false;
let recognizer = null;

function initRecognizer() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert('La reconnaissance vocale n\'est pas supportée par ce navigateur.');
    return null;
  }
  const rec = new SpeechRecognition();
  rec.lang = 'fr-FR';
  rec.interimResults = false;
  rec.maxAlternatives = 1;
  rec.onresult = (e) => {
    const text = e.results[0][0].transcript;
    if (window.__sendText) window.__sendText(text);
  };
  rec.onerror = (e) => console.warn('STT error', e.error);
  rec.onend = () => {
    recognizing = false;
    micBtn.textContent = '🎙️';
  };
  return rec;
}

micBtn.addEventListener('click', () => {
  if (!recognizer) recognizer = initRecognizer();
  if (!recognizer) return;
  if (!recognizing) {
    recognizing = true;
    micBtn.textContent = '⏹️';
    recognizer.start();
  } else {
    recognizer.stop();
    recognizing = false;
    micBtn.textContent = '🎙️';
  }
});
