from rest_framework import serializers
from .models import Product, Category, File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description', 'avatar']
        read_only_fields = ['created_at', 'updated_at']
    
        
class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.ChoiceField(choices=File.FileType.choices, source='get_file_type_display')
    def get_file_type_display(self, obj):
        return obj.get_file_type_display()
    
    class Meta:
        model = File
        fields = ['id', 'title', 'file_type','file']
        read_only_fields = ['created_at', 'updated_at']       

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True)
    file = FileSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'avatar', 'category', 'file', 'url']
        read_only_fields = ['created_at', 'updated_at']
    def get_foo(self, obj):
        return obj.id
        
class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    def get_foo(self, obj):
        return obj.id
        
