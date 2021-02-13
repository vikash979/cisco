from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import RouterDetails
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
# from users.views import paginator_maker
import django_filters
from django.contrib.auth.models import User
from . import serializers
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
import shutil
import getpass

import os
import pwd
import subprocess



from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
import re


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	print(request)
	username = request.data.get("username")

	password = request.data.get("password")
	if username is None or password is None:
		return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
		
	user = authenticate(username=username, password=password)
	
	if not user:
		return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
	token,_= Token.objects.get_or_create(user=user)
	return Response({'token': token.key}, status=HTTP_200_OK)


class CustomAuth(ObtainAuthToken):
	def post(self,request, *args,**kwargs):
		serializer  = self.serializer_class(data=request.data, context ={'request':request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token,_= Token.objects.get_or_create(user=user)
		return Response({'token': token.key}, status=HTTP_200_OK)


class RouterViewset(viewsets.ModelViewSet):   
    queryset = RouterDetails.objects.all()
    serializer_class = serializers.RouterSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ['hostname','macaddress', 'sapid']
    filterset_fields = ('hostname','macaddress','sapid')


    def get_object(self, pk):
        try:
            return RouterDetails.objects.get(pk=pk)
        except RouterDetails.DoesNotExist:
            raise Http404


    def retrieve(self, request, pk=None):
    	instance = self.get_object(pk=pk)
    	serializer = serializers.RouterSerializer(instance)
    	return Response(serializer.data)

    def create(self, request, *args, **kwargs):  
    	serializer = serializers.RouterSerializer(data=request.data)
    	serializer.is_valid(raise_exception=True)
    	if serializer.is_valid() == True:
    		serializer.save()

    	return Response(serializer.data,status=HTTP_200_OK)


    def update(self, request, pk=None):
    	instance = RouterDetails.objects.get(ip=request.data.get('ip'))
    	partial = True
    	#serialize = RouterDetails.objects.filter(ip=request.data.get('ip')).update(hostname=request.data.get('hostname'))
    	serializer = serializers.RouterSerializer(instance, data=request.data, partial=partial)
    	if serializer.is_valid():
    		# print("helloooo")
    		serializer.save()
    		return Response(serializer.data)

    	return Response(serializer.error)


    def destroy(self, request, pk=None):
        try:
            instance = self.get_object(pk=pk)
            instance.delete()
        except:
            pass
        return Response(status=HTTP_204_NO_CONTENT)



class IpViewset(viewsets.ModelViewSet):   
    queryset = RouterDetails.objects.all()
    serializer_class = serializers.RouterSerializer
    #permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    


    def get_object(self, pk):
        try:
            return RouterDetails.objects.get(pk=pk)
        except RouterDetails.DoesNotExist:
            raise Http404


    def list(self, request, pk=None):
    	instance = self.get_object(pk=pk)
    	serializer = serializers.RouterSerializer(instance)
    	return Response(serializer.data)




from django.http import JsonResponse

def ipRange(start_ip, end_ip):
  start = list(map(int, start_ip.split(".")))
  end = list(map(int, end_ip.split(".")))
  temp = start
  ip_range = []

  ip_range.append(start_ip)
  while temp != end:
    start[3] += 1
    for i in (3, 2, 1):
      if temp[i] == 256:
        temp[i] = 0
        temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

  return ip_range



@csrf_exempt
def ipmacid(request):
	if request.method=='POST':
		Start_ip = request.POST['startip']
		End_ip = request.POST['endip']
		try:
			#t=RouterDetails.objects.filter(ip__lte=Start_ip,ip__gte=End_ip)
			t = ipRange(Start_ip, End_ip)
			
			#t ="uuu"
		except:
			t = None
			
		if isinstance(t,list)==True:
			tt=RouterDetails.objects.filter(ip__in=t).values()
			assessments = [{'id':assessment, } for assessment in tt]
		else:
			tt = 'No records'
			assessments = {}

		print(assessments)


	
	return JsonResponse({"data":assessments})
    

class TokenView(TemplateView):
    template_name = "tokencisco/index.html"


    def get(self, request, *args, **kwargs):
    	ctx= {}
    	username = getpass.getuser()
    	path = "/home/"+username+"/Documents"
    	stat = shutil.disk_usage(path)
    	ctx['disk_usage'] = stat[0]
    	ctx['used_disk'] = stat[1]

    	path = os.getcwd()
    	node_name = []
    	with os.scandir(path) as shutle:
    		
    		for entry in shutle:
    			node_name.append(entry.name+"---"+str(entry.inode()))
    	ctx['inode'] = node_name
    	import subprocess
    	out  =  subprocess.call(["ls", "-l"] , shell=True)
    	print("-------------------",out)
    	ctx['listdir'] = out



    	return render(request, self.template_name, ctx)

      
        
from django.shortcuts import redirect
import json

def delete_post(request,pk):
	dell = RouterDetails.objects.get(pk=pk)
	dell.delete()
	return redirect('/user/tokenapp/')

	#return JsonResponse({"gfg":"yt"})
   

def update_post(request):

    dell = RouterDetails.objects.filter(ip=request.GET.get('ip')).update(hostname=request.GET.get('hostname'), macaddress=request.GET.get('macadd'))
    return redirect('/user/tokenapp/')
	
	
	#dell.delete()

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def nrouter_post(request):
    hostname = request.GET.get('hostname')
    loopback = request.GET.get('ip')
    macadd = request.GET.get('macadd')
    sapid = request.GET.get('sapid')
    print(sapid,"----",loopback,"----",macadd,"----",hostname)
    routerdata =  RouterDetails.objects.create(sapid=sapid,ip=loopback, hostname=hostname,macaddress=macadd)
    return redirect('/user/tokenapp/')





class TokenUpdateView(TemplateView):
    template_name = "tokencisco/edit.html"


    def get(self, request, *args, **kwargs):
    	print(request.GET.get('id'))
    	ctx= {}
    	editupdate = RouterDetails.objects.get(pk=request.GET.get('id'))
    	ctx['updatedata']= editupdate

    	


    	return render(request, self.template_name, ctx)
        
class AddNrouterView(TemplateView):
    template_name = "tokencisco/naddrouter.html"
    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class AddRouterView(TemplateView):
    template_name = "tokencisco/addrouter.html"

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)


    def post(self,request,*args, **kwargs):
        ctx = {}
        error = {}
        if request.method == "POST":
            sapid = request.POST.get('sapid')
            hostname = request.POST.get('hostname')
            loopback = request.POST.get('ip')
            mcadd = request.POST.get('mcadd')
            if sapid=='' :
                ctx['sapid'] = "Please Insert the sapid"
            if hostname=='' :
                ctx['hostname'] = "Please Insert the hostname"
            if loopback=='' :
                ctx['loopback'] = "Please Insert the loopback"
           

            if mcadd=='' :
                error['sapid'] = "Please Insert the mcadd"
            if error == {}:
                routerdata =  RouterDetails.objects.create(sapid=sapid,ip=loopback, hostname=hostname,macaddress=mcadd)
                ctx ['msg'] = "Saved Successfully"
                return redirect('/user/tokenapp/')

            else:
                ctx ['msg'] = ctx
                
        return render(request, self.template_name, ctx)
        

 


 
    