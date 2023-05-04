from django.urls import path

from source.apps.users.views import user_view

app_name = 'users'


urlpatterns = [
    # Users
    path('', user_view, name='users-list'),
]
