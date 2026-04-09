import requests

def generate_explanation(job_text, prediction):

    label = "Fake Job" if prediction == 1 else "Real Job"

    prompt = f"""
    Analyze the following job posting and explain why it is {label}.
    
    Job Description:
    {job_text}
    
    Give a short and clear explanation.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result['response']