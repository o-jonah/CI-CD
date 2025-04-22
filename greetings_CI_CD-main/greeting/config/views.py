from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'greeting': 'Hello'})

def wrong_view(request):
    return render(request, 'wrong_template.html')  # Template that doesn't exist


