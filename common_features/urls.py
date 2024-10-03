from django.contrib import admin
from django.urls import path, include

from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='account_logout'),
    path('accounts/', include('allauth.urls')),
    path('', include('login.urls')),
]
