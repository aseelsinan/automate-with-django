document.addEventListener("DOMContentLoaded", function() {
    let messageContainer = document.getElementById("messages");
    
    if (messageContainer) {
        setTimeout(function() {
            messageContainer.style.display = "none";
            messageContainer.remove();
        }, 5000);
    }
});