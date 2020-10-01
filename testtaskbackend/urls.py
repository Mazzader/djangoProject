from django.urls import path
from .views import form, InvalidSerialNumber
urlpatterns = [
    path('/', form.as_view()),
    path('error', InvalidSerialNumber.as_view())
]