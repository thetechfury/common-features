from django.urls import path

from login.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]