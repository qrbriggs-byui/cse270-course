// This sets today's date in the header
const fulldate1: string = new Intl.DateTimeFormat("en-US", { year: "numeric", month: 'long', day: 'numeric', weekday: 'long' }).format( new Date() );
const todayheader = document.querySelector(".header-today p");
if (todayheader!=null){
    todayheader.textContent = fulldate1;
}

// This sets the year for the footer
const today1: Date = new Date();
var obj = document.querySelector("#currentyear");
if (obj!=null){
    obj.textContent = today1.getFullYear().toString();
}

// This sets the last modified date on the home page
obj = document.querySelector("#lastmodified");
if (obj!=null){
    obj.textContent = document.lastModified;
}

// Toggle the menu open or closed
function toggleMenu1(){
    obj = document.querySelector("nav ul");
    if (obj!=null){
        obj.classList.toggle("menu-active");
    }
    obj = document.querySelector("#hamburger-x");
    if (obj!=null){
        obj.classList.toggle("menu-active");
    }
    obj = document.querySelector("#hamburger-equiv");
    if (obj!=null){
        obj.classList.toggle("menu-active");
    }
}

// Attach click listener to the hamburger menu
obj = document.querySelector("#hamburger-menu");
if (obj!=null){
    obj.addEventListener('click', toggleMenu1);
}