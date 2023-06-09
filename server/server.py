from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
#from forms import *
import os


class PlayerAction:
  def __init__(self, id, angle, type, power):
    self.id = ""
    self.angle = 0.0
    self.type = ""
    self.power = 0

class Player:
    def __init__(self, id, points, BombInventory, SquareInventory):
        self.id = ""
        self.points = 0
        self.BombInventory = 0
        self.SquareInventory = 0

class Game:
    def __init__(self, id, player1, player2):
        self.id = ""
        self.player1 = ""
        self.player2 = ""

app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def home():
    p = Player()
    return render_template('game_start.json')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')





# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''