document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.title').classList.add('show');
    setTimeout(function() {
        document.querySelector('.title').classList.remove('show');
        document.querySelector('.intro').classList.add('show');
    }, 2000); // 4000 milliseconds = 4 seconds
});

// Function to navigate to home.html
// Function to navigate to the register page



