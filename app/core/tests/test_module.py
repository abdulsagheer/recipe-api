from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_user_with_email_successfull(self):
        """Test creating a new user with email"""
        email="test@webdev.com"
        password='Testpassword29'
        user=get_user_model().objects.create_user(
            email=email,password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password)) #helper function check whether password is true or not
    
    def test_new_user_normalize(self):
        """Test the email for the new user"""
        email='test@SAGHEER.COM'
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())#User.email is equal to email.lower here 

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user=get_user_model().objects.create_superuser(
            'test@gmail.com','test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
