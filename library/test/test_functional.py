from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import BlogPost
from rest_framework.test import APITestCase
from django.test import TestCase
from django.http import HttpResponse



class UserRegistrationFunctionalTest(APITestCase):

    def test_registration_valid_data(self):
        """Test if a user can register successfully with valid data"""
        test_obj = TestUtils()
        try:
            data = {'username': 'john_doe', 'email': 'john@example.com', 'password': 'strongpassword123'}
            response = self.client.post(reverse('register'), data=data)
            if response.status_code == 200 and "Registration successful" in response.content.decode():
                test_obj.yakshaAssert("TestRegistrationValidData", True, "functional")
                print("TestRegistrationValidData = Passed")
            else:
                test_obj.yakshaAssert("TestRegistrationValidData", False, "functional")
                print("TestRegistrationValidData = Failed")
        except:
            test_obj.yakshaAssert("TestRegistrationValidData", False, "functional")
            print("TestRegistrationValidData = Failed")