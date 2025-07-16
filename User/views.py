from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'access': response.data.get('access'),
            'refresh': response.data.get('refresh'),
            'message': 'Login successful'
        }, status=status.HTTP_200_OK)


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


