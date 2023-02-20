import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"
api_key = "lOZTC7g0lDGUtl7VNxv8TTs54jbNBOTP"

def giphy(q: str, num_of_links: int):
    params = parse.urlencode({
        "q": q,
        "api_key": api_key,
        "limit": "5"
    })
    data = json.loads(request.urlopen("".join((url, "?", params))).read())
    
    for i in range(0, num_of_links):
        print(json.dumps(data["data"][i]["url"]))


q = input("Enter a word for search:")

giphy(q, 5)

