import pytest
from django.core.management import call_command


@pytest.mark.django_db
def test_system_check():
    call_command("check")


@pytest.mark.django_db
def test_swagger_docs(api_client):
    response = api_client.get("/docs/")
    assert response.status_code == 200
