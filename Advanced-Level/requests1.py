#import json
#print(json.__file__) # where json module is installed. 

import requests
import json 

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

#print(result)
print(result[0])
print(result[0]["title"])
print(type(result))
print("#########")
for i in result:
    #print(i)
    print(i["title"])




