
from django.shortcuts import render
# from ccapp.models import AppUser
from ccapp.models import AppUser
from ccapp.forms import LoginForm, RegistrationForm
from datetime import datetime
from django.core.mail import send_mail
import random


# Create your views here.
def landing(request):
    template = 'index.html'
    context = {
        'page_content_title':'this is homepage',
        'msg_welcome':'welcome to calorie counter'
    }
    return render(request, template, context)

def user_login(request):
    login_form = LoginForm()
    template = 'users/login.html'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = AppUser.objects.get(email = email)
        if password == user.password:
            #storing value to session
            # request.session.setdefault('user_emial', user.email)
            request.session['user_email'] = user.email
            # request.seddion.update({'user_email':user.email})
            # checcking session value 
            # if request.session.get('user_email') == None:
            if request.session.has_key('user_email'):
                template = 'users/index.html'
                context ={
                    'form':login_form,
                    'data': {
                            'email': user.email,
                            'page_content_body': 'welcome to calorie counter:-',
                            'page_content_title': 'This is the user dashboard',
                    }
                }
                return render(request,template,context)
        else:
            context = {
                'form': login_form
            }
            return render(request,template,context)

    else:
        context ={
            'form':login_form
        }
        return render(request,template,context)


def user_register(request):
    register_form = RegistrationForm()
    template = 'users/create.html'
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        major_health_issue = request.POST.get('major_health_issue')

        # creating user object
        # method one non parameterized constructor
        vc = random.random()
        user = AppUser()
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.contact = contact
        user.email = email
        user.gender = gender
        user.dob = dob
        user.blood_group = blood_group
        user.created_at = datetime.now()
        user.password = password
        user.verification_code = vc
        user.address = address
        user.major_health_issue = major_health_issue

        # # method 2 with parameterized constructor
        # user = AppUser(first_name = first_name, middle_name = middle_name,last_name = last_name,\
        #              contact = contact, email = email, gender = gender, dob = dob,\
        #                 password = password, blood_group = blood_group)

        #to store data
        user.save()
        send_mail(
            'calorie counter email verification',
            'your email verification is: 2245'+str(user.verification_code),
            'keshavbbashyal@gmail.com',
            [user.email],
            fail_silently = False,
        )
        context ={
        'form':register_form
        }
        return render(request,template,context)
    else:
        context ={
        'form':register_form
        }
        return render(request,template,context)

def user_logout(request):
    if request.session.has_key('user_email'):
        del request.session['user_email']
        login_form = LoginForm()
        template = "users/login.html"
        context = {
            'form': login_form
        }
        return render(request, template, context)



def user_index(request):
    template = 'users/index.html'
    if request.session.has_key('email'):
        context = {
            'page_content_title': 'This is the user dashboard',
            'page_content_body': 'welcome to calorie counter'   
        }
        return render(request, template, context)
    else:
        login_form = LoginForm()
        template = "users/login.html"
        context = {
            'form': login_form
        }
        return render(request, template, context)
