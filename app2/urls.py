from django.urls import path
from . import views 
urlpatterns = [ 
    path('careers',views.home,name='home'),
    path('details/<slug:slug>',views.details,name='details'),
    path('listing/',views.listing,name='listing'),
    path('accounts/register/',views.signup,name='signup'),
    path('login/',views.login_req,name='login'),
    path('logout/',views.logout_req,name='logout')
]
    