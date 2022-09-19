from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.CharField(
        max_length=500, default="https://i.pinimg.com/564x/af/a4/cc/afa4cc7ccfca3de5986521730366ee91.jpg")


class Author(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    author = user.name

    def get_absolute_url(self):
        return reverse("author", kwargs={'pk': self.pk})

    def __str__(self):
        return self.author.username
