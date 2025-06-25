from django.urls import path
from .views import SpecialityListCreateView

urlpatterns = [
    path('', SpecialityListCreateView.as_view(), name='speciality-list-create'),
]
