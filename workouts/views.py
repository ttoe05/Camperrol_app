from django.shortcuts import render, get_object_or_404
from .models import Workout, User, Workout_Summary
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'workouts/index.html'
    context_object_name = 'all_workouts'

    def get_queryset(self):
        return Workout.objects.all()


class DetailView(generic.DetailView):
    model = Workout
    template_name = 'workouts/Description.html'


def workout_summary(request, User_ID):
    user = get_object_or_404(User, pk=User_ID)
    summary = Workout_Summary.objects.filter(User=user)
    content = {
        'user': user,
        'summary': summary,

    }
    return render(request, 'workouts/summary.html', content)
