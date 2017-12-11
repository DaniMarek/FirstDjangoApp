from __future__ import unicode_literals
# do I need the code above?
from django.shortcuts import render, HttpResponse, redirect
# this is stuff the teacher can do on the tracker app
def index(request):
	return HttpResponse('placeholder to later display all the list of students tracked')

def new(request):
	return HttpResponse('placeholder to display a new form to create a new tracker')

def create(request):
	return redirect('/')

def show(request, tracker_id):
	print tracker_id
	return HttpResponse('placeholder to display tracker {}'.format(tracker_id))

def edit(request, tracker_id):
	return HttpResponse('placeholder to edit tracker info {}'.format(tracker_id))

def delete(request, tracker_id):
	return redirect('/')