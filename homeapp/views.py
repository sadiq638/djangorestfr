from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Obj
from home.serailizers import PersonSerailizers

# Create your views here.


@api_view(['GET','POST', 'PATCH',  'DELETE'])
def index(request):
    if request.method == 'GET' :
        objs=Obj.objects.all()
        serailizer= PersonSerailizers(objs , many= True)
        return Response(serailizer.data)
    elif request.method == 'POST':
        data = request.data
        serializer=PersonSerailizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'PATCH':
        data = request.data
        objct=Obj.objects.get(id=data['id'])
        serializer=PersonSerailizers(objct, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    else:
        data = request.data
        objct=Obj.objects.get(id=data['id'])
        objct.delete()
        return Response({'message':'person deleted'})
    



