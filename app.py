from flask import Flask, render_template, request
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.utils.genai_explainer import generate_explanation

app = Flask(__name__)

pipeline = PredictionPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    text = request.form["job_text"]

    prediction, prob = pipeline.predict(text)

    explanation = generate_explanation(text, prediction)

    result = "Fake Job ❌" if prediction == 1 else "Real Job ✅"

    return render_template(
        "result.html",
        result=result,
        probability=round(prob * 100, 2),
        explanation=explanation
    )

if __name__ == "__main__":
    app.run(debug=True)