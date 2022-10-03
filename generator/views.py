
from operator import length_hint
from django.shortcuts import render
# from django.http import HttpResponse
import random


def home(request):
    return render(request,"generator/home.html")

def about(request):
    return render(request,"generator/about.html")

def password(request):
    
    characteres = list("abcdefghijklmnñopqrstuvwxyz")
    generated_password = ""

    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characteres.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characteres.extend(list("%&/()=?![*+-%&/"))
        
    if request.GET.get("numbers"):
        characteres.extend(list("1234567890"))

    for x in range(length):
        generated_password += random.choice(characteres)

    return render(request,"generator/password.html", {"pass" : generated_password})
