from locust import HttpUser, task
from random import randint


class WebsiteTestUser(HttpUser):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def service(self):
        self.client.post("http://127.0.0.1:8000", json={"request_id": randint(1,10000)})
