function toggleMenu(){
    let popupmenu=document.getElementById("popupMenu");
    popupmenu.classList.toggle("hide");
}

function closeMenu(){
    let popupmenu=document.getElementById("popupMenu");
    popupmenu.classList.add("hide");
}

window.addEventListener('resize', function(){
    let width=window.innerWidth;
    let popupmenu=document.getElementById("popupMenu");
        if (width > 600) {
            popupmenu.classList.add("hide");}
});


fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1").then(function(response){
    return response.json();
}).then(function(data){
    let imgList=[];
    let spotList=data.data.results;
    //console.log(spotList)
    let spotList3=spotList.slice(0,13);
    spotList3.forEach(spot => {
        let firstURL=spot.filelist.match(/(https?:\/\/[^?#\s]+?\.(jpg|JPG))/i);
        //console.log(spot.stitle,firstURL[0])
        let spotTitle=spot.stitle;
        let spotImg=firstURL[0];
        imgList.push({name: spotTitle, img: spotImg});
    });
    //console.log(imgList3);
    for(let i=1;i<4;i++){
        const pictureSpan=document.querySelector(`.promotion${i} .p .picture`);
        let newImg=document.createElement("img");  // 建img元素
        newImg.src=imgList[i-1].img;  
        pictureSpan.appendChild(newImg);
        const replaceText = document.querySelector(`.promotion${i} .p`);
        replaceText.lastChild.nodeValue = imgList[i-1].name;
    }
    for(let i=1;i<11;i++){
        const titleDiv=document.querySelector(`.title${i} `);
        titleDiv.style.backgroundImage=`url(${imgList[i+2].img})`;
        const replaceText=document.querySelector(`.title${i} .t`);
        replaceText.lastChild.nodeValue=imgList[i+2].name;
    }    
    });