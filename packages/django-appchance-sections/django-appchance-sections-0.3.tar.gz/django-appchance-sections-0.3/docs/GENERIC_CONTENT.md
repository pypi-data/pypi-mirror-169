# Generic Content

Sometimes you don't want to add items to a section manually. For example, you want to view a section with:

- news
- bestsellers calculated on the number of units sold in the last week
- products on promotion marked with the `is_promotion` flag, etc.

You can register such content using `register_section_content`

In *mysections.sections.py*

```
    from appchance_sections.utils import register_section_content
    
    
    def register_section_contents():
        
        placements = ["home_middle", "home_sidebar"]
        
        news_widgets = ["news_list"]
        register_section_content(
            slug="news",
            name="News",
            url="mynews:news-list",
            widgets=news_widgets,
            placements=placements
        )
    
        product_widgets = ["product_grid_3x3", "product_flat_list"]
    
        register_section_content(
            slug="bestsellers",
            name="Bestsellers",
            url="myproducts:product-list",
            query_params={"bestseller": "true"},
            widgets=product_widgets,
            placements=placements
        )
    
        register_section_content(
            slug="promoted_products",
            name="Promoted products",
            url="myproducts:product-list",
            query_params={"is_promotion": 1},
            widgets=product_widgets,
            placements=placements
        )
```

The `register_section_contents` function should be called on start app

For example you can call it in *mysections.apps.py*

```
    from django.apps import AppConfig
    
    class SectionsConfig(AppConfig):
        name = "mysections"
    
        def ready(self):
            from appchance_sections import receivers  # noqa F405
            from mysection.sections import register_section_contents
            register_section_contents()
```