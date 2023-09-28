document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#postForm");

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (validateForm()) {
      console.log("Form submitted successfully!");
    }
  });

  function validateForm() {
    let valid = true;

    const title = document.querySelector("#title");
    const content = document.querySelector("#content");
    const image = document.querySelector("#image");

    if (!title.value.trim()) {
      valid = false;
      alert("Title is required");
    }

    if (!content.value.trim()) {
      valid = false;
      alert("Content is required");
    }

    // Image validation
    const allowedExtensions = ["jpg", "jpeg", "png", "gif"];
    if (image.files.length === 0) {
      valid = false;
      alert("Image is required");
    } else {
      const fileName = image.files[0].name;
      const fileExtension = fileName.split(".").pop().toLowerCase();
      if (!allowedExtensions.includes(fileExtension)) {
        valid = false;
        alert(
          "Invalid image file format. Please upload a JPG, JPEG, PNG, or GIF file."
        );
      }
    }

    return valid;
  }
});

document.addEventListener("DOMContentLoaded", () => {
  function updateTime() {
    const currentTimeElement = document.getElementById("current-time");
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, "0");
    const minutes = now.getMinutes().toString().padStart(2, "0");
    const seconds = now.getSeconds().toString().padStart(2, "0");
    const currentTimeString = `${hours}:${minutes}:${seconds}`;
    currentTimeElement.textContent = currentTimeString;
  }

  updateTime();
  setInterval(updateTime, 1000);
});
