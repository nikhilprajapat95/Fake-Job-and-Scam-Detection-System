import requests

def generate_explanation(text, prediction):

    label = "Fake Job" if prediction == 1 else "Real Job"

    prompt = f"""
    Analyze the job posting and explain why it is {label}.
    
    Job Description:
    {text}
    
    Give a short explanation.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]