from django.urls import path
from .views import Signup_View, Login_View, Logout_View
app_name = 'accounts'

urlpatterns= [
    path('signup/', Signup_View,name='signup'),
    path('login/', Login_View,name='login'),
    path('logout/',Logout_View,name='logout'),
]