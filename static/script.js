function byttModus() {
    const tittel = document.getElementById("tittel");
    const skjema = document.getElementById("skjema");
    const hovedBtn = document.getElementById("hoved-btn");
    const byttBtn = document.getElementById("bytt-btn");
    const vilkarWrapper = document.getElementById("vilkar-wrapper");

    if (tittel.innerText === "Opprett konto") {
        tittel.innerText = "Logg inn";
        hovedBtn.innerText = "Logg inn";
        byttBtn.innerText = "Opprett konto";
        skjema.action = "/login";
        vilkarWrapper.style.display = "none";
    } else {
        tittel.innerText = "Opprett konto";
        hovedBtn.innerText = "Opprett konto";
        byttBtn.innerText = "Logg inn";
        skjema.action = "/register";
        vilkarWrapper.style.display = "block";
    }
}