function handleSubmit(event) {
    event.preventDefault();
    if (checkForm()) {
        clearValidation();
      sendPostForm(event);
    } else {
      requiredFieldForm(event);
    }
  }
  
  const form = document.querySelector('form');
  form.addEventListener('submit', handleSubmit);

function checkForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;
  
    if (name === "" || email === "" || subject === "" || message === "") {
      return false;
    }

    var emailRegex = /\S+@\S+\.\S+/;
    if (!emailRegex.test(email)) {
      return false;
    }
  
    return true;
  }

  function sendPostForm(event) {
    event.preventDefault();
    var form = document.getElementById("task-form");
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    showLoader();
    var fd = new FormData();
    fd.append("name", name);
    fd.append("email", email);
    fd.append("subject", subject);
    fd.append("message", message);
    fd.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());          
    form.reset();
    axios.post('/', fd)
        .then(function(resp){
            hideLoader();
            toastTrigger(resp.data);
        })
        .catch(function(err){
            hideLoader();
            toastTrigger(err.data);
        });
};

function showLoader() {
    document.getElementById("submit-button-contact").style.display = "none";
    document.getElementById("loader").style.display = "block";
};

function hideLoader() {
    document.getElementById("submit-button-contact").style.display = "block";
    document.getElementById("loader").style.display = "none";
};

function requiredFieldForm() {
    'use strict';
    const forms = document.querySelectorAll('.needs-validation');
  
    Array.from(forms).forEach(form => {
        form.classList.add('was-validated');
      }, false);
    } 
  
function toastTrigger(data) {
    const toastLiveExample = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastLiveExample);
    toast.show();
};

function clearValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
      form.classList.remove('was-validated');
    });
  }