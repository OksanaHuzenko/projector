import json
from urllib import parse, request

q = input("Enter a word for search:")

def giphy(q, num_of_links):
    url = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
        "q": q,
        "api_key": "lOZTC7g0lDGUtl7VNxv8TTs54jbNBOTP",
        "limit": "5"
    })
    data = json.loads(request.urlopen("".join((url, "?", params))).read())
    num_of_links1 = int(num_of_links)
    
    for i in range(0,num_of_links1):
        print(json.dumps(data["data"][i]["url"]))

giphy(q,5)

