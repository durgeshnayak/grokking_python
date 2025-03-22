import requests
import datetime

NUTRITIONIX_APP_ID = ""
NUTRITIONIX_API_KEY = ""
NUTRITIONIX_EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ADD_WORKOUT_URL = "https://api.sheety.co/ba68166c9076ef6635473c09d54a2959/myWorkouts/workouts"

request_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

request_parameters = {
    "query": input("What exercises did you do today?: ")
}

response = requests.post(url=NUTRITIONIX_EXERCISE_URL, json=request_parameters, headers=request_headers)
response.raise_for_status()
raw_exercise_data = response.json()
for exercise in raw_exercise_data["exercises"]:
    exercise_request_parameters = {
        "workout": {
            "date": datetime.datetime.today().strftime("%d/%m/%y"),
            "time": datetime.datetime.now().time().strftime("%H:%M:%S"),
            "exercise": f"{exercise['user_input']}".title(),
            "duration": f"{exercise['duration_min']}",
            "calories": f"{exercise['nf_calories']}",
        }
    }
    exercise_response = requests.post(url=SHEETY_ADD_WORKOUT_URL, json=exercise_request_parameters)
    exercise_response.raise_for_status()
    print(exercise_response.status_code)
    print(exercise_response.text)
