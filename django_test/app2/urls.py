from django.urls import path
from .views import ReviewEmailView

urlpatterns = [
    path('', ReviewEmailView.as_view(), name='reviews')
]
