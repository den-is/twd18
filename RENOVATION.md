* Using relative imports https://www.python.org/dev/peps/pep-0328/
* *4.5*  Mapping URLs https://docs.djangoproject.com/en/1.8/releases/1.8/#django-conf-urls-patterns
* *5.1.1-2*  Configuring the Templates Directory https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/#the-templates-settings
* *5.3-4* serve uploaded media as suitable for Django 1.8. refine description of static files. https://docs.djangoproject.com/en/1.8/howto/static-files/
* *6.7* slightly updated poulate_rango script. Used related objects reference instead of directly quering page table by category id
* Code snippet to update existing rows in db "slug" withou populate_rango script
```python
from rango.models import Category
from django.utils.text import slugify

cats = Category.objects.all()
for cat in cats:
    cat.slug = slugify(cat.name)
    cat.save()

# test
cats = Category.objects.all()
for cat in cats:
    print cat.name, cat.slug
```
* *7.3.4* Used related objects reference instead of directly quering page table.
* *7.** and ongoing, used `url` template tag instead of hardcoded links
* *8.2.2* using django shortcuts `redirect(reverse('view_name'))` in `add_category`
* *8.2.7* clean() method override. https://docs.djangoproject.com/en/1.8/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
* *8.2.7* actual html URL widget not allowing to enter url without `http://`
