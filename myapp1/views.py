from django.shortcuts import get_object_or_404,render,redirect
from django.http import JsonResponse, HttpResponse
from .models import Menu
from django.core import serializers
from .models import Booking,Table
from .forms import BookingForm
from datetime import date,datetime
import json
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error_message':"Username already taken"})


        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        authenticated_user=authenticate(request,username=username,password=password)
        if authenticated_user:
            login(request,user)
        return redirect('book')
    return render(request,'register.html')
    

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('book')
        else:
            return render(request,'login.html',{'error_message':"Invalid"})
    return render(request,'login.html')





def table_list_page(request):
    tables=Table.objects.all()
    booked_tables=Booking.objects.values_list('table_id',flat=True)


    for table in tables:
        table.is_reserved=table.id in booked_tables

    return render(request,'table.html',{'tables':tables})








def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

@login_required
def book(request):
    form=BookingForm()
    tables=Table.objects.filter(status='available')
    user_bookings=Booking.objects.filter(user=request.user)
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            table=form.cleaned_data['table']

            if table.status=='reserved':
                return render(request,'book.html',{'form':form,'tables':tables, 'user_bookings':user_bookings,'reserved_error':True})
            
            bookings = form.save(commit=False)

            bookings.table=table
            bookings.user=request.user
            bookings.status='pending'
            bookings.save()

            table.status='reserved'
            table.save()
            
            return redirect('user_bookings',user_id=request.user.id)

    
    return render(request,'book.html',{'form':form,'tables':tables,'user_bookings':user_bookings})


@login_required
def delete_booking(request,booking_id):
    booking=get_object_or_404(Booking,id=booking_id)
    if request.method=='POST':
        table=booking.table
        table.status='available'
        table.save()
        booking.delete()
        return redirect('bookings')
    return render(request,'book_delete.html',{'booking':booking})

def booking_list(request):
    bookings=Booking.objects.all()
    return render(request,'bookings.html',{'bookings':bookings})


def update(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    reserved_error=True
    if request.method=="POST":
        form=BookingForm(request.POST,instance=booking)
        if form.is_valid():
            table=form.cleaned_data['table']
            if table.status=='reserved' and table!=booking.table:
                reserved_error=True
            else:
                form.save()
                return redirect('bookings')
    else:
        form=BookingForm(instance=booking)
    return render(request,'book_update.html',{'form':form,'reserved_error':reserved_error})


def user_bookings(request,user_id):
    bookings=Booking.objects.filter(user_id=user_id)
    return render(request,'user_booking.html',{"bookings":bookings})



def menu(request):
    menu_data=Menu.objects.all()
    context={'menu':menu_data}
    return render(request,'menu.html',context)

def display_menu_item(request,pk=None):
    if pk:
        menu_items=Menu.objects.get(pk=pk)
    else:
        menu_items=''
    return render(request,'menu_items.html',{'menu_items':menu_items})






