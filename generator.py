import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from your .env file
load_dotenv()

# Configure the client for Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_doc(func_name, args, source_code):
    prompt = f"Write professional documentation for '{func_name}' with args {args}. Code: {source_code}"
    
    # This block is inside the function
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    # Return the result
    return response.choices[0].message.content

# --- Everything below this line is OUTSIDE the function (flush to the left) ---

# Define the test case
func_name = "calculate_area"
args = ["radius"]
code = "def calculate_area(radius):\n    return 3.14 * radius * radius"

# Generate and print the result
result = generate_doc(func_name, args, code)
print(result)