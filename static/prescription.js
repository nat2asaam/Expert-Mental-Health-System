const prescriptionBtn = document.getElementById('prescription-btn');
const closeBtn = document.getElementById('close-btn');
const popupForm = document.getElementById('prescription-form');

// Show the form when button is clicked
prescriptionBtn.addEventListener('click', () => {
  popupForm.style.display = 'block';
});

// Hide the form when the close button is clicked
closeBtn.addEventListener('click', () => {
  popupForm.style.display = 'none';
});
