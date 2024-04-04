function toggleMenu(){
    var popupmenu = document.getElementById("popupMenu");
    popupmenu.classList.toggle("hide");

}
function closeMenu(){
    var popupmenu = document.getElementById("popupMenu");
    popupmenu.classList.add("hide");
}

window.addEventListener('resize', function(){
    var width = window.innerWidth;
    var popupmenu = document.getElementById("popupMenu");
        if (width > 600) {
            popupmenu.classList.add("hide");}
  });

  