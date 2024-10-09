from django.urls import path
from condidates import views
app_name='condidates'

urlpatterns = [
    
    path('signup/',views.registration_view,name='singup'),
    path('signin/',views.login_view,name='signin'),
    path('signout/',views.logout_view,name='signout'),
    path('profile_view/',views.profile_view,name='profile'),
    path('my_profile/',views.my_profile,name='my_profile'),
    
    
    path('custom_csrf_failure/',views.custom_csrf_failure),
   
]
