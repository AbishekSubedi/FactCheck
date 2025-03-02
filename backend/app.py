from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from newspaper import Article
import google.generativeai as genai
import os
from dotenv import load_dotenv
import requests
import json
import re

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')  # Use gemini-2.0-flash

def extract_json(text):
    try:
        json_str = re.search(r'\{.*\}', text, re.DOTALL).group()
        return json.loads(json_str)
    except Exception as e:
        print("JSON extraction error:", e)
        return None

def analyze_with_gemini(prompt_template, text):
    prompt = prompt_template.format(text=text)
    response = model.generate_content(prompt)
    return extract_json(response.text) or {"error": "Analysis failed"}

def get_fact_check(query):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": query,
        "key": os.getenv('FACT_CHECK_API_KEY')
    }
    try:
        response = requests.get(url, params=params)
        claims = response.json().get('claims', [])
        return claims[0]['text'] if claims else None
    except Exception as e:
        print("Fact Check error:", e)
        return None

# Root route
@app.route('/')
def home():
    return """
    <h1>Welcome to the News Verifier API!</h1>
    <p>Use the <code>/analyze</code> endpoint to verify news.</p>
    <p>Send a POST request to <code>/analyze</code> with a JSON body like:</p>
    <pre>
    {
        "input": "Your news text or URL here"
    }
    </pre>
    """

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.json['input']
    content = ""
    
    # Check if input is URL
    if user_input.startswith('http'):
        try:
            article = Article(user_input)
            article.download()
            article.parse()
            content = article.text
        except Exception as e:
            print("Article extraction error:", e)
            return jsonify({"error": "Could not fetch article"}), 400
    else:
        content = user_input

    # Fake News Analysis (with recency context)
    fake_news_prompt = """Analyze this recent news content for fake news indicators. Consider that this article was published today and provide your analysis with the latest context. Return JSON:
{{
    "verdict": "string",
    "confidence": 0-100,
    "reasons": ["list"]
}}
Content: {text}"""
    fake_news = analyze_with_gemini(fake_news_prompt, content)
    
    # AI Detection
    ai_prompt = """Is this text AI-generated? Return JSON:
{{
    "is_ai": boolean,
    "confidence": 0-100,
    "evidence": ["list"]
}}
Text: {text}"""
    ai_generated = analyze_with_gemini(ai_prompt, content)
    
    # Sentiment Analysis
    sentiment_prompt = """Analyze sentiment. Return JSON:
{{
    "sentiment": "positive/neutral/negative",
    "polarity_score": -1 to 1
}}
Text: {text}"""
    sentiment = analyze_with_gemini(sentiment_prompt, content)
    
    # Fact Check using Google Fact Check API (limited by available data)
    fact_check = get_fact_check(content[:500])  # Use first 500 chars as query
    
    return jsonify({
        "fake_news": fake_news,
        "ai_generated": ai_generated,
        "sentiment": sentiment,
        "fact_check": fact_check
    })

if __name__ == '__main__':
    app.run(debug=True)
