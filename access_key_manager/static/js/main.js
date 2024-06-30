document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.code-input');
    inputs.forEach((input, index) => {
        input.addEventListener('input', (e) => {
            if (e.target.value.length === 1 && index < inputs.length - 1) {
                inputs[index + 1].focus();
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
  

  