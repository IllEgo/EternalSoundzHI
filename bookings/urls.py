from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import CalendarView, bookevent

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('bookevent.html', TemplateView.as_view(template_name='bookings/bookevent.html'), name='bookevent'),
    path('bookevent/', bookevent, name='bookevent'),
]
