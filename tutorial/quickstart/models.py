# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

class Contact(models.Model):
	name = models.CharField(max_length=45)
	phone_number = models.IntegerField(max_length=20)
	
	def __str__(self):
		return self.name
		
class Job(models.Model):
	name = models.CharField(max_length=45)
	job = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name