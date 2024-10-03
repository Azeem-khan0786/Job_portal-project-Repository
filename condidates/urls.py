from django.urls import path
from condidates import views
app_name='condidates'

urlpatterns = [
    path('signup/',views.registration,name='singup'),
    path('signin/',views.Login,name='signin')
    
]
