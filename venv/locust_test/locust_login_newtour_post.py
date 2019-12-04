#http://newtours.demoaut.com/login.php
'''action: process
userName: qamile1@gmail.com
password: qamile
login.x: 16
login.y: 9'''

from locust import HttpLocust, TaskSet,task,between

class UserBehaviour(TaskSet):

    @task
    def login_post(self):
        self.client.post("/login.php",data={"action": "process","userName": "qamile1@gmail.com","password": "qamile"
                                       ,"login.x": "16","login.y": "9"})


class User(HttpLocust):
    task_set=UserBehaviour
    wait_time = between(5, 10)
    host="http://newtours.demoaut.com"
