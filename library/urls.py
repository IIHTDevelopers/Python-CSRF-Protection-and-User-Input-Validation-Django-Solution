from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the registration view
    path('register/', views.register, name='register'),  # This view will handle registration form
    path('', views.home, name='home'),  # Assuming a home view as the default page
]
