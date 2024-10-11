from django.urls import path
from candidates import views
app_name='candidates'

urlpatterns = [
    
    path('signup/',views.registration_view,name='singup'),
    path('signin/',views.login_view,name='signin'),
    path('signout/',views.logout_view,name='signout'),
    # path('profile_view/',views.profile_view,name='profile'),
    path('profile/',views.candidate_profile_view,name='candidate_profile'),
    path('profile/update/',views.update_candidate_profile,name='update_candidate_profile'),
    
    
    
    
    path('custom_csrf_failure/',views.custom_csrf_failure),
   
]
