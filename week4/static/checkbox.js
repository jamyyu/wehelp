document.addEventListener("DOMContentLoaded", function () {
    let signinForm = document.getElementById("signinForm");
    signinForm.onsubmit = function (e) {
        let agreeCheckbox = document.getElementById("agree");
        if (!agreeCheckbox.checked) {
            alert("Please check the checkbox first");
            e.preventDefault();
        }
    };
});