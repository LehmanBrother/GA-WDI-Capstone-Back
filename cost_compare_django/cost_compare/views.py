from django.http import JsonResponse
from django.views import View
from .models import Agency, Federal_Account, Consumer_Reference, Agency_Raw, Federal_Account_Raw
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
# from django.shortcuts import render

# Create your views here.
class Agency_Raw(View):
	# toptier agency seed route; will call https://api.usaspending.gov/api/v2/references/toptier_agencies/
	def post(self, request):

		try:
			