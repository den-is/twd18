from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Category


def add_cat(name, views, likes):
    cat = Category.objects.get_or_create(name=name)[0]
    cat.views = views
    cat.likes = likes
    cat.save()

    return cat

class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """ensure_views_are_positive should results True for categories where views are zero or positive
        """

        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_slug_line_creation(self):
        cat = Category(name='Random Category Name')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-name')

class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """If no questions exist, an appropriate message should be displayed.
        """

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['top5categories'], [])

    def test_index_view_with_categories(self):
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tmp test temp')

        num_cats = len(response.context['top5categories'])
        self.assertEqual(num_cats, 4)
