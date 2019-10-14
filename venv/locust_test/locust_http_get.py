from locust import HttpLocust, TaskSet,task

#http://newtours.demoaut.com"

class UserBehaviour(TaskSet):
    @task
    def launch_Url(self):
        self.client.get("/")


class User(HttpLocust):
    task_set=UserBehaviour
    min_wait = 5000
    max_wait = 15000


