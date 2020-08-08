
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "geeky show mini blog"
admin.site.site_title = "mini blog"
admin.site.index_title = "mini blog"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls'))
]
