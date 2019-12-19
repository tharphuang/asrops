'''
数据序列化操作
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Mate:
        model = User
        fields = ('url', 'username')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Mate:
        model = Group
        fields = ('url', 'name')
