from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import json

app = Flask(__name__)

# Folder to store the data
DATA_FOLDER = os.path.join(os.getcwd(), 'data')
os.makedirs(DATA_FOLDER, exist_ok=True)

DATA_FILE = os.path.join(DATA_FOLDER, 'mtbs_data.json')

# Home route to serve HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route to save data to JSON
@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
        return jsonify({"message": "Data saved successfully."})
    except Exception as e:
        return jsonify({"message": f"Failed to save: {str(e)}"}), 500

# Route to load data from JSON
@app.route('/load', methods=['GET'])
def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({})
    except Exception as e:
        return jsonify({"message": f"Failed to load: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)