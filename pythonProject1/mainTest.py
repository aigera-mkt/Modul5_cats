import requests
import json

base_url ='https://catfact.ninja'
endpoint='/breeds'
query_params={'limit':"3", 'max_length':'5'}
headers={'Content-type':'Application/json'}

response_breed = requests.get(base_url+endpoint)

print(response_breed.status_code)
print(response_breed.text)

response_breed_limit = requests.get(base_url+endpoint, params='query_params')
print(response_breed_limit.status_code)
print(response_breed_limit.text)

endpoint='/facts'
response_facts = requests.get(base_url+endpoint)

print(response_facts.status_code)
print(response_facts.text)


