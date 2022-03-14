import requests
import json
import pprint

r = requests.get('https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple')
print(r.status_code)
print(r.text) # return value as json string
print(type(r.text))
question = json.loads(r.text) # converion to disctonary
print(type(question))
pprint.pprint(question)
print(question['results'][0]['incorrect_answers'])
json_question = json.dumps(question)
print(type(json_question)) # conversion to json