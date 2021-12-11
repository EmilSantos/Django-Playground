from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import PostModel

def post_model_detail_view(request, id=None):
  print(id)
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