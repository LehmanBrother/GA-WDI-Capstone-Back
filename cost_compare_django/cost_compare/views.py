from django.http import JsonResponse
from django.views import View
from .models import Agency, Federal_Account, Consumer_Reference, Agency_Raw, Federal_Account_Raw
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json

# Create your views here.
class Agencies_Raw(View):
	
	def dispatch(self, request, *args, **kwargs):
		return super(Agencies_Raw, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		agency_list = list(Agency_Raw.objects.values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'status': 200,
			'data': agency_list
			}, safe=False)

class Accounts_Raw(View):

	def dispatch(self, request, *args, **kwargs):
		return super(Accounts_Raw, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		account_list = list(Federal_Account_Raw.objects.values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'status': 200,
			'data': account_list
			}, safe=False)

class Consumer_References(View):

	def dispatch(self, request, *args, **kwargs):
		return super(Consumer_References, self).dispatch(request, *args, **kwargs)

	def get(self, request):
		cref_list = list(Consumer_Reference.objects.values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'status': 200,
			'data': cref_list
			}, safe=False)

	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		print(request.user.is_authenticated)
		if(request.user.is_authenticated):
			try:
				new_cref = Consumer_Reference(name=data["name"], price=data["price"])
				new_cref.user = request.user
				new_cref.save()
				data["id"] = new_cref.id
				print(data, '<--data', request.user)
				return JsonResponse({"data": data}, safe=False)
			except:
				return JsonResponse({"error": "Data not valid"}, safe=False)
		else:
			return JsonResponse({
				'Content-Type': 'application/json',
				'status': 200,
				'message': 'Must be logged in to add data'
				}, safe=False)