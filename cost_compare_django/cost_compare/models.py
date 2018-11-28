from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=128)
	agency_id = models.IntegerField(default=0)
	budget_authority_amount = models.Float()
	budget_total = models.FloatField()
	budget_pct = models.FloatField()

	def __str__(self):
		return self.name

class Federal_Account(models.Model):
	name = models.CharField(max_length=128)
	id = models.IntegerField(default=0)
	amount = models.FloatField()
	parent = models.ForeignKey(Agency, related_name="federal_accounts")

	def __str__(self):
		return self.name

class Consumer_Reference(models.Model):
	name = models.CharField(max_length=128)
	price = models.FloatField()
	user = models.ForeignKey(User, related_name="consumer_references")

	def __str__(self):
		return self.name