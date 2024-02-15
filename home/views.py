from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Students



@api_view(['GET', 'POST' ,'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!",
                         "status" : 200,
                         "method" : "you called GET method"})
    
    elif request.method == 'POST':
        return Response({"message": "Hello, world!",
                         "status" : 200,
                         "method" : "you called POST method"})
    
    elif request.method == 'PATCH':
        return Response({"message": "Hello, world!",
                         "status" : 200,
                         "method" : "you called PATCH method"})

    else:
        return Response({"message": "Hello, world!",
                         "status" : 400,
                         "method" : "you called invalid method"})  
          
    
@api_view(['GET'])
def get_books(request):
    books_obj = Book.objects.all()
    serializer = Book_serializer(books_obj , many = True)
    return Response({'status' : 200, 'message' : 'success get books database', "data": serializer.data })
    


@api_view(['GET'])
def get_student(request):
    stu_obj = Students.objects.all()
    serializer = Student_serializer(stu_obj , many=True)

    return Response({
    'status' : 200,
    'message' : 'success',
    "data": serializer.data
    })
    

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = Student_serializer(data = data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status' : 400,'message' : 'something went wrong'})

    serializer.save()

    return Response({'status' : 200, 'message' : 'success student database created', "data": serializer.data })
    

@api_view(['PUT'])
def put_student(request , id):
    stu_obj = Students.objects.get(id = id)
    data = request.data
    serializer = Student_serializer(stu_obj, data = data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status' : 400,'message' : 'something went wrong'})

    serializer.save()

    return Response({'status' : 200, 'message' : 'success student database upated', "data": serializer.data })



@api_view(['DELETE'])
def delete_student(request , id):
    stu_obj = Students.objects.get(id = id)
    stu_obj2 = stu_obj
    stu_obj.delete()
    return Response({'status' : 200, 'message' : 'success student databse is deleted', "data": stu_obj2.data })