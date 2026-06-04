# Eksamen – To-do liste

## Oppsett

- [x] Lage ny branch som heter `eksamen`
- [x] Jobbe kun på eksamen-branchen frem til innlevering
- [ ] Teste at alt fungerer før jeg pusher til GitHub

---

## Favoritter

- [x] Lage en egen favoritt-side
- [x] Koble favoritt-siden til databasen
- [x] Bruke `session['user_id']` for å hente riktige favoritter
- [x] Lage SQL-spørring som henter favorittfilmer for innlogget bruker
- [x] Bruke `dictionary=True`
- [x] Bruke `fetchall()`
- [x] Sende filmene til HTML med Jinja2
- [x] Vise favorittfilmene på nettsiden

---

## Innlogging og sikkerhet

- [x] Hash passord med Werkzeug
- [x] Forklare forskjellen på passord og hash
- [x] Legge til tidsbegrensning på innlogging
- [x] Teste at brukeren blir logget ut etter en viss tid
- [x] Kun la innloggede brukere få tilgang til beskyttede sider
- [ ] Kun la brukere se sine egne favoritter
- [x] Kunne forklare hvordan `%s` beskytter mot SQL Injection

---


## Ting jeg må kunne forklare uten hjelp

### Flask

- [ ] `@app.route()`
- [ ] `render_template()`
- [ ] `redirect()`
- [ ] `request.form`

### Session

- [ ] Hva en session er
- [ ] Hvorfor vi bruker `session['user_id']`
- [ ] Hvordan session holder brukeren innlogget

### Database

- [ ] `connect_db()`
- [ ] `cursor`
- [ ] `cursor.execute()`
- [ ] `%s`
- [ ] SQL Injection
- [ ] `fetchone()`
- [ ] `fetchall()`
- [ ] `dictionary=True`
- [ ] `db.commit()`

### Jinja2

- [ ] Hvordan sende data fra Flask til HTML
- [ ] Hva `movies=movies` betyr
- [ ] Hvordan vise data fra databasen i HTML
- [ ] Hvordan bruke løkker i HTML

---

## Ting jeg må kunne forklare til sensor

- [ ] Hvordan favorittsystemet fungerer
- [ ] Hvordan session fungerer
- [ ] Hvordan data flyter fra database til HTML
- [ ] Hvordan jeg beskytter webapplikasjonen
- [ ] Hvorfor jeg bruker hashing
- [ ] Hvordan `%s` beskytter mot SQL Injection
- [ ] Hva GDPR er
- [ ] Hva cookies er
- [ ] Hva WCAG er
- [ ] Hva UU-tilsynet gjør
- [ ] Forskjellen på `fetchone()` og `fetchall()`
- [ ] Hvorfor jeg bruker `dictionary=True`

---

## Før eksamen

- [ ] Teste registrering
- [ ] Teste innlogging
- [ ] Teste favoritter
- [ ] Teste databasekobling
- [ ] Teste session
- [ ] Teste personvernside
- [ ] Teste tastaturnavigasjon
- [ ] Rydde opp i kode
- [ ] Legge til kommentarer der det er nødvendig
- [ ] Push siste versjon til GitHub