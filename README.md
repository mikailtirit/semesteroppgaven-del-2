# 🎬 ChickFiley Movies

ChickFiley Movies is a modern full-stack movie web application built with **Flask**, **Python**, **MySQL**, and the **TMDB API**.

The platform allows users to create accounts, securely log in, search for movies, save personal favorites, delete saved movies, and receive personalized recommendations based on their own interests.

This project was created to combine multiple important development skills into one complete system, including:

- Backend Development
- Frontend Design
- Authentication Systems
- API Integration
- Database Management
- Dynamic Web Content
- UI / UX Design

The goal was to create a realistic and visually modern movie platform inspired by real streaming services.

---

#  Main Features

##  Authentication System

A complete user authentication system was built from scratch using Flask and MySQL.

### Includes:

- User registration
- Secure login system
- Password hashing using Werkzeug
- Protected routes
- Session management
- Logout functionality

### Why it matters:

This ensures that every user has their own private account and personal movie data.

---

##  Movie Dashboard

The dashboard acts as the main page after login.

### Features:

- Search for any movie instantly
- Browse trending and popular movies
- Real movie posters from TMDB
- Dynamic movie data
- Modern responsive card layout

### How it works:

Movie data is fetched live through the TMDB API and rendered dynamically using Flask templates.

---

##  Favorites System

Users can build their own personal movie collection.

### Includes:

- Add movies to favorites
- Store favorites inside MySQL database
- Delete favorites anytime
- Personalized favorites page

### Why it matters:

Each user gets their own saved movie list connected to their account.

---

##  Recommended Movies

One of the smartest features in the project.

### How it works:

1. The app reads the user's saved favorite movies.
2. It selects one favorite movie.
3. It sends that title to TMDB.
4. TMDB returns similar movies.
5. Recommendations are shown automatically.

### Benefits:

- Personalized content
- Smart user experience
- Real streaming platform feeling

---

##  Modern UI / UX Design

A lot of focus was placed on visual quality and user experience.

### Design Features:

- Glassmorphism effects
- Hover animations
- Smooth transitions
- Responsive layout
- Clean spacing
- Premium card design
- Animated spinning 3D logo
- Modern dark theme

---

#  Technologies Used

## Frontend

- HTML5
- CSS3
- Jinja2 Templates

## Backend

- Python
- Flask

## Database

- MySQL

## API Integration

- TMDB API (The Movie Database)

## Security

- Werkzeug Password Hashing
- Flask Sessions

---

# 📂 Project Structure

```bash
project-folder/
│── app.py
│── forms.py
│
│── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── dashboard.html
│   ├── favorites.html
│   └── recommended.html
│
│── static/
│   ├── style.css
│   └── bilder/
│       ├── hovedlogo.png
│       ├── deletebilde.png
│       └── blue_wallpaper.jpeg
