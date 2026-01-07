import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Iris Species Predictor</title>
#     <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
# </head>
# <body>

#     <div class="container">
#         <h2>🌸 Iris Classifier</h2>
        
#         <form id="predictForm">
#             <div class="input-group">
#                 <label>Sepal Length (cm)</label>
#                 <input type="number" step="0.1" id="sl" required placeholder="5.1">
#             </div>
#             <div class="input-group">
#                 <label>Sepal Width (cm)</label>
#                 <input type="number" step="0.1" id="sw" required placeholder="3.5">
#             </div>
#             <div class="input-group">
#                 <label>Petal Length (cm)</label>
#                 <input type="number" step="0.1" id="pl" required placeholder="1.4">
#             </div>
#             <div class="input-group">
#                 <label>Petal Width (cm)</label>
#                 <input type="number" step="0.1" id="pw" required placeholder="0.2">
#             </div>

#             <button type="submit">
#                 <span id="btn-text">Predict Species</span>
#                 <div class="loader" id="loader"></div>
#             </button>
#         </form>

#         <div id="result-box">
#             <p id="result-text"></p>
#             <img id="flower-img" src="" alt="Flower Image">
#         </div>
#     </div>

#     <script src="{{ url_for('static', filename='script.js') }}"></script>
# </body>
# </html>

# Load model
try:
    model = pickle.load(open('iris_model.pkl', 'rb'))
except FileNotFoundError:
    print("Error: iris_model.pkl not found.")
    exit()

class_names = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

# เพิ่ม URL ของรูปภาพดอกไม้ (ใช้รูปจาก Wikimedia)
image_urls = {
    'Setosa': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/640px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
    'Versicolor': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/640px-Iris_versicolor_3.jpg',
    'Virginica': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/640px-Iris_virginica.jpg'
}

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        
        prediction_index = model.predict([features])[0]
        prediction_name = class_names[prediction_index]
        
        # ดึง URL รูปภาพตามชื่อดอกไม้
        result_img = image_urls[prediction_name]

        # ส่ง image_url กลับไปหา JavaScript ด้วย
        return jsonify({
            'success': True, 
            'prediction': prediction_name, 
            'image_url': result_img 
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5002)