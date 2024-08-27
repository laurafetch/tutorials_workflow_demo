from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.

#uses built-in fixture to shortcut to the user model; creates a new user
@pytest.fixture 
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
    username="test_username", password="test_password")
    return "test_username", "test_password"   # this returns a tuple

#client is a built-in dummy web client
def test_login_user(client, test_user):
      test_username, test_password = test_user  # this unpacks the tuple
      login_result = client.login(username=test_username, password=test_password)
      assert login_result == True