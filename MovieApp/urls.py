
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.welcome,name='welcome'),
    path('login',views.authlogin,name='login'),
    path('register',views.register,name='register'),
    path('movies',views.movieslist,name='movies'),
    path('logout',views.authlogout,name='logout'),
    path('moviedetail/<int:movie_id>/',views.moviedetails,name='moviedetail'),
    path('moviedetail',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact')

]