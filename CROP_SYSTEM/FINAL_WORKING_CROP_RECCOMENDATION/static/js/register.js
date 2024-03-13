document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('register-form');
    const container = document.getElementById('container');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
  
      container.classList.add('move-up');
  
      setTimeout(function() {
        form.submit();
      }, 1000); // Adjust delay as needed
    });
  });
  