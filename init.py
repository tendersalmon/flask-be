import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, make_response
from admin.admin import admin


app = Flask(__name__)
app.config.from_object(__name__)


app.register_blueprint(admin, url_prefix='/admin')


if __name__ == "__main__":
    app.run(debug=True)