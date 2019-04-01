#from django.conf.urls import url, include
from django.urls import include, path

from django.contrib.auth.models import User
from quick.ninja.models import Nija
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class NijaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nija
        fields = ( "pk","first_name","last_name","gender")



 



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Nija.objects.all()
    serializer_class = NijaSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('nija', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]