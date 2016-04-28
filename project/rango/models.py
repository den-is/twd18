from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 0
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

def user_pic_upload_path(instance, filename):
    return 'profile_images/{userid}/{imgfile}'.format(userid=instance.user.id, imgfile=filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=user_pic_upload_path,  blank=True)

    def __unicode__(self):
        return self.user.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        UserProfile.objects.get_or_create(user=kwargs.get('instance'))

@receiver(post_delete, sender=UserProfile)
def delete_userpic(sender, instance, **kwargs):
    """Delete UserProfile picture when profile is deleted.
    """
    if instance.picture:
        storage = instance.picture.storage
        path = instance.picture.path
        storage.delete(path)
