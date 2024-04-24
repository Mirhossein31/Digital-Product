from rest_framework import serializers
from .models import Category, Product, File


class CategorySerialiser (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title','description','avatar')

class FileSerializer (serializers.ModelSerializer) :
    file_type = serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ('id','title','file_type','file') 
    def get_file_type(self,obj) :
        return obj.get_file_type_display()   

class ProductSerializer (serializers.HyperlinkedModelSerializer) : 
    categories = CategorySerialiser(many = True)
   #auth.... #files = FileSerializer(many =True )
    
    class Meta:
        model = Product
        fields = ('id','title','description','avatar','categories','url')
                            