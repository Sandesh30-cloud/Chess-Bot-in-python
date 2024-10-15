
from flask import Flask, render_template, jsonify
import chess
import pygame as py
from Board import DisplayBoard
from MiniMax import minimax
from Evaluation import Evalualtion


app = Flask(__name__)

MAX, MIN = 100000, -100000
depth = 4

board = chess.Board()
display = DisplayBoard(board)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-game', methods=['POST'])
def run_game():
    setup_game()  # Call the function to set up the game
    return jsonify({"status": "Game started!"})

# Existing game logic goes here...
def setup_game():
    board.reset_board()
    display.main_menu()
    display.update(board)
    run()

# Existing move, makeMoveWhite, makeMoveBlack, and other functions here...

if __name__ == '__main__':
    app.run(debug=True)
