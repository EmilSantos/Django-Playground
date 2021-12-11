from django.http import HttpResponse, HttpResponseRedirect

# Class Home

def home(request):
  return HttpResponse("<h1>This is home page</h1>")

def redirect_somewhere(request):
  return HttpResponseRedirect("/some/path")

def redirect_test(request):
  return HttpResponse("<h1>New Area</h1>")