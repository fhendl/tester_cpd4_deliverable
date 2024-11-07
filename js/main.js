// Check if the JavaScript file is linked
console.log("JavaScript file is linked!");

// Function to adjust layout based on screen width
function adjustLayout() {
    if (window.innerWidth >= 1440) { // Extra-large screens
        document.body.style.fontSize = "1.8em";
        document.querySelectorAll(".container").forEach((element) => {
            element.style.padding = "2.5rem";
        });
    } else if (window.innerWidth >= 1024) { // Large screens
        document.body.style.fontSize = "1.5em";
        document.querySelectorAll(".container").forEach((element) => {
            element.style.padding = "2rem";
        });
    } else {
        // Small screens (default)
        document.body.style.fontSize = "1em";
        document.querySelectorAll(".container").forEach((element) => {
            element.style.padding = "1rem";
        });
    }
}

// Run adjustLayout after DOM is loaded and on resize
window.addEventListener("DOMContentLoaded", adjustLayout);
window.addEventListener("resize", adjustLayout);

document.querySelectorAll(".card").forEach((card) => {
    // Toggle expansion on click
    card.addEventListener("click", () => {
        card.classList.toggle("expanded");
    });

    // Toggle expansion on Enter or Space key
    card.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault(); // Prevent page from scrolling on Space
            card.classList.toggle("expanded");
        }
    });
});


// Resizable split-screen functionality
const resizer = document.getElementById("resizer");
const sidebar = document.getElementById("sidebar");
const mainContent = document.getElementById("mainContent");

let isResizing = false;

resizer.addEventListener("mousedown", (e) => {
    isResizing = true;
    document.body.style.cursor = "col-resize"; // Change cursor to resizing
});

document.addEventListener("mousemove", (e) => {
    if (!isResizing) return;

    // Calculate new width for the sidebar
    const sidebarWidth = e.clientX;
    sidebar.style.width = `${sidebarWidth}px`;
    mainContent.style.width = `calc(100% - ${sidebarWidth}px)`;
});

document.addEventListener("mouseup", () => {
    isResizing = false;
    document.body.style.cursor = "default"; // Reset cursor
});
