from flask import Flask, render_template


class Render:
    def render_page(self, categories: dict, games: dict) -> str:
        # Render the jinja2 template in templates/index.jinja2.html.
        return render_template('index.jinja2.html', categories=categories, games=games)
