from django.contrib import admin
from mysite.models import Post, NewTable, Product, Maker, PModel, PPhoto, Ch07_Product

# 自訂Post顯示的方式
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
# 將Post納入管理
admin.site.register(Post, PostAdmin)

admin.site.register(NewTable)
admin.site.register(Product)

admin.site.register(Maker)
admin.site.register(PModel)
admin.site.register(PPhoto)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'price', 'year')
    search_fields = ('nickname',)
    ordering = ('-price',)
admin.site.register(Ch07_Product, ProductAdmin)

