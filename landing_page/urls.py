from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path('today', today, name="today"),
    path('comments', comments, name="comments"),
    path('add-comment', add_comment, name="add-comment"),
]