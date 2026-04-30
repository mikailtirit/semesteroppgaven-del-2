#  Installation Guide

This guide explains how to correctly install, configure, and run **ChickFiley Movies** on your own computer or server.

Follow each step carefully.

---

##  Requirements

Before starting, make sure you have the following installed:

- Python 3
- pip
- MySQL Server
- Git
- Internet connection

---

## 1. Clone the Project

```bash
git clone https://github.com/mikailtirit/semesteroppgaven-del-2.git
cd semesteroppgaven-del-2



2. Create Virtual Environment

python3 -m venv envsource env/bin/activate




3. Install Dependencies

pip install flask flask-wtf requests mysql-connector-python werkzeug




4. Open MySQL

Use your own MySQL user:

mysql -u YOUR_USERNAME -p

Example:

mysql -u mikail2008 -p




5. Create Database

CREATE DATABASE semesteroppgave_db;
USE semesteroppgave_db;




6. Create Tables
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password TEXT NOT NULL
    );

CREATE TABLE favorites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    movie_title VARCHAR(255) NOT NULL
    );




7. Configure MySQL in app.py
Update database connection:

host="localhost"
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
database="semesteroppgave_db"





8. Add TMDB API Key

Create account:
https://www.themoviedb.org/

Then inside app.py:
API_KEY = "YOUR_API_KEY"





9. Run Website
python app.py

Open locally:
http://127.0.0.1:5000





10. Open on Other Devices

Use:
app.run(host="0.0.0.0", port=5000, debug=True)
Then find IP:

hostname -I
Example:
http://172.20.128.34:5000


Firewall (If Needed)
sudo ufw allow 5000


Finished Setup

You should now be able to:

- Register user
- Login
- Search movies
- Add favorites
- Delete favorites
- Use recommendations



Final Note
ChickFiley Movies is now ready to run locally and continue developing further.
