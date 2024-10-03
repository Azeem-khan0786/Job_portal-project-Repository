from django.urls import path
from condidates import views
app_name='condidates'

urlpatterns = [
     path('signin/',views.Login,name='signin'),
    path('signup/',views.registration,name='singup'),
    path('signout/',views.signout,name='signout'),
    path('custom_csrf_failure/',views.custom_csrf_failure)
   
]
