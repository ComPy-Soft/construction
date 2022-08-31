from django.urls import path
from django.shortcuts import render

def construction_stage_chart(request):
    return render(request, 'Construction/construction_stage_chart.html')

construction_stage_chart_templates = [
    path('construction_stage_chart/', construction_stage_chart, name='construction_stage_chart'),
]