#from flask import Flask

#app = Flask(__name__)


#@app.route('/')
#def hello_world():  # put application's code here
  #  return 'Hello World!'


#if __name__ == '__main__':
 #   app.run()
import pandas as pd
from flask import Flask, request, render_template
import pickle

model = pickle.load(open("model.pkl", "rb"))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    water = float(request.form['water'])
    season = request.form['season']

    input_df = pd.DataFrame([{
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'water availability': water,
        'season': season
    }])

    prediction = model.predict(input_df)

    return render_template(
        "index.html",
        prediction_text=f"The Predicted Crop is {prediction[0]}"
    )

if __name__ == "__main__":
    app.run(debug=True)
