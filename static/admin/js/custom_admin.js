function openImage(imageUrl) {
    let imageModal = document.createElement("div");
    imageModal.style.position = "fixed";
    imageModal.style.top = "0";
    imageModal.style.left = "0";
    imageModal.style.width = "100%";
    imageModal.style.height = "100%";
    imageModal.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    imageModal.style.display = "flex";
    imageModal.style.justifyContent = "center";
    imageModal.style.alignItems = "center";
    imageModal.style.zIndex = "10000";

    let image = document.createElement("img");
    image.src = imageUrl;
    image.style.maxWidth = "90%";
    image.style.maxHeight = "90%";
    image.style.borderRadius = "8px";
    image.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.5)";

    imageModal.appendChild(image);

    // Close modal on click
    imageModal.onclick = function () {
        document.body.removeChild(imageModal);
    };

    document.body.appendChild(imageModal);
}
