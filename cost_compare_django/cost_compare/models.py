from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=128)
	agency_id = models.IntegerField(default=0)
	budget_authority_amount = models.FloatField()
	budget_total = models.FloatField()
	budget_pct = models.FloatField()

	def __str__(self):
		return self.name

class Federal_Account(models.Model):
	name = models.CharField(max_length=128)
	account_id = models.IntegerField(default=0)
	amount = models.FloatField()
	parent = models.ForeignKey('Agency', on_delete=models.CASCADE, related_name="federal_accounts")

	def __str__(self):
		return self.name

class Consumer_Reference(models.Model):
	name = models.CharField(max_length=128)
	price = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="consumer_references")

	def __str__(self):
		return self.name

class Agency_Raw(models.Model):
	percentage_of_total_budget_authority = models.FloatField()
	budget_authority_amount = models.FloatField()
	obligated_amount = models.FloatField()
	active_fq = models.IntegerField(default=0)
	active_fy = models.IntegerField(default=0)
	outlay_amount = models.FloatField()
	abbreviation = models.CharField(max_length=32)
	agency_id = models.IntegerField(default=0)
	agency_name = models.CharField(max_length=128)
	current_total_budget_authority_amount = models.FloatField()

	def __str__(self):
		return self.name

class Federal_Account_Raw(models.Model):
	name = models.CharField(max_length=256)
	account_id = models.IntegerField(default=0)
	account_number = models.CharField(max_length=16)
	code = models.IntegerField(default=0)
	amount = models.FloatField()
	category = models.CharField(max_length=32)

	def __str__(self):
		return self.name