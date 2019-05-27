import sys
import json
import requests

URL = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=1&explaintext=1&titles='
topic = ''

if (len(sys.argv) > 1):
    topic = sys.argv[1]
else:
    print ('Enter a topic to search: ', end='')
    topic = input()
    print ()

response = requests.get(URL + topic)
content = ''

if response.status_code == 200:
    content = response.json()['query']['pages']['8100']['extract']
    print ()
    
print (content)
