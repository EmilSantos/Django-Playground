from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import PostModelForm
from .models import PostModel

def post_model_create_view(request):
  if request.method == "POST":
    print(request.POST)
  form = PostModelForm(request.POST or None)
  context = {
    "form": form
  }
  if form.is_valid():
    obj = form.save(commit=False)
    obj.save()
    messages.success(request, "Created a new blog post")
    return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
  template = "blog/create-view.html"
  return render(request, template, context)

def post_model_detail_view(request, id=None):
  obj = get_object_or_404(PostModel, id=id)
  context = {
    "object": obj,
  }
  template = "blog/detail-view.html"
  return render(request, template, context)

#@login_required(login_url='/login/')
def post_model_list_view(request):
  print(request.user)
  qs = PostModel.objects.all()
  template = "blog/list-view.html"
  context = {
    "object_list": qs
  }
  if request.user.is_authenticated:
    template = "blog/list-view.html"
  else:
    template = "blog/list-view-public.html"
  return render(request, template, context)