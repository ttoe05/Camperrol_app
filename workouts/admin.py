from django.contrib import admin
from .models import User, Workout, Workout_Summary
# Register your models here.

admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Workout_Summary)
