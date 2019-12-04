from locust import Locust, TaskSet,task,bewteen

class UserBehaviour(TaskSet):

    @task(1)
    def mytask1(l):
        print("I am logged In")

    @task(2)
    def mytask2(m):
        print("I am logged Out")


class User(Locust):
    task_set = UserBehaviour
    wait_time = between(5, 10)