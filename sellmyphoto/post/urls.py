from django.urls import path
from . import views
urlpatterns = [
    path('',views.PostFeed.as_view(),name='postfeed'),
   
]