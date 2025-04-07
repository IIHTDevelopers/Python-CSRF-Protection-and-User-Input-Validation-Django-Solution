from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase



class UserRegistrationBoundaryTest(APITestCase):

    def test_boundary_username_contains_admin(self):
        """Test that a username containing 'admin' is not allowed"""
        test_obj = TestUtils()
        try:
            data = {'username': 'admin123', 'email': 'admin@example.com', 'password': 'adminpassword'}
            response = self.client.post(reverse('register'), data=data)
            if response.status_code == 200:
                test_obj.yakshaAssert("TestUsernameContainsAdmin", True, "boundary")
                print("TestUsernameContainsAdmin = Passed")
            else:
                test_obj.yakshaAssert("TestUsernameContainsAdmin", False, "boundary")
                print("TestUsernameContainsAdmin = Failed")
        except:
            test_obj.yakshaAssert("TestUsernameContainsAdmin", False, "boundary")
            print("TestUsernameContainsAdmin = Failed")
