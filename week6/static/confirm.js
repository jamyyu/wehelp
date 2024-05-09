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