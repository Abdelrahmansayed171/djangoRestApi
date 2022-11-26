# There are more than one client
# one from the web browser
# one from python client
import requests

# endpoint in term of API client is really a kind of URL 
endpoint = "https://httpbin.org/status/200/"
# /anything will echo what i send to it 
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/" #"http://127.0.0.1:8000"

get_response = requests.get(endpoint, data={"query" : "Hello world"}) # a API method (akenak fata7t el mawke3 mn el browser bs with code)
# Every request will need a response to it so we will save 
# this request to a variable response 
# requests.get(endpoint, json={"query" : "Hello world"}) will be an json application
# and message will be in data field not (form like data)
print(get_response.text) #print raw text response
print(get_response.status_code)
# Phone -> Camera -> APP -> API -> Camera (it's library API not REST APIs)

# Rest APIs -> Web Api (Rest API work on the internet)


# HTTP Request -> HTML
# REST API HTTP Request -> JSON (Javascript object notation)
# print(get_response.json()) # Format the JSON into it's form 



###TESTING COMMITS####
### nOW I'M TESTING COMMITING ISSUE