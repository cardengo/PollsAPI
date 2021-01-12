from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class PollAPI(APIView):
    """
    Create/patch/delete poll.
    """
    permission_classes = [IsAdminUser]

    def get_obj(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, poll_id, format=None):
        poll = self.get_obj(pk=poll_id)
        serializer = PollSerializer(poll, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, poll_id, format=None):
        poll = self.get_obj(pk=poll_id)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionAPI(APIView):
    """
    Create/patch/delete question in poll.
    """
    permission_classes = [IsAdminUser]

    def get_obj(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)

        try:
            Poll.objects.get(pk=request.data['poll'])
        except Question.DoesNotExist:
            raise Http404

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, question_id, format=None):
        question = self.get_obj(pk=question_id)
        serializer = QuestionSerializer(
            question, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, question_id, format=None):
        question = self.get_obj(pk=question_id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
