from rest_framework import serializers
from .models import Bookmarks,tags
class bookmarksapi(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ['id','Link','Title','Time_Created','Publisher','Tags']
class tagapi(serializers.ModelSerializer):
    class Meta:
        model = tags
        fields = ['tag_id','Title','Time_Created']