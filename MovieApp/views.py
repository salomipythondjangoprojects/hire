from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def welcome(request):
    movies = models.movies.objects.all()
    movie_img =[]
    for mov in movies:
        movie_img.append(mov.movie_img.url)
    print(movie_img)
    return render(request,'welcome.html',{'images':movie_img})


def authlogin(request):
    if request.method == 'POST':
        username = request.POST['email']
        print(username)
        password =request.POST['password']
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            mov =models.movies.objects.all()
            return render(request,'movie_list.html',{'movies':mov})
        else:
            print("User return empty")
            messages.error(request,"Credential is Invalid")
            # movies = models.movies.objects.all()
            # movie_img =[]
            # for mov in movies:
            #     movie_img.append(mov.movie_img.url)
            # print(movie_img)
            return redirect('/')
    else:
       
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first = request.POST['first']
        last = request.POST['last']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password != cpassword:
            messages.error(request,'Password Confirmation is Wrong')
            return render(request,'register.html')

        
        ifEmalExists = User.objects.filter(email=email)

        ifUsernameExists = User.objects.filter(username=username)
        if ifEmalExists:
            messages.error(request,"Email already exists")
            return render(request,'register.html')
        
        if ifUsernameExists:
            messages.error(request,"Username already exists")
            return render(request,'register.html')


        user = User.objects.create_user(username=username,email=email,first_name=first,last_name=last)
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_superuser=False
        user.save()

        return redirect('welcome')
    else:
        return render(request,'register.html')

@login_required(login_url='/')
def movieslist(request):
    mov =models.movies.objects.all()
    return render(request,'movie_list.html',{'movies':mov})

def authlogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def moviedetails(request,movie_id):
    if request.method == 'POST':
        pass
    else:
        movie = models.movies.objects.get(id=movie_id)
        return render(request,'Booking.html',{'movie':movie})

def booking(request):
    if request.method =='POST':
        user_name = request.POST['fullname']
        movie_name = request.POST['movie']
        show = request.POST['show']
        count = request.POST['count']
        email =request.POST['email']

        fmovie = models.movies.objects.get(movie_name=movie_name)
        try:
            show = models.show.objects.get(movie=fmovie,Timing=show)
        except:
            messages.error(request,"Show not available")
            return redirect('moviedetail/{}'.format(fmovie.id))
        
        user = User.objects.get(email=email)
        if show.seats >=int(count):
            send_mail(
                    auth_user =settings.EMAIL_HOST_USER,
                    auth_password=settings.EMAIL_HOST_PASSWORD,
                    subject = 'Booking Confirmed',
                    message = 'Thanks for Booking, You have made a reservation for a {movieshow} show of {moviename}'.format(moviename=show.movie.movie_name,movieshow=show.Timing),
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [user.email,],
                    fail_silently = False,
                    
                    )
           
            show.seats = show.seats-int(count)
            show.save()
            messages.success(request,"Booking Successfull !!")
            return redirect('moviedetail/{}'.format(fmovie.id))
        else:
            messages.ERROR(request,"Not enough Seats")
            return render(request,'Booking.html')
    else:
        return redirect('/')

def about(request):
    employee = models.employee.objects.all()
    context ={
        'employee':employee
    }
    return render(request,'about.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg= request.POST['message']
        models.messages(name=name,email=email,message=msg).save()

        send_mail(
                    auth_user =settings.EMAIL_HOST_USER,
                    auth_password=settings.EMAIL_HOST_PASSWORD,
                    subject = 'Message Recieved',
                    message = msg,
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = ['rohan-k.antony@outlook.com',],
                    fail_silently = False,
                    
                    )
        return redirect('contact')
    else:
        return render(request,'contact.html')