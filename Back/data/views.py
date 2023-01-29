from rest_framework.views import APIView, Request, Response
from rest_framework.generics import ListCreateAPIView
from django import forms
from .serializer import DataSerializer
from trasation.models import Trasation
from trasation.serializer  import TransationSerializer
from .models import Data
import os
from django.shortcuts import render


class UploadForm(forms.Form):
    file = forms.FileField()
class TransationView(ListCreateAPIView):   
    serializer_class = DataSerializer
    queryset = Data.objects.filter()
    def post(self, request:Request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.files['file']
            name.name
            with open(name.name,'w') as arquivo:
                for valor in request.FILES['file']:
                    valor = valor.decode("utf-8")
                    valor = valor.replace('\n',"")
                    type = valor[0:1]
                    if type == "1":
                        type = dict(type=type, description="Débito", nature="Entrada", signal="+")
                    if type == "2":
                        type = dict(type=type, description="Boleto", nature="Saída", signal="-")
                    if type == "3":
                        type = dict(type=type, description="Financiamento", nature="Saída", signal="-")
                    if type == "4":
                        type = dict(type=type, description="Crédito", nature="Entrada", signal="+")
                    if type == "5":
                        type = dict(type=type, description="Recebimento Empréstimo", nature="Entrada", signal="+")
                    if type == "6":
                        type = dict(type=type, description="Vendas", nature="Entrada", signal="+")
                    if type == "7":
                        type = dict(type=type, description="Recebimento TED", nature="Entrada", signal="+")
                    if type == "8":
                        type = dict(type=type, description="Recebimento DOC", nature="Entrada", signal="+")
                    if type == "9":
                        type = dict(type=type, description="Aluguel", nature="Saída", signal="-")
                    create,_ = Trasation.objects.get_or_create(**type) 
                    date = valor[1:9]
                    year = date[0:4]
                    month = date[4:6]
                    day = date[6:]
                    date =year+"-"+month+"-"+day
                    value = valor[9:19]
                    value = float(value) / 100
                    if create.signal == "-":
                        value = - value
                    recipient_cpf = valor[19:30]
                    card = valor[30:42]
                    hour = valor[42:48]
                    h = hour[0:2]
                    mm = hour[2:4]
                    s = hour[4:]
                    hour = h+":"+mm+":"+s
                    store_owner = valor[48:62]
                    store_owner = store_owner.strip().capitalize()
                    store_name = valor[62:]
                    store_name = store_name.strip().capitalize()
                    transation = dict(
                        store_owner=store_owner,
                        store_name=store_name,
                        recipient_cpf=recipient_cpf,
                        card=card,
                        value=value,
                        date=date,
                        hour=hour,
                        type=create.id
                        )
                    
                    serializer = DataSerializer(data=transation)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()            
        os.remove(name.name)
        return Response({"detail":"Dados extraidos com sucesso !"}, 201)
    def get(self, request, *args, **kwargs):
        data = Data.objects.all()
        serializer = DataSerializer(data, many=True)
        type = Trasation.objects.all()
        serializer2 = TransationSerializer(type, many=True)
        result = []
        for dado in serializer.data:
            new = dict(store_name= dado["store_name"])
            if new not in result:
                result.append(new)            
        for names in result:
            all = Data.objects.filter(store_name=names["store_name"])
            names["saldo"] = 0
            serializer = DataSerializer(all, many=True)
            for val in serializer.data:
                names["saldo"] = names["saldo"] + float(val["value"])                
        return Response(result)
    def upload(request):
        return render(request, 'upload.html')    