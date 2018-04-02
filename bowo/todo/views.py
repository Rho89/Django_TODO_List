
# todo/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, DeleteView
from todo.models import Todo
from django.urls import reverse_lazy
from todo.forms import TodoForm

from django.shortcuts import get_object_or_404

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


    
class AboutPageView(TemplateView):
    template_name = "about.html"
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'profile.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class ProfilePageView(TemplateView):
    template_name='profile.html'
    model = Todo

class TodoCreateView(CreateView):
    form_class = TodoForm
    success_url = reverse_lazy('todo-list')

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)


TODO_LIST_URL = reverse_lazy('todo-list')

def clear_resolved_todos(request):
    if request.method == 'POST':
        # Modify an object in POST only
        Todo.objects.filter(is_resolved=True).delete()
    return HttpResponseRedirect(TODO_LIST_URL)

class TodoDeleteView(DeleteView):
    model=Todo
    success_url= TODO_LIST_URL
