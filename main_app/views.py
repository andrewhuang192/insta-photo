from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photo, Tag
from .forms import CommentForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def photos_index(request):
  photos = Photo.objects.all()
  return render(request, 'photos/index.html', { 'photos': photos })

def photos_detail(request, photo_id):
  photo = Photo.objects.get(id=photo_id)
  # Get the tags the photo doesn't have
  tags_photo_doesnt_have = Tag.objects.exclude(id__in = photo.tags.all().values_list('id'))
  comment_form = CommentForm()
  return render(request, 'photos/detail.html', { 'photo': photo , 'comment_form': comment_form, 'tags': tags_photo_doesnt_have })

def profile(request):
 return render(request, 'photos/profile.html', {'tag': tags_photo_doesnt_have })

class PhotoCreate(CreateView):
  model = Photo
  fields = '__all__'
  success_url = '/photos/'

class PhotoUpdate(UpdateView):
  model = Photo
  fields = ['category', 'description', 'age']

class PhotoDelete(DeleteView):
  model = Photo
  success_url = '/photos/'

def add_comment(request, photo_id):
  form = CommentForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_comment = form.save(commit=False)
    new_comment.photo_id = photo_id
    new_comment.save()
  return redirect('detail', photo_id=photo_id)

def assoc_tag(request, photo_id, tag_id):
  # Note that you can pass a tag's id instead of the whole object
  Photo.objects.get(id=photo_id).tags.add(tag_id)
  return redirect('detail', photo_id=photo_id)

def delete_tag(request, photo_id, tag_id):
  Photo.objects.get(id=photo_id).tags.remove(tag_id)
  return redirect('detail', photo_id=photo_id)