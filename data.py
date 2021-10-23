import requests


# -----------------------------------------------------------

question_data = []


def get_questions():
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    global question_data
    question_data = data["results"]


get_questions()

