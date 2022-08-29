from django.shortcuts import render
from django.urls import path

################################# Users Registration ################################################
def AddUsers(request):
    return render(request, "Registration/add_users.html")


def ManageUsers(request):
    return render(request, "Registration/manage_users.html")


users_template = [
    path("add_users/", AddUsers, name="add_users"),
    path("manage_users/", ManageUsers, name="manage_users"),
]
