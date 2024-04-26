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

document.addEventListener("DOMContentLoaded", function () {
    let squareCalculate = document.getElementById("squareCalculate");
    squareCalculate.onsubmit = function (e) {
        e.preventDefault();
        let positivenumber = document.getElementById("positivenumber").value;
        if (!/^[1-9]\d*$/.test(positivenumber)) {
            alert("Please enter a positive number");
            return;
        }
        let url = "http://127.0.0.1:8000/square/" + positivenumber;
        window.location.href = url
    };
});

