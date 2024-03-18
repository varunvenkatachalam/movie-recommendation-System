from django.urls import path
from .views import home , recommendation , MR , login_view , profile , action , fantasy , love , comedy , historical , horror , mystery , sci_fi , register


urlpatterns = [
    path('',home,name='home'),
    path('recommendation',recommendation,name='recommendation'),
    path('MR',MR,name='MR'),
    path('login',login_view,name='login'),
    path('profile',profile,name='profile'),
    path('action',action,name='action'),
    path('fantasy',fantasy,name='fantasy'),
    path('love',love,name='love'),
    path('comedy',comedy,name='comedy'),
    path('historical',historical,name='historical'),
    path('horror',horror,name='horror'),
    path('mystery',mystery,name='mystery'),
    path('sci-fi',sci_fi,name='sci-fi'),
    path('register',register,name='register'),
]