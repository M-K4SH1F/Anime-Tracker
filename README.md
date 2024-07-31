# Anime Tracker - Your Top 10 Anime List

## Project Description:
Anime tracker is a Flask-based web application which was built usying PYTHON. This web application allows users to create and maintain a list of their top 10 animes of all time. Users can add new animes, update their ratings and reviews, and delete animes from their list. The application uses Flask, WTForms, SQLite, SQLAlchemy, and more to provide a seamless and interactive experience. Additionally, it integrates with the Jikan API to fetch anime details.

## Features
  - **Home Page:** Displays the top 10 animes with their details including title, year, description, rating, ranking, review, and poster image. Users can update or delete entries from the home page.
  - **ADd Anime:** Allows users to add a new anime to their list by searching for the title using the Jikan API. Users can select the desired anime from the search results and then provide a rating and review.
  - **Edit Anime:** Users can update the rating and review of an anime.
  - **Delete Anime:** Users can delete an anime from their list
  - **Database:** Uses SQLite to store anime details, and SQLAlchemy for ORM.

## Project Structure:
  - `main.py`: Contains the main application logic including routes, database models, and form handling.
  - **Templates:**
      - `base.html`: Base template for the application.
      - `index.html`: Home page template displaying the list of animes.
      - `add.html`: Template for adding a new anime.
      - `edit.html`: Template for editing anime details.
      - `select.html`: Template for selecting an anime from the search results.
  - **Static Files:**
      - `styles.css`: CSS file for styling the application.
  
## Installation and Setup
1. **Clone the Repository:** Clone this repository to your local machine using `git clone`.
2. Go to Project Directory.
3. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
4. **Activate the virtual Environment:**
   - **On Windows:**
     ```bash
     venv\Scripts\activate
    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
6. **Install Dependencies:** Navigate to the project directory and run:
   ```bash
   pip install -r requirements.txt
7. Set Up the Database: Initialize the SQLite database by running:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   flask run
9. **Run the Application:**
   ```bash
   python main.py
10. **Access the Application:**
    - Open your web browser and go to `http://localhost:5000`.
   
## Usage
1.**Home Page:** View the list of top 10 animes. Click "Add Anime" to add a new entry.


https://github.com/M-K4SH1F/Anime-Tracker/assets/159590221/9879ca45-0990-4503-9508-5451d444e5a8


2.**Add Anime:** Enter the title of the anime and click "Add Anime". Select the desired anime from the search results. Provide a rating and review on the next page.


https://github.com/M-K4SH1F/Anime-Tracker/assets/159590221/5749e2e5-e833-4a58-9b56-b815ed63b651


3. **Edit Anime:** Click the "Update" button on an anime card to update its rating and review.


https://github.com/M-K4SH1F/Anime-Tracker/assets/159590221/1b244059-5b56-414a-b040-6c7485132b62


5. **Delete Anime:** Click the "Delete" button on an anime card to remove it from the list.


https://github.com/M-K4SH1F/Anime-Tracker/assets/159590221/7956bff8-6fdf-4214-ab53-d23d53bfbb81


6. **Error Handling:** If the user submits the form without entering an anime title or enters an incorrect value, the application will display an error message prompting the user to enter a valid anime title.


https://github.com/M-K4SH1F/Anime-Tracker/assets/159590221/c1818f21-4608-4a85-8315-bc1106987e5b


## Project Dependencies
 - Flask: Web framework.
 - Flask-Bootstrap: Bootstrap integration for Flask.
 - Flask-WTF: WTForms integration for Flask.
 - Flask-SQLAlchemy: SQLAlchemy integration for Flask.
 - WTForms: Form handling library.
 - Requests: HTTP library for making API requests.

## Deployment

The Anime Tracker project has been successfully deployed:
https://anime-tracker-phi.vercel.app/

This project demonstrates how to build a comprehensive Flask application with CRUD operations, form handling, and external API integration. It is an excellent example for anyone looking to learn Flask or web development in Python.
