from django.db import models
from django.utils import timezone
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)    

    def get_absolute_url(self):
        return reverse("core:post_detail", kwargs={"pk": self.pk, "slug": self.slug})
    
    # def get_absolute_url(self):
    #     return reverse('core:index',
    #                         args=[self.publish.year,
    #                                 self.publish.month,
    #                                 self.publish.day, self.slug])