""" tests.py """
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY


# Create your tests here.

class LogInTest(TestCase):
	def test_index(self):
		resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)