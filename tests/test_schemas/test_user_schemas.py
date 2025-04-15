import pytest
from pydantic import ValidationError
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, LoginRequest
from uuid import uuid4


# Fixtures
@pytest.fixture
def user_base_data():
   return {
       "nickname": "john_doe",
       "email": "john.doe@example.com",
       "full_name": "John Doe",
       "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
       "bio": "I am a software engineer with over 5 years of experience.",
   }


@pytest.fixture
def user_create_data():
   return {
       "nickname": "john_doe",
       "email": "john.doe@example.com",
       "password": "StrongPassword123!",
   }


@pytest.fixture
def user_update_data():
   return {
       "email": "updated.email@example.com",
       "first_name": "John",
       "last_name": "Doe",
   }


@pytest.fixture
def user_response_data():
   return {
       "id": str(uuid4()),  # UUID as string
       "nickname": "john_doe",
       "email": "john.doe@example.com",
       "full_name": "John Doe",
       "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
       "bio": "I am a software engineer with over 5 years of experience.",
       "last_login_at": "2024-11-23T12:34:56",
   }


@pytest.fixture
def login_request_data():
   return {
       "email": "john.doe@example.com",
       "password": "StrongPassword123!",
   }


@pytest.fixture
def user_base_data_invalid():
   return {
       "nickname": "john_doe",
       "email": "john.doe.example.com",  # Invalid email
       "full_name": "John Doe",
       "profile_picture_url": "https://example.com/profile_pictures/john_doe.jpg",
       "bio": "I am a software engineer with over 5 years of experience.",
   }


# Tests for UserBase
def test_user_base_valid(user_base_data):
   user = UserBase(**user_base_data)
   assert user.nickname == user_base_data["nickname"]
   assert user.email == user_base_data["email"]


def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**user_base_data_invalid)
    
    assert "value is not a valid email address" in str(exc_info.value)
