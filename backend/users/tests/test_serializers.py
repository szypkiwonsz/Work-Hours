import pytest


@pytest.mark.users_serializers
class TestUserCreateSerializer:

    def test_contains_expected_fields(self, user_create_serializer):
        user_create_serializer.is_valid()
        assert set(user_create_serializer.data.keys()) == {'email'}

    def test_email_field_content(self, user_create_serializer):
        user_create_serializer.is_valid()
        assert user_create_serializer.data['email'] == 'test@email.com'
