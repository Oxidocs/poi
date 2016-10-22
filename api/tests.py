from django.test import TestCase

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class DarToken():
	token = Token.objects.create(user=User.objects.get(id=1))
	print token.key
