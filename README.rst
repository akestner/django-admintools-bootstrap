Django Admin Bootstrap theme
============================

A fork without mediagenerator (I use pipeline instead) and with some of my fixes and hacks. More or less provides bootstrap3 theme for admintools.

What other authors wrote:

Twitter Bootstrap support for Django Admin. Requires django-admin-tools and mediagenerator packages.
It also requires SASS to be installed.

This module started out life here:

https://bitbucket.org/salvator/django-admintools-bootstrap

I've developed it to fit into my preferred Django stack that includes mediagenerator and SASS. I've also updated to Bootstrap 3 and fixed a few bugs, as well as restyling things and including Glyphicons.

I'm currently trying to get this included as part of Django proper. Please star it if you would like to see it included as part of Django. Please remember that this is just a quick prototype and will be fully tested if accepted. (I don't believe that admintools will become a part of Django project in near future. -- Ivan)

Screenshots
-----------

Deleted, I don't need them.

Features
--------

* Bootstrap 3
* Much nicer widgets for images and dates (dunno, never tested yet)
* More responsive
* Some nice icons (dunno where they are :) )
* Dashboard
* Cleaner javascript
* Feincms tree editor support
* Admin Widgets easier to extend with custom templates
* django-pipeline asset manager (with plans to enable use of others)


Install
-------

 $ pip install -e git+https://github.com/anishchuk-ia/django-admintools-bootstrap#egg=admintools_bootstrap

* Insert `admintools_bootstrap` to your INSTALLED_APPS before `admin_tools` and `django.contrib.admin` apps.
* Make sure you have static files application installed and configured. See https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/ for details.
* add the following below where PIPELINE_JS/PIPELINE_CSS are set in your settings file:

    import admintools_bootstrap as bs3
    PIPELINE_CSS.update(bs3.ADMIN_PIPELINE_CSS)
    PIPELINE_JS.update(bs3.ADMIN_PIPELINE_JS)

* make sure your sass compiler settings are like these and compiler is working:

    PIPELINE_SASS_BINARY = '/usr/bin/env sass'  # it's a default value, you may omit it
    PIPELINE_SASS_ARGUMENTS = '--update --compass'  # --compass is required here

* ...
* Enjoy.

(If you didn't use pipeline before, just replace PIPELINE_CSS.update with PIPELINE_CSS = and everything should work. Refer to pipeline's docs for more info. You need )

Widgets
-------

There are some custom widgets for your pleasure including a nice image widget I picked up and a bootstrap-datetimepicker.js implementation.
To use these widgets, just subclass admintools_bootstrap.models.BootstrapModelAdmin in your admin.py files

	from admintools_bootstrap.models import BootstrapModelAdmin

	class ExampleAdmin(BootstrapModelAdmin):
	...

Alternatively if you are already subclassing something else you can simply do it like this using formfield_overrides:

	class ExampleModelAdmin(admin.ModelAdmin):

		formfield_overrides = {
	        DateTimeField: {'widget': BootstrapAdminSplitDateTime},
	        DateField: {'widget': BootstrapAdminDateWidget},
	        ImageField: {'widget': BootstrapAdminImageWidget},
	    }


Site name in navigation bar and title
-------------------------------------

(Ugly stuff. Sites should be deleted and replaced with settings.)

admintools-bootstrap can use current site to display site name in admin interface.

To enable this feature, add `django.contrib.sites` to your `INSTALLED_APPS` list (if you have not yet).

Set site name and domain in `django.contrib.sites` admin.



Settings
--------

Site link::

 ADMINTOOLS_BOOTSTRAP_SITE_LINK = '/'

If not False, display specified link to site in the top panel

See above for pipeline dicts.


Used software:
--------------

* http://twitter.github.com/bootstrap/
* https://bitbucket.org/izi/django-admin-tools/
* http://www.crummy.com/software/BeautifulSoup/
* https://github.com/jezdez/django-appconf
* http://pypi.python.org/pypi/versiontools
* https://github.com/cyberdelia/django-pipeline
* http://sass-lang.com/
* bootstrap-datetimepicker.js
* some nice image widget which i'll find the link for!


TODO (mine)
----

* replace sass with less (I don't mind, but I usually never use sass)
* fix icons
* figure out a way to support various asset managers
* get rid of sites.* stuff

TODO (not mine)
----

* better mobile support
* get rid of those green plus icons!
* improve the dashboard views
* reduce dependencies, in particular mediagenerator. Then just add support for it
