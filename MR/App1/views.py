from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def recommendation(request):
    return render(request,'recommendation.html')
def MR(request):
    return render(request, 'about.html')
def login_view(request):
    return render(request, 'login.html')
def register(request):
    return render(request,'register.html')
def profile(request):
    return render(request, 'profile.html')
def action(request):
    return render(request, 'action.html')
def love(request):
    return render(request, 'love.html')
def mystery(request):
    return render(request,'mystery.html')
def historical(request):
    return render(request, 'historical.html')
def horror(request):
    return render(request, 'horror.html')
def comedy(request):
    return render(request, 'comedy.html')
def fantasy(request):
    return render(request, 'fantasy.html')
def sci_fi(request):
    return render(request,'sci-fi.html')
