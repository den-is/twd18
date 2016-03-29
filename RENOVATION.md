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
* _12_ slight refactoring of templates for registration redux. `{% extends 'base.html' %}`
* _12.3.6_ typo `LOGIN_REQUIRED` instead of `LOGIN_URL`
* _13_ Bootstrapping Rango
  * downloaded all required files into static folder and used `{% load staticfiles %}`
  * Bootstrap 3.3.6
  * JQuery 1.12.2
  * _13.2.1_ template typo: `div class='page-header'` - open div should be outside of `if` statement
  * _13.2.1_ typo at pages section  `<strong>There are no categories present.</strong>` should be pages instead of categories
  * used `django-crispy-forms`
    * `pip install django-crispy-forms`
    * `in settings.py` add `CRISPY_TEMPLATE_PACK = 'bootstrap3'`
    * in template add `{% load crspy_forms_tags %}`
    * in template change `{{ form.as_p }}` to `{{ form|crispy }}`
  * save signin.css as forms.css in project/static/css
    * add following snippet for registration form and simmilar for other forms:
    ```css
    .form-register {
      max-width: 330px;
      padding: 15px;
      margin: 0 auto;
    }
    ```
    * find `.form-signin-heading` in css file and change it to `.form-heading` - making it universal, coz you can use it for other forms
    * in login.html change <h2> class to .form-heading
    * in registration_form.html add <h2> with same class
    * give your registration form class `form-register`
    * in form template add `{% load staticfiles %}`
    * add in tempates `<link href="{% static 'css/forms.css' %}" rel="stylesheet">`
    * _repeat same for other forms_
  * add `target="_blank"` to page links so they open in a new tab
  * make `Add Page` link on category pages act as a button, adding `class="btn btn-primary" role="button"`
