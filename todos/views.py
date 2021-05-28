from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def todo_list_item(request):
	tasks = Todo.objects.all()

	if request.method == 'POST':
		data = request.POST
		content = data['content']
		todo = Todo(content=content)
		todo.save()
		return redirect('/')

	context = {
		'tasks': tasks,
	}
	return render(request, 'todos/todo_list.html', context)

def delete_todo_item(request, pk):
	task = Todo.objects.get(id=pk)
	task.delete()
	return redirect('/')
