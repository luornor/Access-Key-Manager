document.addEventListener('DOMContentLoaded', (event) => {
  const inputs = document.querySelectorAll('.code-input');

  console.log(inputs); // Check if inputs are correctly selected

  inputs.forEach((input, index) => {
      input.addEventListener('input', () => {
          console.log('Input event triggered');
          if (input.value.length === 1 && index < inputs.length - 1) {
              console.log('Moving focus to next input');
              inputs[index + 1].focus();
          }
      });

      input.addEventListener('keydown', (e) => {
          console.log('Keydown event triggered');
          if (e.key === 'Backspace' && input.value === '' && index > 0) {
              console.log('Moving focus to previous input');
              inputs[index - 1].focus();
          }
      });
  });
});


// Function to remove messages after 5 seconds
setTimeout(function () {
    var alertMessages = document.querySelectorAll(".alert");
    alertMessages.forEach(function (alert) {
      alert.remove();
    });
  }, 5000);
  

  