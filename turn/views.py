from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serial import TodoSerial
from .models import Todo
from rest_framework import status

from rest_framework.views import APIView

@api_view(['GET', 'POST', 'DELETE'])
def home(request):
    if request.method == 'POST':
        return Response({
            'status' : status.HTTP_200_OK,
            'message' : 'Yes/ Django is Working'
        })
    
    elif request.method == 'GET':
        return Response({
            'status' : status.HTTP_100_CONTINUE,
            'message' : 'this is GET method'
        })
    elif request.method == 'DELETE':
        return Response({
            'status' : status.HTTP_508_LOOP_DETECTED,
            'message': 'This is DELETE method'
        })
    else:
        raise Exception
    
@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        ser = TodoSerial(data=data)
        if ser.is_valid():
            ser.save()
            return Response({
                'status': True,
                'message': 'Success Data',
                'data': ser.data
            })  
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong',
            'data' : ser.error
        })

        
@api_view(['GET'])
def get_todo(request):

    todo_obj = Todo.objects.all()
    ser = TodoSerial(todo_obj, many= True)
    return Response({
        'status' : True,
        'message' : 'Todo Fetched',
        'data' : ser.data
    })

@api_view(['PATCH'])
def update_patch(request):
    
    try:

        data = request.data

        if not data.get('uid'):
            return Response({
                'status' : False,
                'message' : 'uid is required',
                'data' : {}
            })
        
        obj = Todo.objects.get(uid = data.get('uid'))
        ser  =TodoSerial(obj, data= data, partial = True)
        if ser.is_valid():
            ser.save()
            return Response({
                'status' : True,
                'message' : 'success data',
                'data' : ser.errors
            })
        
    except Exception as e:
        print(e)

        return Response({
            'status' : False,
            'message' : 'invalid uid',
            'data' : {}
        })
    

@api_view(['DELETE'])
def delete_todo(request):
    try:
        if 'uid' in request.data:
            uid = request.data['uid']
            obj = Todo.objects.get(uid=uid)
            obj.delete()
            return Response({
                'status': True,
                'message': 'Deleted',
                'data': {}
            })
    except Todo.DoesNotExist:
        return Response({
            'status': False,
            'message': 'Todo not found',
            'data': {}
        })

    
class TodoClass(APIView):
    def get_queryset(self, uid):
        try:
            return Todo.objects.filter(uid = uid)
        
        except Todo.DoesNotExist:
            return None
        

    def get(self, request):
        return Response({
            'status' : True,
            'message' : 'Yes this is working',
            'method called' : 'The GET method is called'
        })
    
    def post(self, request):
        return Response({
            'status' : True,
            'message' : 'Yes this is working',
            'method called' : 'This is the post'
        })
    
    def patch(self, request):
        return Response({
            'status' : False,
            'message' : 'Hey How are you'
        })
    

