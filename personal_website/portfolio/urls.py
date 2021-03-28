from django.urls import path
from .views import home_view, HomeView

urlpatterns = [
    # path('', home_view, name='home'),
    path('', HomeView.as_view(), name='portfolio'),
]
