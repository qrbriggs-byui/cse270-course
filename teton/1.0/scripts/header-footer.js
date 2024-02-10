// This sets today's date in the header
const fulldate = new Intl.DateTimeFormat("en-US", { dateStyle: "medium", timeStyle: "short" }).format( new Date() );
document.querySelector(".header-today p").textContent = fulldate;   
