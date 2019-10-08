
#request module is already available as dependency for locust module
import requests

#returns response object
res= requests.get("http://newtours.demoaut.com/mercurycruise.php")
#print("my text"+res.text)
#print(res.status_code)
#print(res.headers)
#print(res.content)
#print(res.cookies)