from django.urls import path
from recruiters import views

app_name = 'recruiters'

urlpatterns = [
    
    path('profile/', views.recruiter_profile_view, name='recruiter_profile'),
    
]