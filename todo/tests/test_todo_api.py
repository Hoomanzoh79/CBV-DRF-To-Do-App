import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="test@test.com", password="Aa@1234%")
    return user


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_status_200(self, api_client):
        url = reverse("todo:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_post_task_response_unauthorized_status_401(self, api_client):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "Go to the gym",
            "is_done": False,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_post_task_response_status_201(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "Go to the gym",
            "is_done": False,
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_post_task_invalid_data_response_status_400(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400