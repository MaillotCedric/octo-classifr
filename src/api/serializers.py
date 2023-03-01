from rest_framework import serializers
from django.contrib.auth.models import User
from app_images.models import *
from django.contrib.auth.hashers import make_password

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
