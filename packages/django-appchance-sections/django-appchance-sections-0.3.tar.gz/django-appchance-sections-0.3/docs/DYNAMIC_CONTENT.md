# Dynamic Content

For example, we want to create a banner application and present banners as a section.

Create new banners app - for example mybanners `python manage.py startapp mybanners`.

In *mybanners.models.py* file

```
    from appchance_sections.models import DynamicContentAbstract
    from django.db import models
    

    # This is standard model - nothing special
    class Banner(models.Model):
        name = models.CharField(max_length=255)
        image = models.ImageFile(upload_to="/uploads")
        url = models.CharField(max_length=255)
    
        def __str__(self):
            return self.name
    
    
    class BannerSet(DynamicContentAbstract):
        URL = "mybanners:bannerset-detail"
        WIDGETS = ["banner_slider", "banner_carousel"]
        PLACEHOLDERS = ["home_top", "between_products"]
        PREFIX = "banners"
    
    
    class BannerInSet(models.Model):
        banner_set = models.ForeignKey(BannerSet, related_name="bannersinset", on_delete=models.CASCADE)
        banner = models.ForeignKey(Banner, related_name="bannersinset", on_delete=models.CASCADE)
        order = models.PositiveSmallIntegerField(default=0)
    
        def __str__(self):
            return f"{self.banner_set.name} {self.banner.name}"
```

**Note**:
The banner set aggregates the banners to be displayed within the sections. Therefore, the BannerSet model must be configured for the section.
 - The `BannerSet.URL` should be a valid url, so you will have to add ViewSet and link it to urls.py
 - The `BannerSet.QUERY_PARAMS` allows you to add additional fixed query params to the url
 - The `BannerSet.PREFIX` is not required but useful because it is visible when adding content to a section
    in the Admin Panel
 - The `BannerSet.WIDGETS` and `BannerSet.PLACEHOLDERS` - list of widgets and section presentation places
    supported by the consument API
 - The `BannerSet.FILTER_ATTRIBUTE` - If you implement a custom filter that will allow you to filter 
    the list of banners assigned to a given section, this is where you enter the name of the query string parameter
    that is used to pass the section ID

You need `BannerSerializer` at first. It depends on your model. In this example it could look like this.

In *mybanners.serializer.py*

```
    from mybanners.models import Banner
    from rest_framework.serializers import ModelSerializer
    
    
    class BannerSerializer(ModelSerializer):
        class Meta:
            model = Banner
            fields = ["id", "name", "image", "url"]
```

In *mybanners.views.py*

```
    from mybanners.models import Banner, BannerSection
    from mybanners.serializers import BannerSerializer
    from rest_framework import mixins, viewsets
    
    from rest_framework.response import Response
    
    
    class BannerViewSet(viewsets.ReadOnlyModelViewSet):
        model = Banner
        permission_classes = (AllowAny,)
        queryset = Banner.objects.all()
        serializer_class = BannerSerializer
    
    
    class BannerSetViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    
        model = BannerSet
        queryset = BannerSet.objects.all()
        serializer_class = BannerSerializer
    
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            data = [item.item for item in instance.bannersinset.all().order_by("order")]
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
```

**Note that the `BannerSetViewSet.list` returns a list of banners** because you get the `BannerSet`
data when you request a list of sections from sections endpoint.


**Note! Alternatively, you can implement views like this - filter list by section**

```
    import django_filters
    from mybanners.models import Banner
    from mybanners.serializers import BannerSerializer
    from rest_framework import viewsets
    
    
    class BannerListFilterSet(django_filters.FilterSet):
        # do not forget set BannerSet.FILTER_ATTRIBUTE = "section"
        section = django_filters.NumberFilter(method="get_by_section", field_name="section")
    
        class Meta:
            model = Banner
            fields = []
    
        def get_by_section(self, queryset, _field_name, value):
            return (
                queryset.filter(banners_in_set__banner__id=value).order_by("banners_in_set__order")
                if value else queryset
            )
    
    class BannerViewSet(viewsets.ReadOnlyModelViewSet):
        model = Banner
        permission_classes = (AllowAny,)
        queryset = Banner.objects.all()
        serializer_class = BannerSerializer
        filter_class = BannerListFilterSet
```

In *mybanners.urls.py*

```
    from mybanners.views import BannerSetViewSet, BannerViewSet
    from rest_framework import routers
    
    router = routers.DefaultRouter()
    router.register(r"banners", BannerViewSet)
    router.register(r"banner-sections", BannerSetViewSet)
    
    app_name = "banners"
    urlpatterns = router.urls
```

and


```
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("appchance_sections.urls", namespace="sections")),
        path("", include("mybanners.urls", namespace="banners")),
    ]
```

Now the `BannerSet` model needs to be registered also as dynamic content for the section.

In *mybanners.sections.py* file define a registration function.

```
    from appchance_sections.utils import register_dynamic_content
    from mybanners.models import BannerSet
    
    
    def register_section_contents():
        register_dynamic_content(content_class=BannerSet)
```

The `register_section_contents` function should be called when the banner application is ready

So call it in *mybanners.apps.py*

```
    from django.apps import AppConfig
    
    
    class BannersConfig(AppConfig):
        name = "mybanners"
    
        def ready(self):
            from mybanners.sections import register_section_contents
            register_section_contents()
```