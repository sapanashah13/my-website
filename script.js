

//Hamburger menu
function toggleMenu(){
    document.getElementById("nav-menu").classList.toggle("show");
}

//Active Link
function setActive(element) {
    let links = document.querySelectorAll("#nav-menu a");

    links.forEach(link => {
        link.classList.remove("active");
    });

    element.classList.add("active");
}

function validateForm() {


    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    //Check if fields are empty
    if (name=== "" || email === "" || message === "") {
        alert("please fill in the field.");
        return false;
    }

    //Simple email validation
    if(!email.includes('@')) {
        alert("Please enter a valid email.");
        return false;
    }

    alert("Thank you! Your message has been sent.");
    return true;
}

//Section Animation
function revealSections (){
    let sections = document.querySelectorAll("section");

    sections.forEach(section =>  {
        let windowHeight = window.innerHeight;
        let sectionTop = section.getBoundingClientRect().top;

        if (sectionTop < windowHeight - 100) {
            section.classList.add("show");
        }

    });
}
//Single Scroll Listener (FIXED)
window.addEventListener("scroll", function(){

//Run once on page load
revealSections();


//Navbar scroll effect
    let nav = document.querySelector("nav");

    if (window.scrollY > 50) {
        nav.classList.add("scrolled");
    } else {
        nav.classList.remove("scrolled");
    }

//show button on scroll
    let btn = document.getElementById("topBtn");

    if (document.documentElement.scrollTop > 200) {
        btn.style.display = "block";
    }
    else {
        btn.style.display = "none";
    }
});

//Scroll to top function
function scrollToTop(){
    window.scrollTo ({
        top: 0,
        behavior: "smooth"
    });
}


//Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    //Save preference 
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    }
    else{
        localStorage.setItem("theme", "light");
    }
    }

   // Load theme properly

    document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }

    revealSections(); // run once on load
});