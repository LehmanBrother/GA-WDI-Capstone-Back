from django.urls import path
from .views import Agencies_Raw

urlpatterns = [
	path('agencies/', Agencies_Raw.as_view())
]