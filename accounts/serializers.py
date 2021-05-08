from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Favourite
from movies.serializers import MovieSerializer

class FavouriteSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model=Favourite
        # fields = '__all__'
        exclude = ['user','id']
        

class UserSerializer(serializers.ModelSerializer):
    user_favourites = FavouriteSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password','user_favourites')
        write_only_fields = ('password',)
        read_only_fields= ('id', 'user_favourites',)

    def create(self, validated_data):
        user = super().create(validated_data)
        # this is for hashing password
        user.set_password(validated_data['password'])
        user.save()
        return user