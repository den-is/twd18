* Using relative imports https://www.python.org/dev/peps/pep-0328/
* _4.5_  Mapping URLs https://docs.djangoproject.com/en/1.8/releases/1.8/#django-conf-urls-patterns
* _5.1.1-2_  Configuring the Templates Directory https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/#the-templates-settings
* _5.3-4_ serve uploaded media as suitable for Django 1.8. refine description of static files. https://docs.djangoproject.com/en/1.8/howto/static-files/
* _6.7_ slightly updated populate_rango script. Used related objects reference instead of directly quering page table by category id
* Code snippet to update existing rows in db "slug" without populate_rango script
```python
from rango.models import Category
from django.utils.text import slugify

cats = Category.objects.all()
for cat in cats:
    cat.slug = slugify(cat.name)
    cat.save()

# make sure that it worked
cats = Category.objects.all()
for cat in cats:
    print cat.name, cat.slug
```
* _7.3.4_ Used related objects reference instead of directly quering page table.
* _7.*_ and ongoing, used `url` template tag instead of hardcoded links
* _8.2.2_ using django shortcuts `redirect(reverse('view_name'))` in `add_category`
* _8.2.7_ clean() method override. https://docs.djangoproject.com/en/1.8/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
* _8.2.7_ actual html URL widget not allowing to enter url without `http://`
* _9.3_ broken markup in the beginnig
* _9.3_ admin interfaca; make UserProfile StackedInline into User admin page. https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
* _9.4.2_ no need `data=request.POST` for bounding forms just Form(request.POST)
* _9.8_ exercise hint. used django messages framework. https://docs.djangoproject.com/en/1.8/ref/contrib/messages/
* _11.6_ minor code refactor
