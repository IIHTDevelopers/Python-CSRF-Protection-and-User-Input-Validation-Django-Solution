from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase



class UserRegistrationExceptionalTest(APITestCase):

    def test_invalid_email(self):
        """Test if a user cannot register with an email from 'spam.com'"""
        test_obj = TestUtils()
        try:
            data = {'username': 'jane_doe', 'email': 'jane@spam.com', 'password': 'password123'}
            response = self.client.post(reverse('register'), data=data)
            if response.status_code == 200:
                test_obj.yakshaAssert("TestInvalidEmailDomain", True, "exceptional")
                print("TestInvalidEmailDomain = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidEmailDomain", False, "exceptional")
                print("TestInvalidEmailDomain = Failed")
        except:
            print("h")
            test_obj.yakshaAssert("TestInvalidEmailDomain", False, "exceptional")
            print("TestInvalidEmailDomain = Failed")
