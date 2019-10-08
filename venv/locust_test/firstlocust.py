from locust import Locust, TaskSet,task

class UserBehaviour(TaskSet):

    @task(1)
    def mytask1(l):
        print("I am logged In")

    @task(2)
    def mytask2(m):
        print("I am logged Out")


class User(Locust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 15000