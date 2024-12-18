from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # type: ignore
from .models import Todo


class TodoListView(ListView):
  model = Todo

class TodoCreateView(CreateView):
  model = Todo
  fields = ['title','deadline']
  success_url = reverse_lazy('todo_list') # type: ignore

class TodoUpdateView(UpdateView):
  model = Todo
  fields = ['title','deadline']
  success_url = reverse_lazy('todo_list') # type: ignore

class TodoDeleteView(DeleteView):
  model = Todo
  success_url = reverse_lazy('todo_list') # type: ignore
