from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    message = request.GET.get("prm", "World")
    print("hogehoge")
    return JsonResponse({"hote":"hote"});