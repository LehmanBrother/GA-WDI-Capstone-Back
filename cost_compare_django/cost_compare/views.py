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
class Agencies_Raw(View):
	
	#only use csrf_exempt in development
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(Agencies_Raw, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		agency_list = list(Agency_Raw.objects.values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'status': 200,
			'data': agency_list
			}, safe=False)
			