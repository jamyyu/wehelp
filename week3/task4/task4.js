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
    spotList.forEach(spot => {
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
    clickTimes=0;
    let count=spotList.length-12;
    const btn=document.querySelector('.btn')
    btn.addEventListener('click', function(){
        const box=document.querySelector(".box");
        const newwrapper2=document.createElement("div");
        newwrapper2.className="wrapper2";
        // 用迴圈一次建10個title標籤]
        if(count>10){
            for (let i = 1; i<11; i++) {
                const titleDiv = document.createElement("div");
                titleDiv.className = `title${i}`;
                titleDiv.style.backgroundImage=`url(${imgList[12+i+clickTimes*10].img})`;

                const span = document.createElement("span");
                span.className = "star";
                titleDiv.appendChild(span);

                const div = document.createElement("div");
                div.className = "t";
                div.textContent = imgList[12+i+clickTimes*10].name;
                titleDiv.appendChild(div);

                newwrapper2.appendChild(titleDiv);
            }
        }else{
            for (let i = 1; i<count; i++) {
                const titleDiv = document.createElement("div");
                titleDiv.className = `title${i}`;
                titleDiv.style.backgroundImage=`url(${imgList[12+i+clickTimes*10].img})`;

                const span = document.createElement("span");
                span.className = "star";
                titleDiv.appendChild(span);

                const div = document.createElement("div");
                div.className = "t";
                div.textContent = imgList[12+i+clickTimes*10].name;
                titleDiv.appendChild(div);

                newwrapper2.appendChild(titleDiv);
            }
            btn.style.display="none";   
        }
        // 將包裝容器添加到body或其他元素
        box.appendChild(newwrapper2);
        clickTimes++;
        count-=10;
    });
    });






