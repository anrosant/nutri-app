# coding=utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET", "POST"])
@permission_classes((AllowAny,))
def validate_user(request):
    context = {}
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            user = None
        if user is not None and not user.is_superuser:
            """Función que genera tokens de usuarios"""
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            user = User.objects.get(username=username)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            context["token"] = token
            user.token = token
            context["userId"] = user.id
            context["msj"] = "Ingreso exitoso"

        else:
            context["msj"] = "Usuario o contraseña incorrectos"
    else:
        context["msj"] = "No tiene permisos"
    return Response(context)