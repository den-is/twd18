import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python', 128, 64)

    add_page(cat=python_cat,
            title='Official Python tutorial',
            url='https://docs.python.org/2/tutorial/',
            views=50)

    add_page(cat=python_cat,
            title='How to Think like a Computer Scientist',
            url='http://greenteapress.com/wp/think-python/',
            views=12)

    add_page(cat=python_cat,
            title='Learn Python the Hard Way',
            url='http://learnpythonthehardway.org/book/',
            views=37)

    django_cat = add_cat('Django', 64, 32)

    add_page(cat=django_cat,
            title='Official Django Docs',
            url='https://docs.djangoproject.com/en/1.8/',
            views=49)

    add_page(cat=django_cat,
            title='Django Rocks',
            url='https://www.djangorocks.com/',
            views=14)

    add_page(cat=django_cat,
            title='How To Tango With Django',
            url='http://www.tangowithdjango.com/',
            views=42)

    frame_cat = add_cat('Other Frameworks', 32, 16)

    add_page(cat=frame_cat,
            title='Flask',
            url='http://flask.pocoo.org/',
            views=40)

    add_page(cat=frame_cat,
            title='Bottle',
            url='http://bottlepy.org/docs/dev/index.html',
            views=5)

    for c in Category.objects.all():
        for p in c.page_set.all():
            print " - {cat} - {page}".format(cat=str(c), page=str(p))

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

if __name__ == '__main__':
    print 'Starting Rango population script...'
    populate()
