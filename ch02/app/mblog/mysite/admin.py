from django.contrib import admin
from mysite.models import Post

# 自訂Post顯示的方式
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
# 將Post納入管理
admin.site.register(Post, PostAdmin)
