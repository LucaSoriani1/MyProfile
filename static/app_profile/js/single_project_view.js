window.addEventListener('load', function() {
    let full = document.getElementsByClassName("big-formula-full")
    let medium = document.getElementsByClassName("big-formula-medium")
    let mobile = document.getElementsByClassName("big-formula-mobile")
    if (window.innerWidth <= 550 && full.length>0 && mobile.length>0){
        for (let i =0; i<full.length; i++){
            full[i].style.display = 'none';
        }
        for (let i=0; i<mobile.length; i++){
            mobile[i].style.display = 'block';
        }
    } else if (window.innerWidth<1200 && full.length>0 && medium.length>0){
        for (let i =0; i<full.length; i++){
            full[i].style.display = 'none';
        }
        for (let i=0; i<medium.length; i++){
            medium[i].style.display = 'block';
        }
    }
  });