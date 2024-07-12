from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from job.views import JobViewSets, PortalViewSets

router = routers.DefaultRouter()
router.register(r"jobs", JobViewSets)
router.register(r"portais", PortalViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
