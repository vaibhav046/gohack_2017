#from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import MasterprofileSerializer, ProfileSerializer,TransactionSerializer
from .models import Masterprofile,Profile,Transaction

class MasterprofileViewSet(ModelViewSet):
    queryset = Masterprofile.objects.all()
    serializer_class = MasterprofileSerializer


class ProfileViewSet(ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
#	acc = Profile.objects.raw('SELECT * FROM moneypool_profile where group_id="123456')
	model = Profile
	def list(self, request):
		id="123456"
#		id=request.GET["id"]
		queryset = Profile.objects.raw('SELECT * FROM moneypool_profile WHERE group_id=%s',[id])
		serializer = ProfileSerializer(queryset, many=True)
		return Response(serializer.data)
	

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
