from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

fruits = ['apple','mango','grapes','banana','kiwi']
grid_size = 8 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/grid')
def get_grid():
    grid = [
        [random.choice(fruits) for _ in range(grid_size)]
        for _ in range(grid_size)
    ]
    return jsonify(grid)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

