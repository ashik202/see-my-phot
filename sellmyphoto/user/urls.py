from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.RegisterUser.as_view(),name='Register'),
    path('login/',views.CustomTokenObtainPairView.as_view(),name='Login')
]