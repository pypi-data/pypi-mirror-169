# Immediate content

This kind of section content is exactly dynamic content but returned togheter with section data on the list of sections.

All we need to do is inherit from the Foo class and implement the required method. Referring to the example with Banners from `/docs/DYNAMIC_CONTENT.md`.

In mybanners.models.py file
```
    from appchance_sections.models import DynamicContentAbstract, ImmediateContentMixin


    class BannerSet(ImmediateContentMixin, DynamicContentAbstract):
        URL = None
        WIDGETS = ["banner_slider", "banner_carousel"]
        PLACEHOLDERS = ["home_top", "between_products"]
        PREFIX = "banners"

        def get_data_immediately(self):
            data = [item.item for item in self.bannersinset.all().order_by("order")]
            serializer = self.get_serializer(data, many=True)
            return serializer.data
```

**Note**:
The `BannerSet.URL` - it is no longer needed so is set to `None`.
