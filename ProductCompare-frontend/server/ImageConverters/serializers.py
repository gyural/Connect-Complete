# from accounts.serializers import UserSerializer
from .models import CompareList, Obj
from rest_framework import serializers


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obj
        fields = ['object_name', 'image']


class CompareListSerializer(serializers.ModelSerializer):
    objs = ObjSerializer(many=True, read_only=True)

    class Meta:
        model = CompareList
        fields = ['id', 'objs']

    def create(self, validated_data):
        # print(dir(self))
        # user = self.context['request'].user  # Get the user from the request
        print(self)
        comparelist = CompareList.objects.create(**validated_data)

        images_data = self.context['request'].data
        print('-----------------')
        print(images_data.getlist('image'))
        texts_data = self.context['request'].data
        print('-----------------')
        print(texts_data.getlist('object_name'))
        print('-----------------')
        for image_data, text_data in zip(images_data.getlist('image'), texts_data.getlist('object_name')):
            Obj.objects.create(comparelist=comparelist, image=image_data, object_name=text_data)
        return comparelist