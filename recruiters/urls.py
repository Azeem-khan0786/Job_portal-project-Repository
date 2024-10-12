from django.urls import path
from recruiters import views

app_name = 'recruiters'

urlpatterns = [
    
    path('profile/', views.recruiter_profile_view, name='recruiter_profile'),
    path('profile/update/', views.update_recruiter_profile, name='update_recruiter_profile'),
    path('jobs/', views.job_view, name='job_view'),
    
    
    
    
]