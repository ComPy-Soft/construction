from django.shortcuts import render
from django.urls import path

################################# Users Registration ################################################
def add_users(request):
    return render(request, "Registration/Users/add_users.html")


def manage_users(request):
    return render(request, "Registration/Users/manage_users.html")


users_template = [
    path("add_users/", add_users, name="add_users"),
    path("manage_users/", manage_users, name="manage_users"),
]
