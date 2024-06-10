# main.py

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

ANIME_DB_API_KEY = "https://api.jikan.moe/v4"
ANIME_DB_SEARCH_URL = "https://api.jikan.moe/v4/anime"  # Jikan API for Anime
ANIME_DB_INFO_URL = "https://api.jikan.moe/v4/anime"
ANIME_DB_IMAGE_URL = "https://cdn.myanimelist.net/images/anime"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Anime(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class FindAnimeForm(FlaskForm):
    title = StringField("Anime Title", validators=[DataRequired()])
    submit = SubmitField("Add Anime")

class RateAnimeForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

@app.route("/")
def home():
    result = db.session.execute(db.select(Anime).order_by(Anime.rating))
    all_animes = result.scalars().all()

    for i in range(len(all_animes)):
        all_animes[i].ranking = len(all_animes) - i
    db.session.commit()

    return render_template("index.html", animes=all_animes)

@app.route("/add", methods=["GET", "POST"])
def add_anime():
    form = FindAnimeForm()
    if form.validate_on_submit():
        anime_title = form.title.data
        response = requests.get(ANIME_DB_SEARCH_URL, params={
                                "q": anime_title})
        data = response.json()["data"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/find")
def find_anime():
    anime_api_id = request.args.get("id")
    if anime_api_id:
        anime_api_url = f"{ANIME_DB_INFO_URL}/{anime_api_id}"
        response = requests.get(anime_api_url)
        data = response.json()["data"]
        new_anime = Anime(
            title=data["title"],
            year=data["aired"]["prop"]["from"]["year"],
            img_url=data["images"]["jpg"]["image_url"],
            description=data["synopsis"]
        )
        db.session.add(new_anime)
        db.session.commit()
        return redirect(url_for("rate_anime", id=new_anime.id))

@app.route("/edit", methods=["GET", "POST"])
def rate_anime():
    form = RateAnimeForm()
    anime_id = request.args.get("id")
    anime = db.get_or_404(Anime, anime_id)
    if form.validate_on_submit():
        anime.rating = float(form.rating.data)
        anime.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", anime=anime, form=form)

@app.route("/delete")
def delete_anime():
    anime_id = request.args.get("id")
    anime = db.get_or_404(Anime, anime_id)
    db.session.delete(anime)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
