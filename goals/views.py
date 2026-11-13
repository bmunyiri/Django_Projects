from django.shortcuts import render
from .models import Goal

# Create your views here.
def goals(request):
    """Show all goals."""
    goals = Goal.objects.all().order_by('date_added')
    context = {'goals': goals}
    return render(request, 'goals/goals.xhtml', context)

