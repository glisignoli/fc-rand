from flask import Flask, render_template


class Render:
    def render_page(self, categories: dict, games: dict) -> str:
        categories_left = {}
        categories_right = {}

        # Split categories dict into two equal dicts
        for category in categories.keys():
            if len(categories[category]) % 2 == 0:
                categories_left[category] = categories[category]
            else:
                categories_right[category] = categories[category]

        # Render the jinja2 template in templates/index.jinja2.html.
        return render_template('index.jinja2.html', categories=categories, categories_left=categories_left, categories_right=categories_right, games=games)
