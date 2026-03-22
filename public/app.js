/* =========================================================
   Vow Vision — Wedding AI Studio
   Gemini API: gemini-3-pro-image-preview
   ========================================================= */

'use strict';

// ── Scene Presets ─────────────────────────────────────────
const SCENES = [
  {
    id: 'chapel',
    icon: '⛪',
    name: 'Chapel',
    prompt: 'inside a grand European chapel with soaring stone arches, stained glass windows casting colorful light, candles lining the aisle, bouquets of white roses on wooden pews',
  },
  {
    id: 'garden',
    icon: '🌿',
    name: 'Garden',
    prompt: 'in a lush English garden with blooming peonies and roses, trailing wisteria, a pergola draped in white flowers, dappled golden afternoon sunlight filtering through the trees',
  },
  {
    id: 'beach',
    icon: '🌊',
    name: 'Beach',
    prompt: 'on a pristine white sand beach at golden hour, gentle waves in the background, warm orange and pink sunset sky reflecting on the wet sand, soft sea breeze',
  },
  {
    id: 'forest',
    icon: '🌲',
    name: 'Forest',
    prompt: 'in a misty enchanted forest with ancient oak trees, soft morning light streaming through the canopy, moss-covered ground, wildflowers scattered along a winding path',
  },
  {
    id: 'palace',
    icon: '🏛️',
    name: 'Palace',
    prompt: 'in the ornate hall of a European palace with gilded baroque architecture, grand crystal chandeliers, marble floors with intricate inlay, tall arched windows overlooking formal gardens',
  },
  {
    id: 'vineyard',
    icon: '🍇',
    name: 'Vineyard',
    prompt: 'among rolling Tuscan vineyard hills at sunset, golden grapevines stretching into the distance, a rustic stone villa in the background, warm amber and golden hour light',
  },
  {
    id: 'cityscape',
    icon: '🌆',
    name: 'City',
    prompt: 'on a rooftop terrace overlooking a glittering city skyline at blue hour, twinkling city lights below, a subtle mist, elegant string lights framing the space',
  },
  {
    id: 'lake',
    icon: '🏔️',
    name: 'Lake',
    prompt: 'beside a crystal mountain lake reflecting snow-capped peaks, wildflowers along the water\'s edge, a wooden dock stretching out over the glassy water, perfect mountain reflections',
  },
];

// ── Style Definitions ──────────────────────────────────────
const STYLE_PROMPTS = {
  cinematic:    'cinematic film photography, anamorphic lens bokeh, rich color grading, shallow depth of field, dramatic lighting with soft fill, 35mm film grain, professional Hollywood cinematography',
  editorial:    'editorial fashion photography, bold composition, high contrast, magazine-quality lighting, clean and elegant, Vogue-style portrait photography, precise styling',
  'fine-art':   'fine art photography, painterly light, soft romantic atmosphere, impressionistic bokeh, dreamy film aesthetics, gentle pastel tones, classical compositional balance',
  documentary:  'documentary wedding photography, authentic candid moment, photojournalistic style, natural window light, genuine emotion, unposed and natural, reportage photography',
};

// ── Ratio to pixel size ───────────────────────────────────
const RATIO_SIZES = {
  '1:1':  { width: 1024, height: 1024 },
  '4:3':  { width: 1024, height: 768 },
  '16:9': { width: 1280, height: 720 },
  '3:4':  { width: 768,  height: 1024 },
};

// ── State ─────────────────────────────────────────────────
const state = {
  apiKey:        null,
  groomBase64:   null,
  groomMime:     null,
  brideBase64:   null,
  brideMime:     null,
  selectedScene: null,
  customScene:   '',
  ratio:         '1:1',
  style:         'cinematic',
  generating:    false,
  resultDataUrl: null,
};

// ── DOM refs ──────────────────────────────────────────────
const $ = id => document.getElementById(id);

const dom = {
  modalOverlay:    $('modal-overlay'),
  apiKeyInput:     $('api-key-input'),
  toggleKeyBtn:    $('toggle-key-visibility'),
  modalSubmit:     $('modal-submit'),
  modalError:      $('modal-error'),
  app:             $('app'),
  changeKeyBtn:    $('change-key-btn'),
  groomFile:       $('groom-file'),
  groomPreview:    $('groom-preview'),
  groomClear:      $('groom-clear'),
  brideFile:       $('bride-file'),
  bridePreview:    $('bride-preview'),
  brideClear:      $('bride-clear'),
  sceneGrid:       $('scene-grid'),
  customScene:     $('custom-scene'),
  ratioGroup:      $('ratio-group'),
  styleGroup:      $('style-group'),
  generateBtn:     $('generate-btn'),
  generateLabel:   $('generate-label'),
  generateSpinner: $('generate-spinner'),
  generateHint:    $('generate-hint'),
  resultSection:   $('result-section'),
  resultImage:     $('result-image'),
  downloadBtn:     $('download-btn'),
  regenerateBtn:   $('regenerate-btn'),
  errorBanner:     $('error-banner'),
  errorMessage:    $('error-message'),
  errorClose:      $('error-close'),
};

// ── Init ──────────────────────────────────────────────────
function init() {
  // Check sessionStorage
  const savedKey = sessionStorage.getItem('vv_api_key');
  if (savedKey) {
    state.apiKey = savedKey;
    showApp();
  }

  // Build scene cards
  buildScenes();

  // Bind events
  dom.toggleKeyBtn.addEventListener('click', toggleKeyVisibility);
  dom.modalSubmit.addEventListener('click', handleKeySubmit);
  dom.apiKeyInput.addEventListener('keydown', e => { if (e.key === 'Enter') handleKeySubmit(); });
  dom.changeKeyBtn.addEventListener('click', showModal);

  dom.groomFile.addEventListener('change', e => handleFileUpload(e, 'groom'));
  dom.brideFile.addEventListener('change', e => handleFileUpload(e, 'bride'));
  dom.groomClear.addEventListener('click', e => { e.preventDefault(); clearPhoto('groom'); });
  dom.brideClear.addEventListener('click', e => { e.preventDefault(); clearPhoto('bride'); });

  dom.customScene.addEventListener('input', () => {
    state.customScene = dom.customScene.value.trim();
    updateGenerateState();
  });

  bindPillGroup(dom.ratioGroup, 'ratio');
  bindPillGroup(dom.styleGroup, 'style');

  dom.generateBtn.addEventListener('click', handleGenerate);
  dom.downloadBtn.addEventListener('click', handleDownload);
  dom.regenerateBtn.addEventListener('click', handleGenerate);
  dom.errorClose.addEventListener('click', hideError);
}

// ── Modal ─────────────────────────────────────────────────
function showModal() {
  dom.modalOverlay.classList.remove('hidden');
  dom.app.classList.add('hidden');
  dom.apiKeyInput.value = '';
  dom.modalError.textContent = '';
}

function showApp() {
  dom.modalOverlay.classList.add('hidden');
  dom.app.classList.remove('hidden');
}

function toggleKeyVisibility() {
  const input = dom.apiKeyInput;
  const isPassword = input.type === 'password';
  input.type = isPassword ? 'text' : 'password';
  dom.toggleKeyBtn.setAttribute('aria-label', isPassword ? 'Hide key' : 'Show key');
}

function handleKeySubmit() {
  const key = dom.apiKeyInput.value.trim();
  if (!key) {
    dom.modalError.textContent = 'Please enter your Gemini API key.';
    dom.apiKeyInput.focus();
    return;
  }
  if (!key.startsWith('AIza')) {
    dom.modalError.textContent = 'Key should start with "AIza". Please check and try again.';
    dom.apiKeyInput.focus();
    return;
  }
  dom.modalError.textContent = '';
  state.apiKey = key;
  sessionStorage.setItem('vv_api_key', key);
  showApp();
}

// ── Scene Builder ──────────────────────────────────────────
function buildScenes() {
  dom.sceneGrid.innerHTML = '';
  SCENES.forEach(scene => {
    const card = document.createElement('button');
    card.type = 'button';
    card.className = 'scene-card';
    card.dataset.id = scene.id;
    card.setAttribute('role', 'radio');
    card.setAttribute('aria-checked', 'false');
    card.innerHTML = `
      <span class="scene-icon">${scene.icon}</span>
      <span class="scene-name">${scene.name}</span>
    `;
    card.addEventListener('click', () => selectScene(scene.id, card));
    dom.sceneGrid.appendChild(card);
  });
}

function selectScene(id, cardEl) {
  // Deselect all
  dom.sceneGrid.querySelectorAll('.scene-card').forEach(c => {
    c.classList.remove('selected');
    c.setAttribute('aria-checked', 'false');
  });

  if (state.selectedScene === id) {
    // Toggle off
    state.selectedScene = null;
  } else {
    state.selectedScene = id;
    cardEl.classList.add('selected');
    cardEl.setAttribute('aria-checked', 'true');
  }
  updateGenerateState();
}

// ── Photo Upload ───────────────────────────────────────────
async function handleFileUpload(event, role) {
  const file = event.target.files[0];
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    showError('Please upload an image file (JPG, PNG, WebP, etc.)');
    return;
  }

  if (file.size > 10 * 1024 * 1024) {
    showError('Image is too large. Please use an image under 10MB.');
    return;
  }

  try {
    const { base64, mime } = await fileToBase64(file);
    const dataUrl = `data:${mime};base64,${base64}`;

    if (role === 'groom') {
      state.groomBase64 = base64;
      state.groomMime = mime;
      setPreview(dom.groomPreview, dataUrl);
      dom.groomClear.classList.remove('hidden');
    } else {
      state.brideBase64 = base64;
      state.brideMime = mime;
      setPreview(dom.bridePreview, dataUrl);
      dom.brideClear.classList.remove('hidden');
    }
    updateGenerateState();
  } catch (err) {
    showError('Failed to read image. Please try another file.');
    console.error(err);
  }
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const result = reader.result; // data:mime;base64,xxxx
      const [header, base64] = result.split(',');
      const mime = header.replace('data:', '').replace(';base64', '');
      resolve({ base64, mime });
    };
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
}

function setPreview(previewEl, dataUrl) {
  // Remove placeholder, add image
  previewEl.innerHTML = '';
  const img = document.createElement('img');
  img.src = dataUrl;
  img.alt = 'Uploaded photo';
  previewEl.appendChild(img);
}

function clearPhoto(role) {
  if (role === 'groom') {
    state.groomBase64 = null;
    state.groomMime = null;
    dom.groomFile.value = '';
    resetPreview(dom.groomPreview, 'Groom');
    dom.groomClear.classList.add('hidden');
  } else {
    state.brideBase64 = null;
    state.brideMime = null;
    dom.brideFile.value = '';
    resetPreview(dom.bridePreview, 'Bride');
    dom.brideClear.classList.add('hidden');
  }
  updateGenerateState();
}

function resetPreview(previewEl, label) {
  previewEl.innerHTML = `
    <div class="upload-placeholder">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
      <span>${label}</span>
    </div>
  `;
}

// ── Pill Groups ────────────────────────────────────────────
function bindPillGroup(groupEl, stateKey) {
  groupEl.querySelectorAll('.pill').forEach(pill => {
    pill.addEventListener('click', () => {
      groupEl.querySelectorAll('.pill').forEach(p => {
        p.classList.remove('active');
        p.setAttribute('aria-checked', 'false');
      });
      pill.classList.add('active');
      pill.setAttribute('aria-checked', 'true');
      state[stateKey] = pill.dataset.value;
    });
  });
}

// ── Generate State ─────────────────────────────────────────
function updateGenerateState() {
  const hasBoth  = state.groomBase64 && state.brideBase64;
  const hasScene = state.selectedScene || state.customScene.length > 0;

  dom.generateBtn.disabled = !hasBoth;

  if (!hasBoth) {
    dom.generateHint.textContent = 'Upload both portraits to begin.';
  } else if (!hasScene) {
    dom.generateHint.textContent = 'Choose a scene or describe one below.';
  } else {
    dom.generateHint.textContent = 'Ready to create your portrait.';
  }
}

// ── Prompt Builder ─────────────────────────────────────────
function buildPrompt() {
  const sceneText = state.customScene
    ? state.customScene
    : (SCENES.find(s => s.id === state.selectedScene)?.prompt ?? 'in a beautiful romantic setting');

  const styleText = STYLE_PROMPTS[state.style] || STYLE_PROMPTS['cinematic'];
  const { width, height } = RATIO_SIZES[state.ratio] || RATIO_SIZES['1:1'];
  const ratioDesc = `${state.ratio} aspect ratio (${width}×${height}px)`;

  return `Create a stunning luxury wedding portrait photograph of a couple.

PEOPLE:
- The first uploaded image shows the GROOM. Preserve his exact facial features, skin tone, hair color, hair style, and physical appearance with complete fidelity.
- The second uploaded image shows the BRIDE. Preserve her exact facial features, skin tone, hair color, hair style, and physical appearance with complete fidelity.
- Both individuals must appear clearly recognizable as the same people from their respective uploaded photos.
- The couple should appear together in the scene, posed naturally and romantically.

SETTING:
${sceneText}

TECHNICAL STYLE:
${styleText}

FORMAT: ${ratioDesc}, high resolution, ultra-detailed

WEDDING ATTIRE:
- Groom: elegant classic black tuxedo or tailored suit with white dress shirt and silk tie
- Bride: exquisite white bridal gown with delicate lace details, flowing veil or tasteful accessories

MOOD: Romantic, timeless, luxurious, emotionally resonant. The image should feel like a frame from a feature film or a spread in a high-end wedding magazine.

OUTPUT: Single portrait photograph, no text overlays, no borders, no watermarks.`;
}

// ── Gemini API Call ────────────────────────────────────────
async function callGeminiApi() {
  const prompt = buildPrompt();
  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=${state.apiKey}`;

  const requestBody = {
    contents: [
      {
        role: 'user',
        parts: [
          // Groom image first
          {
            inline_data: {
              mime_type: state.groomMime,
              data: state.groomBase64,
            },
          },
          // Bride image second
          {
            inline_data: {
              mime_type: state.brideMime,
              data: state.brideBase64,
            },
          },
          // Text prompt last
          {
            text: prompt,
          },
        ],
      },
    ],
    generationConfig: {
      responseModalities: ['TEXT', 'IMAGE'],
      temperature: 1,
      topP: 0.95,
    },
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(requestBody),
  });

  if (!response.ok) {
    let errMsg = `API error ${response.status}`;
    try {
      const errData = await response.json();
      errMsg = errData?.error?.message || errMsg;
    } catch (_) {}
    throw new Error(errMsg);
  }

  const data = await response.json();
  console.log('Gemini API response:', JSON.stringify(data, null, 2));

  // Extract image from response
  const candidates = data?.candidates;
  if (!candidates || candidates.length === 0) {
    throw new Error('No candidates returned from the API. Please try again.');
  }

  const parts = candidates[0]?.content?.parts;
  if (!parts || parts.length === 0) {
    throw new Error('No content parts in the API response. Please try again.');
  }

  // Find the image part
  const imagePart = parts.find(p => p.inline_data?.mime_type?.startsWith('image/'));
  if (!imagePart) {
    // Check if there's a text error
    const textPart = parts.find(p => p.text);
    if (textPart) {
      throw new Error(`API returned text instead of image: ${textPart.text}`);
    }
    throw new Error('No image data in the API response. Please try again.');
  }

  const { mime_type, data: imageBase64 } = imagePart.inline_data;
  return `data:${mime_type};base64,${imageBase64}`;
}

// ── Generate Handler ───────────────────────────────────────
async function handleGenerate() {
  if (state.generating) return;
  if (!state.groomBase64 || !state.brideBase64) {
    showError('Please upload both groom and bride photos first.');
    return;
  }
  if (!state.apiKey) {
    showModal();
    return;
  }

  // Determine scene
  if (!state.selectedScene && !state.customScene) {
    showError('Please select a background scene or enter a custom description.');
    return;
  }

  state.generating = true;
  hideError();
  setGeneratingUI(true);

  // Show loading state in result section
  dom.resultSection.classList.remove('hidden');
  dom.resultImage.classList.add('hidden');
  dom.resultImage.src = '';

  const resultFrame = dom.resultSection.querySelector('.result-frame');
  resultFrame.classList.add('loading');
  resultFrame.innerHTML = `
    <div class="loading-inner">
      <div class="spinner"></div>
      <p>Crafting your portrait…</p>
    </div>
  `;

  // Scroll to result
  dom.resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });

  try {
    const dataUrl = await callGeminiApi();
    state.resultDataUrl = dataUrl;

    // Restore frame and show image
    resultFrame.classList.remove('loading');
    resultFrame.innerHTML = '';
    resultFrame.appendChild(dom.resultImage);

    dom.resultImage.src = dataUrl;
    dom.resultImage.classList.remove('hidden');
    dom.resultSection.querySelector('.result-actions').style.display = 'flex';

  } catch (err) {
    resultFrame.classList.remove('loading');
    resultFrame.innerHTML = '';
    resultFrame.appendChild(dom.resultImage);
    dom.resultSection.classList.add('hidden');

    let userMsg = err.message || 'An unexpected error occurred.';
    if (userMsg.includes('API_KEY_INVALID') || userMsg.includes('invalid API key')) {
      userMsg = 'Invalid API key. Please check your Gemini API key and try again.';
    } else if (userMsg.includes('QUOTA_EXCEEDED') || userMsg.includes('quota')) {
      userMsg = 'API quota exceeded. Please check your Gemini API quota and try again.';
    } else if (userMsg.includes('SAFETY') || userMsg.includes('safety')) {
      userMsg = 'The request was blocked by safety filters. Please try a different scene description.';
    }
    showError(userMsg);
    console.error('Gemini API error:', err);
  } finally {
    state.generating = false;
    setGeneratingUI(false);
  }
}

function setGeneratingUI(isGenerating) {
  dom.generateBtn.disabled = isGenerating;
  dom.generateLabel.classList.toggle('hidden', isGenerating);
  dom.generateSpinner.classList.toggle('hidden', !isGenerating);
  if (!isGenerating) updateGenerateState();
}

// ── Download ───────────────────────────────────────────────
function handleDownload() {
  if (!state.resultDataUrl) return;

  const link = document.createElement('a');
  link.href = state.resultDataUrl;
  const timestamp = new Date().toISOString().slice(0, 19).replace(/[T:]/g, '-');
  link.download = `vow-vision-portrait-${timestamp}.png`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// ── Error handling ─────────────────────────────────────────
function showError(msg) {
  dom.errorMessage.textContent = msg;
  dom.errorBanner.classList.remove('hidden');
  dom.errorBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
  dom.errorBanner.classList.add('hidden');
  dom.errorMessage.textContent = '';
}

// ── Start ──────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', init);
