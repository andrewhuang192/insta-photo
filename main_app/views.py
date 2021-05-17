from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

class Photo:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, category, description, age):
    self.name = name
    self.category = category
    self.description = description
    self.age = age

photos = [
  Photo('Lolo', 'tabby', 'foul little demon', 3),
  Photo('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Photo('Raven', 'black tripod', '3 legged photo', 4)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def photos_index(request):
  return render(request, 'photos/index.html', { 'photos': photos })

def profile(request):
 return render(request, 'photos/profile.html', {'photos': photos })