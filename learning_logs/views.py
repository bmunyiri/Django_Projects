from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm

# index view.
def index(request):
    """The Home Page for learning_logs"""
    return render(request, 'learning_logs/index.xhtml')

#Topics view.
def topics(request):
    topics = Topic.objects.all().order_by('date_added')  
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.xhtml', context)


def new_topic(request):
    """add new topic """
    if request.method !='POST':
        #No data submitted 
        form = TopicForm()
    else:
        #form data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')


    #Display a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.xhtml', context)
