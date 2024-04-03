import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User, Profile
from todo.models import Task


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="test@test.com", password="Aa@1234%")
    return user


@pytest.fixture
def profile(common_user):
    profile = Profile.objects.create(
        user=common_user,
        first_name="test firstname",
        last_name="test lastname",
        bio="test bio",
    )
    return profile


@pytest.fixture
def task_example(profile):
    task = Task.objects.create(
        title="test task",
        status=True,
        author=profile,
        is_done=False,
    )

    return task


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_status_200(self, api_client):
        url = reverse("todo:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_post_task_unauthorized_status_401(self, api_client):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "Go to the gym",
            "is_done": False,
            "status": True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_post_task_authorized_status_201(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "Go to the gym",
            "is_done": False,
            "status": True,
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_post_task_invalid_data_status_400(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        invalid_data = {}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, invalid_data)
        assert response.status_code == 400

    def test_delete_task_authorized_status_201(
        self, api_client, common_user, task_example
    ):
        url = reverse("todo:api-v1:task-detail", args=[task_example.id])
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_delete_task_unauthorized_status_401(self, api_client, task_example):
        url = reverse("todo:api-v1:task-detail", args=[task_example.id])
        response = api_client.delete(url)
        assert response.status_code == 401

    def test_put_task_authorized_status_200(
        self, api_client, common_user, task_example
    ):
        url = reverse("todo:api-v1:task-detail", args=[task_example.id])
        user = common_user
        data = {
            "title": "Go to the gym",
            "is_done": False,
            "status": True,
        }
        api_client.force_authenticate(user=user)
        response = api_client.put(url, data)
        assert response.status_code == 200

    def test_put_task_unauthorized_status_401(self, api_client, task_example):
        url = reverse("todo:api-v1:task-detail", args=[task_example.id])
        response = api_client.put(url)
        assert response.status_code == 401

    def test_put_task_invalid_data_status_400(
        self, api_client, common_user, task_example
    ):
        url = reverse("todo:api-v1:task-detail", args=[task_example.id])
        user = common_user
        invalid_data = {}
        api_client.force_authenticate(user=user)
        response = api_client.put(url, invalid_data)
        assert response.status_code == 400
