from faker import Faker
from locust import HttpUser, task

fake = Faker()
from helpers import call as posts


class TestClass(HttpUser):

    @task
    def test_get_all_posts(self):
        result = posts.get_todos(self.client)
        assert result.status_code == 200

    @task
    def test_todos_1(self):
        result = posts.get_1st_todo(self.client)
        assert result.status_code == 200
