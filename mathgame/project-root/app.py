from flask import Flask, render_template, jsonify, send_from_directory
import os
import random

app = Flask(__name__, static_folder="static")

# List of different object categories
object_categories = {
    "fruits": ["🍎", "🍊", "🍌", "🍇", "🍉"],
    "vegetables": ["🥕", "🌽", "🥦", "🍆", "🥒"],
    "animals": ["🐶", "🐱", "🐭", "🐰", "🐵"],
    "vehicles": ["🚗", "🚕", "🚙", "🚌", "🚎"]
}

# Generate random game data
def generate_game():
    category = random.choice(list(object_categories.keys()))  # Pick a random category
    objects = object_categories[category]
    box_counts = [random.randint(1, 5) for _ in range(5)]  # Random count of objects in each box
    red_box_index = random.randint(0, 4)  # Mark one random box as red
    correct_answer = box_counts[red_box_index]
    correct_object = random.choice(objects)
    
    # Generate numerical options instead of images
    options = [random.randint(1, 5) for _ in range(3)]
    options.append(correct_answer)
    random.shuffle(options)
    
    return {
        "boxes": box_counts,
        "red_index": red_box_index,
        "options": options,
        "object": correct_object,
        "category": category
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_game_data')
def get_game_data():
    return jsonify(generate_game())

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)