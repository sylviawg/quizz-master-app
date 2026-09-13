import requests


def get_question_data():
    """Retrieve a new set of True/False questions from the Open Trivia Database API."""

    parameters = {
        "amount": 10,
        "type": "boolean"
    }

    response = requests.get(
        url="https://opentdb.com/api.php",
        params=parameters
    )
    response.raise_for_status()

    return response.json()["results"]
