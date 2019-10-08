#This script demonstrates basic example for launching web page using Locust
#http://newtours.demoaut.com/mercurycruise.php

from locust import HttpLocust,TaskSet,task

class UserBehaviour(TaskSet):

      @task
      def launch_url(self):
          self.client.get("/mercurycruise.php")


class User(HttpLocust):
    task_set=UserBehaviour
    host="http://newtours.demoaut.com"
