Appchance Sections
==================

This application will allow you to implement flexible sections. It is not an out of the box mechanism and its
implementation requires a bit of effort, but in return you get a solution that you can relatively easily adapt
to your needs.

Including: 
 - the possibility of generic and dynamic content,
 - convenient operation in the admin panel.

This solution was designed for the Django Rest Framework.


Not so quick start
------------------

The application `appchance_sections` contains only abstract models so you nead add new application

```
    python manage.py startapp mysections
```

add created app to settings.INSTALLED_APPS

```
    INSTALLED_APPS = [
        ...
        'mysections',
    ]
```

and define real models.


### 1. Real Section Model

In mysections.models.py file define `Section` model. If you need you can add additional fields, but the default fields
provide basic functionality.

```
    from appchance_sections.models import SectionAbstract
    from django.db import models
    
    class Section(SectionAbstract):
        pass
```

In your Django project settings file define `Section` model.

```
SECTION_MODEL = "mysections.Section"
```

In mysections.admin.py use `SectionAdminMixin` **which binds - most importantly - the modified form**.

```
    from appchance_sections.admin import SectionAdminMixin
    from django.contrib import admin
    from mysections.models import Section

    @admin.register(Section)
    class SectionAdmin(SectionAdminMixin):
        pass
```

In mysections.apps.py **it is very important that you do not forget to import `appchance_sections.receivers`
in the config**

```
    from django.apps import AppConfig
    
    class SectionsConfig(AppConfig):
        name = "mysections"
    
        def ready(self):
            from appchance_sections import receivers  # noqa F405
```

The last thing you have to do is add urls to urls.py

```
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("appchance_sections.urls", namespace="sections")),
    ]
```

### 2. Bind content

Then we need some content that we could present in sections. We can add two types of content:
 - generic
 - dynamic

To see how to define dynamic content and how to make this content possible to attach to the section.

Read more in `/docs/DYNAMIC_CONTENT.md` and `/docs/GENERIC_CONTENT.md`.

Sections were originally designed such that the section content is geted asynchronously by separate requests from the api. However, it is possible to get the content of the sections together with the list of sections.

How to? Read in `/docs/IMMEDIATE_CONTENT.md`