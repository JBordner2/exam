from __future__ import unicode_literals
from datetime import date, datetime
from ..login_app.models import User
from django.db import models


class TripManager(models.Manager):
        def validate(self, postData):
                results = {"errors" : [], "status" : False}
                for key in postData:
                        if str(postData['startDate']) > str(postData['endDate']):
			        results['errors'].append("Please re-check your dates")
                                results['status']=True
                        if str(date.today()) > str(postData['startDate']):
			        results['errors'].append("Please re-check your dates")
                                results['status']=True
                        if len(postData['destination']) < 4:
                                results['errors'].append("Please enter a valid destination")
                                results['status']=True
                        if len(postData['description']) < 6:
                                results['errors'].append("Please enter a valid description")
                                results['status']=True


                        return results


class Trip(models.Model):
        destination = models.CharField(max_length = 255)
        description = models.CharField(max_length = 255)
        startDate = models.CharField(max_length = 255)
        endDate = models.CharField(max_length = 255)
        traveler = models.ManyToManyField(User, related_name = "travelers")
        creator = models.CharField(max_length = 200)
        objects = TripManager()