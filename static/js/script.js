const resumeInput = document.getElementById("resumeInput");
const fileName = document.getElementById("fileName");

resumeInput.addEventListener("change", () => {

    if (resumeInput.files.length) {
        fileName.textContent = resumeInput.files[0].name;
    } else {
        fileName.textContent = "No file selected";
    }

});

const form = document.querySelector("form");
const uploadBtn = document.getElementById("uploadBtn");

form.addEventListener("submit", () => {
    uploadBtn.classList.add("loading");
});