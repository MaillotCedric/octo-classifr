from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from app_images.models import Categorie, Image
from django.contrib.auth.decorators import login_required
from .serializers import *

@login_required(login_url="/admin")
@api_view(["GET"])
def get_categories(request):
    categorie = Categorie.objects.all()
    serializer = CategorieSerializer(categorie, many=True)

    return Response(serializer.data)

@api_view(["GET"])
def get_images(request):
    # images = Image.objects.all()
    # serializer = ImageSerializer(images, many=True)

    # return Response(serializer.data)

    categorie = request.query_params.get("categorie", None)
    id_cat = 4 if categorie == "pizza" else 1 if categorie == "rose" else None
    where = "WHERE img.id_categorie = '{}'".format(id_cat) if categorie else ""

    requeteSQL = """
        SELECT url, nom_image, id_categorie
            FROM image AS img
            {};
    """.format(where)

    images = Image.objects.raw(requeteSQL)
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)
