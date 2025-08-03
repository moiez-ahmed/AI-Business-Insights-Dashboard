# insights_engine.py

import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

def generate_insights(df: pd.DataFrame) -> str:
    # Get the API key securely
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "❌ Error: GROQ_API_KEY not set. Check your .env file or environment variables."

    # Initialize Groq client
    client = Groq(api_key=api_key)

    # Prepare the prompt using the first 20 rows of the DataFrame
    prompt = f"""
You are a professional data analyst. The user uploaded the following dataset:

{df}

Please provide: (Stylyze everthing, use numbers where needed)
1. Summary of key trends
2. Any anomalies or issues
3. Actionable business recommendations
4. Assumptions made
"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful business analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error generating insights: {str(e)}"