from django.urls import path
from .views import index, wrong_view

urlpatterns = [
    path("", index, name="index"),
    path('wrong/', wrong_view, name='wrong'),
]

