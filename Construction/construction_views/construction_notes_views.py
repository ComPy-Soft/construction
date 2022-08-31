from django.urls import path
from django.shortcuts import render

def add_construction_note(request):
    return render(request, 'Construction/construction_note/add_construction_note.html')

def manage_construction_note(request):
    return render(request, 'Construction/construction_note/manage_construction_note.html')

construction_notes_templates = [
    path('add_construction_note/', add_construction_note, name='add_construction_note'),
    path('manage_construction_note/', manage_construction_note, name='manage_construction_note'),
]