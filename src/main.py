from flask import Flask

from genres import Genres
from games import Games
from render import Render

app = Flask(__name__)


@app.route("/")
def main():
    genres = Genres()
    games = Games()
    page = Render()

    return page.render_page(genres.genres, games.games)
