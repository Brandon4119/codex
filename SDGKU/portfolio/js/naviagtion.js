document.querySelectorAll(".nav-link a").forEach(option => {
    option.addEventListener("click", function (event){
        event.preventDefault();

        const targetID = this.getAttribute("href").substring(1);

        document.getElementById(targetID).scrollIntoView({
            behavior: 'smooth'
        });

    });
});