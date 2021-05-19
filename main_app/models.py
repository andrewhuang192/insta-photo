from django.db import models
from django.urls import reverse
from datetime import date

REACTIONS = (
    ('L', 'Like'),
    ('D', 'Dislike'),
    ('F', 'Favorite')
)

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tags_detail', kwargs={'pk': self.id})

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'photo_id': self.id})

    def commented_for_today(self):
        return self.comment_set.filter(date=date.today()).count() >= 1

class Comment(models.Model):
    date = models.DateField('comment date')
    comment_text = models.CharField(max_length=250)
    reaction = models.CharField(
        max_length=1,
            choices=REACTIONS,
            default=REACTIONS[0][0]   
    )
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_reaction_display()} on {self.date}"

     # change the default sort
    class Meta:
        ordering = ['-date']