from urllib import response
from django.shortcuts import render
from datetime import date, datetime
from weatherapp.models import AppUser
import random
# package for sending email
from django.core.mail import send_mail

# forms
# from weatherapp.forms import LoginForm, RegistrationForm

# Create your views here.
def landing(request):
    return render(request, 'index.html')

# def user_login(request):    
#     # creating form object
#     lf = LoginForm()
#     template = 'users/login.html'
#     if request.method == "POST":
#         # creating use object
#         user = AppUser.objects.get(email=request.POST.get('email'))
#         if request.POST.get('password') == user.password:
#             # storing user data in session
#             # request.session.setdefault("user_email", user.email)
#             # request.session.update({'user_email': user.email})
#             # method two
#             request.session['user_email'] = user.email

#             if request.session.has_key('user_email'):
#                 template = "users/index.html"
#                 context = {
#                     'page_content_title': 'This is a user dashboard.',
#                     'page_content_body': 'Hello! Welcome to our User Dashboard.',
#                     'user_email': request.session.get('user_email')
#                 }
#                 return render(request, template, context)
#         else:
#             context = {
#                 'form': lf,
#                 'msg_error': 'Invalid email or password'
#             }
#             return render(request, template, context)
#     else:
#         context = {'form': lf}
#         return render(request, template, context)

# def user_logout(request):
#     # destroying session object
#     del request.session['user_email']

#     # using dict function
#     # request.session.clear()
#     # request.session.pop("user_email")
#     template = "users/login.html"
#     lf = LoginForm()
#     context = {
#         'form': lf,
#         'msg_error': "Please login."
#     }
#     return render(request, template, context)

# def user_register(request):
#     template = 'users/create.html'
#     rf = RegistrationForm()
#     if request.method == "POST":
#         # non parameterized constructor
#         user = AppUser()
#         user.email = request.POST['email']
#         user.verification_code = str(random.random())
#         user.password = request.POST['password']
#         user.created_at = datetime.now()
#         # to store data
#         user.save()

        # send_mail(
        #     'Weather App - Verification Code',
        #     'Your email verification code is: ' + user.verification_code,
        #     'c4crypt@gmail.com', # sender email
        #     [user.email], # receiver email
        #     fail_silently=False,
    #     # )
    #     context = {
    #         'form': rf,
    #         'success': 'Registered Successfully'
    #     }
    #     return render(request, template, context)
    # else:
    #     context = {'form': rf}
    #     return render(request, template, context)



# def user_index(request):
#     # render() - this function is use to render pages in django
#     # takes three parameter
#     # 1. request
#     # 2. template
#     # 3. data (which can be null) - must be a dict - context
#     if request.session.has_key('user_email'):
#         context = {
#             'page_content_title': 'This is a user dashboard.',
#             'page_content_body': 'Hello! Welcome to our User Dashboard.',
#             'user_email': request.session['user_email']
#             }
#         template = 'users/index.html'
#         return render(request, template, context)
#     else:
#         template = 'users/login.html'
#         lf = LoginForm()
#         context = {
#                 'form': lf,
#                 'msg_error': 'Please login first.'
#             }
#         return render(request, template, context)
    
    
    
    
    
    
    
    
    
    
    

# custom register
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
################
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
    


        
        
        
@api_view(['POST'])
def cpmlogin(request):    
    # creating form object
    if request.method == "POST":
        response_data = AppUser.objects.get(email=request.data.get('email'))
        serializer = AppUserSerializer(response_data)
        if serializer.data.get('password') == request.data.get('password'):
            # storing user data in session
            request.session['user_email'] = serializer.data.get('email')
            # return Response(request.session['user_email'])
            return Response({
                'Succesfully Logged in',
            })
        return Response({
                'User Name or password incorrect',
            })
    else:
        # return Response(request.POST.get('email'))
            return Response({
                'User Name or password incorrect',
            })



# -----reg-----

@api_view(['GET', 'POST'])
def cpmreg(request, format=None):
    if request.method == 'POST':
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': "HTTP_201_CREATED",
                'message': 'Cmp Registration Info List Created',
                'data': serializer.data
            })
        else:
            return Response({
                'message': 'Email Already Exists',

            })
            
            
@api_view(['GET', 'PUT', 'DELETE'])
def cmpregde(request, id):
    permission_classes = ([IsAuthenticated])
    authentication_classes = [TokenAuthentication]
    try:
        job_r = AppUser.objects.get(pk=id)
    except AppUser.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'User Not Found',   
        })

    if request.method == 'GET':
        serializer = AppUserSerializer(job_r)
        return Response(serializer.data)


