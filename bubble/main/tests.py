from django.test import TestCase
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
import logging

class SettingsFormSubmitTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='JamesG',
            password='password'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio='Old bio',
            location='Old location',
            id_user=("12")
            
        )

    def test_form_submission(self):
        # Get the URL for the settings page
        url = reverse('settings')

        # Set up the form data
        form_data = {
            'bio': 'This is my new bio',
            'location': 'San Francisco',
            # Add more form fields as needed
        }

        # Log in as a user (if needed)
        self.client.login(username='JamesG', password='password')

        # Submit the form
        response = self.client.post(url, data=form_data)

        # Check that the form submitted successfully
        self.assertEqual(response.status_code, 302)

        # Check that the user's profile was updated
        user_model = User.objects.get(username='JamesG')
        user_profile = Profile.objects.get(user=user_model)
        self.assertEqual(user_profile.bio, 'This is my new bio')
        self.assertEqual(user_profile.location, 'San Francisco')