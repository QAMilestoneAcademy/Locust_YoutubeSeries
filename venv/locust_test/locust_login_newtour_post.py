#http://newtours.demoaut.com/login.php
'''action: process
userName: qamile1@gmail.com
password: qamile
login.x: 16
login.y: 9'''

from locust import HttpLocust, TaskSet,task

class UserBehaviour(TaskSet):

    @task
    def login_post(self):
        self.client.post("/login.php",{"action": "process","userName": "qamile1@gmail.com","password": "qamile"
                                       ,"login.x": "16","login.y": "9"})


class User(HttpLocust):
    task_set=UserBehaviour
    min_wait=5000
    max_wait = 10000
    host="http://newtours.demoaut.com"
