from django.contrib.auth.models import User, Group
from models import Company
from models import Contact
from models import Job
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('url', 'name', 'address')

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = Contact
		fields = ('url', 'name', 'phone_number')

class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
		model = Job
		fields = ('url', 'name', 'job')