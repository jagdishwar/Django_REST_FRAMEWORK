from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer
from .models import Course
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def ApiOverview(request):
  api_urls = {
      'To Return all Courses': '/courses',
      'To add a new Course': '/courses/add',
    'Update an Course': '/courses/{CourseId}/update',
    'Delete an Course': '/courses/{CourseId}/delete',
  }
  return Response(api_urls)


@api_view(['GET'])
def get_courses(request):
  courses = Course.objects.all()
  serializer = CourseSerializer(courses, many=True)
  print('we are entereing into this',courses)
  return Response(serializer.data)


@api_view(['POST'])
def add_course(request):
  serializer = CourseSerializer(data = request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
  else:
      return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_course(request, id):
  try:
      task = Course.objects.get(id=id)
  except Course.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  serializer = CourseSerializer(task, data=request.data)
  data = {}
  if serializer.is_valid():
      serializer.save()
      data["success"] = "updated successfully"
      return Response(data=data)
  return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_course(request, id):
  try:
      task = Course.objects.get(id=id)
  except Course.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  operation = task.delete()
  data = {}
  if operation:
      return Response(status=status.HTTP_202_ACCEPTED)
  else:
      return Response(status=status.HTTP_404_NOT_FOUND)