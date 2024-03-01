from rest_framework.decorators import api_view , authentication_classes ,permission_classes
from rest_framework.response import Response
from .serializer import *
from .models import Students
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


## create user by session authentication 

# class RegisterUser(APIView):
#     def post(self , request):
#         serializer = User_srializer(data = request.data)
#         if not serializer.is_valid(): 
#             print(serializer.errors)  
#             return Response({'status' : 400,'message' : 'something went wrong'})
            
#         serializer.save()
#         user = User.objects.get(username = serializer.data['username'])
#         token_obj , _ = Token.objects.get_or_create(user=user)
#         return Response({'status' : 200,'message' : 'user created successfully' , "data" : serializer.data ,"token"  : str(token_obj)})
    

## create user by JWT authentication
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterUser(APIView):
    def post(self , request):
        serializer = User_srializer(data = request.data)
        if not serializer.is_valid(): 
            print(serializer.errors)  
            return Response({'status' : 400,'message' : 'something went wrong'})
            
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status' : 200,
                         'message' : 'user created successfully' ,
                          "data" : serializer.data ,
                          'refresh': str(refresh),
                          'access': str(refresh.access_token) })


 

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
    
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

## authentication in classed based view
# class StudentApi(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self ,request):
#         stu_obj = Students.objects.all()
#         serializer = Student_serializer(stu_obj , many=True)

#         return Response({
#         'status' : 200,
#         'message' : 'success',
#         "data": serializer.data
#         })

## authentication in Function based view

## authentication in Function based view
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self ,request):
        stu_obj = Students.objects.all()
        serializer = Student_serializer(stu_obj , many=True)

        return Response({
        'status' : 200,
        'message' : 'success',
        "data": serializer.data
        })


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_student(request):
    stu_obj = Students.objects.all()
    serializer = Student_serializer(stu_obj , many=True)
    return Response({
    'status' : 200,
    'message' : 'success',
    "data": serializer.data
    })
    
## authentication in Function based view

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
   
    stu_obj.delete()
    return Response({'status' : 200, 'message' : 'success student databse is deleted'})