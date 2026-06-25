import google.generativeai as genai

# Directly set the API key here
API_KEY = "AIzaSyDjMSwO7awO0Tfp4APvdrz3kWzQktzGLWc"

# Replace the dotenv-based API key configuration with the direct API key
print(API_KEY)
genai.configure(api_key=API_KEY)

try:
    models = genai.list_models()
    print("Available models:", list(models))
except Exception as e:
    print(f"Error: {e}")