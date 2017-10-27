from django.shortcuts import render, redirect
from django.contrib import messages
from models import Trip
from ..login_app.models import User


def index(request):
        if 'first_name' not in request.session:
                redirect('/')
        context = {
                "trips" : Trip.objects.all(),
                "user" : User.objects.get(id = request.session['id'])

        }
        # users = User.objects.all()
        # users.delete()
        # trips = Trip.objects.all()
        # trips.delete()
        return render(request, "main_app/index.html", context)

def newTrip(request):
        return render(request, "main_app/addTrip.html")

def bookTrip(request):
        if 'first_name' not in request.session:
                redirect('/')
        results = Trip.objects.validate(request.POST)
        if len(results['errors']) > 0:
                for error in results['errors']:
                        messages.error(request, error)
                return redirect('/newTrip')
        newTrip = Trip.objects.create(destination = request.POST['destination'], description = request.POST['description'], startDate = request.POST['startDate'], endDate = request.POST['endDate'], creator = request.session['first_name'])
        traveler = User.objects.get(id = request.session['id'])
        newTrip.traveler.add(traveler)
        return redirect("/index")


def travelInfo(request, id):
        if 'first_name' not in request.session:
                redirect('/')
        context = {
                "trip" : Trip.objects.get(id = id)
                
        }
        return render(request, "main_app/tripInfo.html", context)


def join(request, id):
        if 'first_name' not in request.session:
                redirect('/')
        curUser = User.objects.get(id = request.session['id'])
        trip = Trip.objects.get(id = id)
        trip.traveler.add(curUser)
        return redirect('/index')