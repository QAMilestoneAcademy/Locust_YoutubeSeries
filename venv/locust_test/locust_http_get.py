from locust import HttpLocust, TaskSet,task,between

#http://newtours.demoaut.com"

class UserBehaviour(TaskSet):
    @task
    def launch_Url(self):
        self.client.get("/")


class User(HttpLocust):
    task_set=UserBehaviour
    wait_time = between(5, 10)


