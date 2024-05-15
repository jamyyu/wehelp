function confirmDelete(messageid) {
    const confirmDeletion = confirm("確定要刪除此筆留言嗎?");
    if (!confirmDeletion) {
        return;
    }
    fetch("/deleteMessage", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ messageid: messageid })
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
}


function getMember(){
    const username = document.getElementById("username").value;
    fetch("/api/member?username="+username).then((response)=>{
        return response.json();
    }).then((result)=>{
        const usernameData = document.getElementById("usernameData");
        if(result.data === null){
            usernameData.textContent = "無此會員";
        }else{
            usernameData.textContent = `${result.data.name} (${result.data.username})`;
        }
        document.getElementById("username").value = "";
    })
}


function updateName(){
    const name = document.getElementById("name").value;
    fetch("/api/member",{
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name: name })
    }).then((response)=>{
        return response.json();
    }).then((result)=>{
        const nameData = document.getElementById("nameData");
        if(result.ok){
            document.getElementById("newName").textContent = name;
            nameData.textContent = "更新成功";
        }else{
            nameData.textContent = "更新失敗";
        }
        document.getElementById("name").value = "";
    })
}