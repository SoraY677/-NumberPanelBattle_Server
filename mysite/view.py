from django.shortcuts import render
from django.http.response import JsonResponse

def index(request):
    message = request.GET.get("prm", "World")
    print("hogehoge")
    return JsonResponse({"test": [
      [1, 2, 3],
      [4, 5, 6]
      7, 8, 9]});