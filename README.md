 Spotify Music Recommendation System Using Machine Learning

 Overview

This project is a Spotify-inspired Music Recommendation System developed using Machine Learning and Flask.

The system recommends songs similar to a user-selected track based on Spotify audio features such as Danceability, Energy, Loudness, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, and Tempo.

A K-Nearest Neighbors (KNN) model is used to identify songs with similar audio characteristics.

---

 Features

* Song recommendation based on audio features
* Machine Learning using KNN
* Flask web application
* Responsive Spotify-inspired user interface
* Music-themed background
* Fast similarity search
* Easy deployment on localhost

---

 Dataset Features

* Artist
* Track
* Album
* Danceability
* Energy
* Loudness
* Speechiness
* Acousticness
* Instrumentalness
* Liveness
* Valence
* Tempo
* Streams
* Likes
* Views

---

 Technologies Used

 Frontend

* HTML5
* CSS3

 Backend

* Python
* Flask

Machine Learning

* Scikit-Learn
* K-Nearest Neighbors (KNN)
* StandardScaler

Data Processing

* Pandas
* NumPy

---

 Project Structure

Spotify_Recommender/

├── data/

├── models/

├── static/

├── templates/

├── application.py

├── train_model.ipynb

├── requirements.txt

└── README.md

---

 Installation

Clone the repository:

git clone <repository-url>

Move into project directory:

cd Spotify_Recommender

Install dependencies:

pip install -r requirements.txt

---

 Run Application

python application.py

Open browser:

http://127.0.0.1:5000

---

Machine Learning Workflow

1. Load dataset
2. Select Spotify audio features
3. Standardize features using StandardScaler
4. Train KNN recommendation model
5. Save model using Joblib
6. Deploy using Flask
7. Recommend top 5 similar songs

---

 Future Enhancements

* Spotify API Integration
* Artist Recommendations
* Playlist Generation
* Mood-Based Recommendations
* Deep Learning Recommender Systems
* User Authentication

---

 Author

Shreshtha Singh

Master's Student | Bioinformatics | Machine Learning Enthusiast
