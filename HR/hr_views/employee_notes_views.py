from django.shortcuts import render
from django.urls import path

def add_employee_notes(request):
    return render(request, 'HR/Employee_Notes/add_employee_note.html')

def manage_employee_notes(request):
    return render(request, 'HR/Employee_Notes/manage_employee_note.html')

employee_notes_templates = [
    path('add_employee_note/', add_employee_notes,name='add_employee_note'),
    path('manage_employee_note/', manage_employee_notes,name='manage_employee_note'),
]