import requests

formData = {'login-form:email': 'qamile1@gmail.com', 'login-form:password': 'qamile'}
myheader={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
          'Origin': 'http://newtours.demoaut.com',
'Referer': 'http://newtours.demoaut.com/mercurysignon.php'
'Upgrade-Insecure-Requests: 1'}
resp=requests.post("http://newtours.demoaut.com/login.php",data=formData,header)
print(resp.headers)