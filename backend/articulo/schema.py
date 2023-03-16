import graphene
from graphene_django import DjangoObjectType
from .models import Articulo

class ArticuloType(DjangoObjectType):
  class Meta:
    model = Articulo
    fields = '__all__'
    

class Query(graphene.ObjectType):
  articulo = graphene.List(ArticuloType)



  def resolve_articulo(self, info, **kwargs):
   return Articulo.objects.all()   

schema = graphene.Schema(query=Query)    