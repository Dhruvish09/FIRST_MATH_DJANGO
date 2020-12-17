from django.urls import path
from app import views

# urlpatterns = [
#     path('',views.math,name='math'),
#     path('expression',views.expression,name='expression'),
# ]

urlpatterns = [
    # path('',views.math,name='math'),
    # path('expresssion',views.expression,name='expression')
    path('',views.home,name='home'),
    path('expression',views.expression,name='expression name'),
    
]