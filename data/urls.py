from django.urls import path
from .views import TransationView

urlpatterns = [
    path("transation", TransationView.as_view())
]