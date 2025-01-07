import requests
import os

class QuizAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("QUIZ_API")
        if not self.api_key:
            print("API key not found. Please make sure the environment variable is set.")
        self.url = "https://quizapi.io/api/v1/questions"


    def fetch_questions(self, category):
        params = {
            'apiKey': self.api_key,
            'category': category,
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
