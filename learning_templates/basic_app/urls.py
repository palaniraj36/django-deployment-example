from django.conf.urls import url
from basic_app import views
from django.urls import path

#templatetagging

app_name="basic_app"

urlpatterns = [
    path('register/', views.register, name='other'),
    path('user_login/',views.user_login, name='user_login')
    # path('relative/', views.relative, name='relative'),
]
