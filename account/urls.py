from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.userregister, name="register"),
    path('login/', views.userlogin, name="login"),
    path('logout/', views.userlogout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('subscription/', views.subscription,
         name='subscription'),
    path('subscription/payment/', views.go_to_gateway_view, name='payment'),
    path('subscription/callback/',
         views.callback_gateway_view, name='payment-callback'),
]
