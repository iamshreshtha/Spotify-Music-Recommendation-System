from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load dataset
df = pd.read_csv('cleaned_dataset.csv')

# Load model
model = joblib.load("song_recommender.pkl")
scaler = joblib.load("scaler.pkl")

features = [
    'Danceability',
    'Energy',
    'Loudness',
    'Speechiness',
    'Acousticness',
    'Instrumentalness',
    'Liveness',
    'Valence',
    'Tempo'
]

X = df[features]
X_scaled = scaler.transform(X)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/recommend', methods=['POST'])
def recommend():

    song_name = request.form['song']

    try:

        song_index = df[
            df['Track'].str.lower() ==
            song_name.lower()
        ].index[0]

        distances, indices = model.kneighbors(
            [X_scaled[song_index]]
        )

        recommendations = []

        for idx in indices[0][1:]:

            recommendations.append(
                df.iloc[idx]['Track']
            )

        return render_template(
            "index.html",
            recommendations=recommendations,
            selected_song=song_name
        )

    except Exception as e:

        return render_template(
            "index.html",
            recommendations=[
                f"Song Not Found ({str(e)})"
            ]
        )


if __name__ == "__main__":
    app.run(debug=True)