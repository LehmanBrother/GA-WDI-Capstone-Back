from django.urls import path
from .views import Agencies_Raw, Accounts_Raw, Consumer_References

urlpatterns = [
	path('agencies/', Agencies_Raw.as_view()),
	path('accounts/', Accounts_Raw.as_view()),
	path('crefs/', Consumer_References.as_view())
]