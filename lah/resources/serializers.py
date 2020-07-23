from rest_framework import serializers

from .models import Resource, Tag


class InlineTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Resource
        fields = "__all__"
