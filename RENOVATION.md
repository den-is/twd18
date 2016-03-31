* Using relative imports https://www.python.org/dev/peps/pep-0328/
* __4.5__  Mapping URLs https://docs.djangoproject.com/en/1.8/releases/1.8/#django-conf-urls-patterns
* __5.1.1-2__  Configuring the Templates Directory https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/#the-templates-settings
* __5.3-4__ serve uploaded media as suitable for Django 1.8. refine description of static files. https://docs.djangoproject.com/en/1.8/howto/static-files/
* __6.7__ slightly updated populate_rango script. Used related objects reference instead of directly quering page table by category id
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
* __7.3.4__ Used related objects reference instead of directly quering page table.
* __7.*__ and ongoing, used `url` template tag instead of hardcoded links
* __8.2.2__ using django shortcuts `redirect(reverse('view_name'))` in `add_category`
* __8.2.7__ clean() method override. https://docs.djangoproject.com/en/1.8/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
* __8.2.7__ actual html URL widget not allowing to enter url without `http://`
* __9.3__ broken markup in the beginnig
* __9.3__ admin interfaca; make UserProfile StackedInline into User admin page. https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model
* __9.4.2__ no need `data=request.POST` for bounding forms just Form(request.POST)
* __9.8__ exercise hint. used django messages framework. https://docs.djangoproject.com/en/1.8/ref/contrib/messages/
* __11.6__ minor code refactor
* __12__ slight refactoring of templates for registration redux. `{% extends 'base.html' %}`
* __12.3.6__ typo `LOGIN_REQUIRED` instead of `LOGIN_URL`
* __12.3.7__ Overwritten MyRegistration view did not work.
  ```python
  # Create a new class that redirects the user to the index page, if successful at logging
  class MyRegistrationView(RegistrationView):
      def get_success_url(self,request, user):
          return '/rango/'
  ```
  ```
  TypeError at /accounts/register/
  get_success_url() takes exactly 3 arguments (2 given)
  ```
  Actually mentioned it at __16.3(1)__ when first tried registering with add_profile functionality. Substituted it with:
  ```python
  # Create a new class that redirects the user to the index page, if successful at logging
  class MyRegistrationView(RegistrationView):
      success_url = '/rango/'
      # or
      # success_url = '/rango/add_profile/'
  ```
* __13__ Bootstrapping Rango
  * downloaded all required files into static folder and used `{% load staticfiles %}`
  * Bootstrap 3.3.6
  * JQuery 1.12.2
  * __13.2.1__ template typo: `div class='page-header'` - open div should be outside of `if` statement
  * __13.2.1__ typo at pages section  `<strong>There are no categories present.</strong>` should be pages instead of categories
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
    * in login.html change `<h2>` class to .form-heading
    * in registration_form.html add `<h2>` with same class
    * give your registration form class `form-register`
    * in form template add `{% load staticfiles %}`
    * add in tempates `<link href="{% static 'css/forms.css' %}" rel="stylesheet">`
    * __repeat same for other forms_
  * add `target="_blank"` to page links so they open in a new tab
  * make `Add Page` link on category pages act as a button, adding `class="btn btn-primary" role="button"`
* __14.2__ update template for get_category_list templatetag (IMHO more readable)
* __15.2__ switch to `requests` package instead of urllib
* __15.3__ store secrets (BING_API_KEY) in separate file (e.g. rango/secrets.py). Example contents of secrets.py:
  ```python
  import os

  BING_API_KEY = None

  if os.getenv('BING_API_KEY'):
      BING_API_KEY = os.getenv('BING_API_KEY')
  else:
      BING_API_KEY = "YOUR_BING_API_KEY_GOES_HERE"
  ```
* __16.1__ involve get_object_or_404 helper function (use it in other places as well)
* __17.1.3__ use bootstrap badge class in list items for views/likes
* __16.3(2)__ rename profile -> profile_edit in view, template, url_name
* __16.3(2)__ add readonly user profile page and/or combine it with user area page (list of users)
