# ChickFiley Films

ChickFiley Films er en webapplikasjon utviklet med Flask, MySQL og TMDB API. Applikasjonen lar brukere opprette konto, logge inn, utforske populære filmer, søke etter spesifikke filmer og lagre favoritter i sin personlige filmliste.

Prosjektet kombinerer webutvikling, databaser, API-integrasjon og sikker brukerautentisering for å skape en enkel og brukervennlig plattform for filmutforskning.

## Hovedfunksjoner

* Registrering av brukere
* Sikker innlogging med hashede passord
* Session-basert autentisering
* Utforsking av populære filmer fra TMDB
* Filmsøk gjennom TMDB API
* Personlig favorittliste
* MySQL-database for lagring av brukere og favoritter

## Teknologier

* Python
* Flask
* MySQL
* HTML
* CSS
* Jinja2
* TMDB API
* Werkzeug Security

## Sikkerhet

Passord lagres ikke som vanlig tekst. Ved registrering hashes passordene med Werkzeug Security før de lagres i databasen. Ved innlogging verifiseres passordet mot den lagrede hashen.

Applikasjonen benytter også parameteriserte SQL-spørringer for å redusere risikoen for SQL Injection og Flask Sessions for sikker autentisering av brukere.

## Utvikler

Utviklet av Mikail Tirit som en del av et skoleprosjekt innen IT og medieproduksjon.
