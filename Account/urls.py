from django.urls import path,re_path
from Account import views
from django.views.generic import RedirectView
app_name='Account'

urlpatterns = [
    # path('home/',views.home,name='home'),
    path('signup/',views.registration_view,name='singup'),
    path('signin/',views.login_view,name='signin'),
    path('signout/',views.logout_view,name='signout'),
    # path('profile_view/',views.profile_view,name='profile'),
    path('profile/',views.candidate_profile_view,name='candidate_profile'),
    path('profile/update/',views.update_candidate_profile,name='update_candidate_profile'),
    path('profile/', views.recruiter_profile_view, name='recruiter_profile'),
    path('profile/update/', views.update_recruiter_profile, name='update_recruiter_profile'),
]