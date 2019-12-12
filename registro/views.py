from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def registro(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    return render(response, "registro/registro.html",{"form":form})