from django.urls import path # type: ignore
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView

urlpatterns = [
   path('', TodoListView.as_view(), name='todo_list'), # type: ignore
   path('create/', TodoCreateView.as_view(), name='todo_create'), # type: ignore
   path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo_update'), # type: ignore
   path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo_delete')] # type: ignore


