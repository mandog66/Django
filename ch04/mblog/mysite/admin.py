from django.contrib import admin
from mysite.models import Post, NewTable, Product

# 自訂Post顯示的方式
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
# 將Post納入管理
admin.site.register(Post, PostAdmin)

admin.site.register(NewTable)
admin.site.register(Product)
