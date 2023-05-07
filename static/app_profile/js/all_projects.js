window.addEventListener('load', function() {
    if (window.innerWidth > 991) {
      let projectToShow = document.getElementsByClassName('project-show')
      for (let i=0; i<projectToShow.length; i++) {
        projectToShow[i].style.display = 'block'
      }
    } else {
      let showButtons = document.getElementsByClassName('show-more-button')
      for (let i = 0; i < showButtons.length; i++) {
        showButtons[i].style.display = 'block'
      }
    }
  });

  var dict = {}

  function showMore(category){
    if (category in dict && !dict[category]) {
      hideProjects(category)
      dict[category] = true;
    } else {
      showProjects(category);
      dict[category] = false;
    };
  };
  
  
  function showProjects(category){
    let projectToShow = document.getElementsByClassName('project-show-' + category)
    if (window.location.href.includes('it')) {
      document.getElementById('show-more-button-' + category).textContent = "Chiudi"
    } else {
      document.getElementById('show-more-button-' + category).textContent = "Hide"
    }
    for (let i=0; i< projectToShow.length; i++){
      projectToShow[i].style.display = 'block'
    }
  }
  
  
  function hideProjects(category){
    let projectToShow = document.getElementsByClassName('project-show-' + category)
    if (window.location.href.includes('it')) {
    document.getElementById('show-more-button-' + category).textContent = "Mostra altro"
  } else {
    document.getElementById('show-more-button-' + category).textContent = "Show more"
  }
    for (let i=0; i< projectToShow.length; i++){
      projectToShow[i].style.display = 'none'
    }
  }