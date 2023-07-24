from django.shortcuts import render, redirect
# from django.http import JsonResponse
from django.views import View
from .models import Booking, SoundPackage, LightPackage


def bookevent(request):
    sound_packages = SoundPackage.objects.all()
    light_packages = LightPackage.objects.all()
    return render(request, 'bookings/bookevent.html', {'sound_packages': sound_packages, 'light_packages': light_packages})


class CalendarView(View):
    def get(self, request):
        # Retrieve all bookings from the database
        bookings = Booking.objects.all()

        # Pass the bookings to the template
        return render(request, 'calendar.html', {'bookings': bookings})

    def post(self, request):
        # Retrieve the selected date and time from the POST data
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time')

        # Check if the selected date and time are available
        if Booking.objects.filter(event_start=selected_date, event_end=selected_time).exists():
            # Event already booked, show an error message or handle as desired
            error_message = "The selected time slot is already booked. Please choose another."
            return render(request, 'calendar.html', {'error_message': error_message})
        else:
            # Create a new booking with the selected date and time
            booking = Booking(event_start=selected_date, event_end=selected_time)
            booking.save()

            # Redirect to a success page or do something else
            return redirect('success')

def home(request):
    return render(request, 'bookings/home.html')