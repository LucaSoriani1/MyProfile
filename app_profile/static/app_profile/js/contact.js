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
    var name = document.getElementById("id_name").value;
    var email = document.getElementById("id_email").value;
    var subject = document.getElementById("id_subject").value;
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
    var name = document.getElementById("id_name").value;
    var email = document.getElementById("id_email").value;
    var subject = document.getElementById("id_subject").value;
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
        .then(function(){
            hideLoader();
            toastTrigger("success");
        })
        .catch(function(error){
          console.warn = () => {};
          hideLoader();
          toastTrigger(error.response.data.status);
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
  
function toastTrigger(status) {
  let toastLiveExample = document.getElementById('liveToast');
  if (status=="invalid"){
    toastLiveExample = document.getElementById('liveToastWarning');
  } else if (status=="error") {
    toastLiveExample = document.getElementById('liveToastError');
  }
  const toast = new bootstrap.Toast(toastLiveExample);
  toast.show();
}

function clearValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
      form.classList.remove('was-validated');
    });
  }