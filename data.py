import requests

number_of_questions = 3
trivia_url = "https://opentdb.com/api.php"
trivia_params = {
    'amount': number_of_questions,
    'type': 'boolean'
}

trivia_respons = requests.get(url=trivia_url, params=trivia_params)
trivia_respons.raise_for_status()
#print(trivia_respons.json()['results'])
question_data = trivia_respons.json()['results']
