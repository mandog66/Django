from django.contrib import admin
from mysite.models import Post, NewTable, Product, Maker, PModel, PPhoto, Ch07_Product, ch08_Mood, ch08_Post

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

class Ch08_PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)
admin.site.register(ch08_Mood)
admin.site.register(ch08_Post, Ch08_PostAdmin)
