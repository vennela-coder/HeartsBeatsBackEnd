from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



# Replace with your own secret key (keep it secret!)
JWT_SECRET = 'your-secret-key'
JWT_EXP_HOURS = 2

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"msg": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is not None:
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(hours=JWT_EXP_HOURS),
            'iat': datetime.utcnow()
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

        return Response({
            "msg": "Login successful",
            "token": token,
            "login": 1
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "msg": "Invalid credentials",
            "login": 0
        }, status=status.HTTP_401_UNAUTHORIZED)


# views.py



# @api_view(["POST"])
# def register(request):
#     if request.method == 'POST':

#         username = request.POST.get('username')
#     # handle missing username (e.g., return an error response)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return redirect('register')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect('register')

#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists")
#             return redirect('register')

#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         messages.success(request, "Registration successful")
#         return redirect('login')  # or wherever you want

#     return render(request, 'User/register.html')


