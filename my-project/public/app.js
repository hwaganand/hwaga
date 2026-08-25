/* =========================================================
   My Project
   ========================================================= */

'use strict';

// -- Elements ---------------------------------------------
const helloBtn = document.getElementById('hello-btn');
const helloOut = document.getElementById('hello-out');

// -- Events -----------------------------------------------
helloBtn.addEventListener('click', () => {
  helloOut.textContent = 'Hello from My Project.';
});
