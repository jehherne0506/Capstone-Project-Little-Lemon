from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import generics,viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import BookingSerializer,MenuSerializer,UserSerializer
from .models import Booking,Menu
from .forms import BookingForm

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html',{})

class UserView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BookingItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        guest_count = request.POST['max_guests']
        email = request.POST['email']
        date = request.POST['booking_date']
        form = BookingForm(request.POST)
        if form.is_valid():
            send_mail(
                subject='Booking Confirmation',
                message=f'Thank you for your booking, {name}!\n'
                        f'Guest Count: {guest_count}\n'
                        f'Date: {date}\n'
                        'We look forward to seeing you!\nYours Sincerely, Little Lemon',
                from_email='yeohjehherne@gmail.com',  # replace with your actual email
                recipient_list=[email],
                fail_silently=False,
            )
            form.save()
            return render(request,'success.html')
    form = BookingForm()
    return render(request,'booking.html',{'form':form})