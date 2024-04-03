import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def api_client_for_jwt():
    user = User.objects.create_user(email="test@test.com", password="Sduwdsdas&12412")
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="test@test.com", password="Sduwdsdas&12412")
    return user


@pytest.fixture
def login_data():
    data = {
        "email": "test@test.com",
        "password": "Sduwdsdas&12412",
    }
    return data


@pytest.mark.django_db
class TestAccountApi:
    def test_token_login_status_200(self, api_client, login_data, common_user):
        url = reverse("accounts:api-v1:token-login")
        response = api_client.post(url, data=login_data)
        assert response.status_code == 200
        assert len(response.data.keys()) == 3
        assert response.data["email"] == common_user.email
        assert response.data["user_id"] == common_user.id

    def test_token_login_invalid_data_status_400(self, api_client):
        url = reverse("accounts:api-v1:token-login")
        response = api_client.post(
            url,
            data={
                "email": "invalid_email@gmail.com",
                "password": "Sduwdsdas&12412",
            },
        )
        assert response.status_code == 400

    def test_token_logout_status_204(self, api_client, common_user, login_data):
        url = reverse("accounts:api-v1:token-login")
        api_client.post(url, data=login_data)
        user = common_user
        api_client.force_authenticate(user=user)
        url = reverse("accounts:api-v1:token-logout")
        response = api_client.post(url)
        assert response.status_code == 204
        assert user.auth_token is not True

    def test_jwt_create(self, api_client, login_data, common_user):
        url = reverse("accounts:api-v1:jwt-create")
        response = api_client.post(url, data=login_data)

        assert response.status_code == 200
        assert len(response.data.keys()) == 4
        assert response.data["email"] == common_user.email
        assert response.data["user_id"] == common_user.id

    def test_jwt_login_api_client(self, login_data, common_user, api_client):
        user = common_user
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
        url = reverse("accounts:api-v1:jwt-create")
        response = api_client.post(url, login_data)

        assert response.status_code == 200
        assert user.is_authenticated is True
