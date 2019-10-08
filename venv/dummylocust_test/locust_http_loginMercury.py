#This script demonstrates basic example for launching web page using Locust
#http://newtours.demoaut.com/mercurycruise.php

from locust import HttpLocust,TaskSet,task

formData={"action": "process","userName": "qamile1@gmail.com","password": "qamile"}
class UserBehaviour(TaskSet):

      @task
      def launch_url(self):
          res=self.client.post("/login.php",formData)
          print(res.text)


class User(HttpLocust):
    task_set=UserBehaviour
    host="http://newtours.demoaut.com"
