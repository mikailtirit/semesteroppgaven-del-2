# IT Asset Management System (ITAM)

## Konsept 
Dette er et system utviklet for IT-avdelinger, skoler eller bedrifter for å holde full kontroll på alt digitalt utstyr. Systemet gjør det enkelt å registrere enheter som PC-er, mobiler, servere og annet IT-utstyr, koble enhetene til brukere, og loggføre reparasjoner, vedlikehold og statusendringer.  

Målet er å gjøre hverdagen enklere for IT-ansvarlige ved å samle all informasjon på ett sted, ha oversikt over hvem som har hvilket utstyr, og sikre at enheter følges opp på riktig måte. Systemet skal være brukervennlig, effektivt og sikkert.

---

## Teknologier brukt

Prosjektet kombinerer flere teknologier for å dekke både frontend, backend og database:  

* **Frontend (HTML/CSS/JavaScript)**  
  - HTML og CSS brukes for å lage en visuelt ryddig og intuitiv nettside.  
  - JavaScript brukes for dynamiske funksjoner som å bytte mellom “Opprett konto” og “Logg inn” på samme side, samt validering av skjemaer før sending.  

* **Backend (Python/Flask)**  
  - Flask håndterer serverlogikk, skjemaer, brukersesjoner og kommunikasjon med databasen.  
  - Python brukes også til å sikre passord med hashing og håndtere logikk for register og login.  

* **Database (MySQL)**  
  - MySQL brukes som relasjonsdatabase for å lagre brukere, IT-assets og relasjoner mellom dem.  
  - Databasen gjør det mulig å hente ut, legge til, oppdatere og slette data på en trygg og strukturert måte.  

---

## Funksjoner i systemet

1. **Brukerregistrering og innlogging**  
   - Brukere kan opprette konto, godta vilkår og logge inn med passord.  
   - Passord lagres sikkert med hashing, og brukernavn valideres mot databasen.  

2. **IT Asset registrering og oversikt**  
   - IT-enheter kan registreres med navn, type og serienummer.  
   - En oversiktsside viser alle registrerte enheter med mulighet for redigering og sletting.  

3. **Dynamisk frontend**  
   - JavaScript brukes til å bytte mellom register- og login-modus uten å laste siden på nytt.  
   - Checkbox for vilkår kan skjules eller vises avhengig av modus.  

4. **Sikkerhet og brukervennlighet**  
   - Sessions håndterer innlogging slik at kun autoriserte brukere får tilgang til enkelte sider.  
   - Feilmeldinger vises når brukernavn eller passord er feil, eller hvis brukernavn allerede finnes ved registrering.  

---

## Kompetansemål

Prosjektet dekker mål i alle tre hovedfag:  

* **Utvikling**: lage frontend (HTML/CSS/JavaScript) og backend (Python/Flask) med en database (**MySQL**)  
* **Design**: lage et ryddig, brukervennlig og visuelt tiltalende grensesnitt  
* **Sikkerhet**: implementere passordhashing, sesjoner og validering for å sikre systemet mot uautorisert tilgang  

Dette prosjektet gir en helhetlig erfaring med å utvikle et komplett webbasert system fra start til slutt, og viser ferdigheter innen både programmering, databaser og webdesign.