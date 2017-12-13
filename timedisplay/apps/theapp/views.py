from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
	context={
		'time': datetime.now()
	}

	return render(request, 'timedisplay/index.html', context)
