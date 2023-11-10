from django.shortcuts import render, HttpResponse
from home.models import Contact
from django import forms
from home.linked_list import Node, Sinlink
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def home(request):
   return render(request, 'home.html')

def addcontact(request):
   if request.method=="POST":
        a=request.POST.get('name','')
        b = request.POST.get('number','')
        c= request.POST.get('relation','')
        dataset=Contact.objects.all()
        obj=Sinlink()
        for i in dataset:
           obj.add_node(i.name, i.number, i.relation)
        k=obj.contains(a,b,c)
        if k[0]:
           d=k[1]
           data_to_display = "This number is already saved in contacts as"
           return render(request, 'addcontact.html', {'data_to_display': data_to_display, 'd': d})
        else:
           her= Contact(name= a, number=b, relation=c)
           her.save()
           data_to_display="CONTACT HAS BEEN SAVED SUCCESSFULLY..."
           return render(request, 'addcontact.html', {'data_to_display': data_to_display})
   return render(request, 'addcontact.html')

 
def dltcontact(request):
   if request.method=="POST" and request.POST.get("form_identifier")=="form1":
      a=request.POST.get('valuee','')
      dataset=Contact.objects.all()
      obj=Sinlink()
      for i in dataset:
         obj.add_node(i.name, i.number, i.relation)
      n=obj.search(a)
      if n:
         delete=True
         return render(request, 'dltcontact.html', {'contact_info': n, 'delete': delete}) 
      else:
         note="OOPS...NO CONTACT FOUND TO DELETE..."
         return render(request, 'dltcontact.html', {'note': note})
      
   if request.method=="POST" and request.POST.get("form_identifier")=="form2":
      original = request.POST.get('original', '')
      dataset=Contact.objects.all()
      obj=Sinlink()
      for i in dataset:
         obj.add_node(i.name, i.number, i.relation)
      n=obj.search(original)
      Contact.objects.filter(name=n[0]).delete()
      note = "CONTACT HAS BEEN DELETED SUCCESSFULLY..."
      return render(request, 'dltcontact.html', {'note': note})
   

   return render(request, 'dltcontact.html')

def search(request):
   
   if request.method=="POST" and request.POST.get("form_identifier")=="form1":
        a=request.POST.get('valuee','')
        dataset=Contact.objects.all()
        obj=Sinlink()
        for i in dataset:
           obj.add_node(i.name, i.number, i.relation)
        m=obj.search(a)
        if m:
           modify= True
           return render(request, 'search.html', {'contact_info': m, 'modify': modify})     
        else:
           note="NO CONTACT FOUND"
           return render(request, 'search.html', {'note': note})
   
   elif request.method=="POST" and request.POST.get("form_identifier")=="form2":
      p=request.POST.get('newname','')
      q= request.POST.get('newnumber','')
      r = request.POST.get('newrelation','')
      original = request.POST.get('original', '') 
      try:
         record = Contact.objects.get(name=original)
         record.name = p
         record.number = q
         record.relation = r
         record.save()
         j = "Contact has been modified successfully!!!"
         return render(request, 'search.html', {'j': j})
      except Contact.DoesNotExist:
        declaimer ="No fucking Operation"
        return render(request, 'search.html', {'declaimer': declaimer})

      
   return render(request, 'search.html')
   

        
           
         
        
   

def modify(request):
   if request.method=="POST":
        a=request.POST.get('newname','')
        b = request.POST.get('newnumber','')
        c= request.POST.get('newrelation','')
        dataset=Contact.objects.all()
        obj=Sinlink()
        for i in dataset:
           obj.add_node(i.name, i.number, i.relation)
        mod=obj.modify(a,b,c)
        try:
           data = Contact.objects.get(Q(name=mod[0]) | Q(number=mod[1]))
           if data and mod:
              data.name = mod[0]
              data.number = mod[1]
              data.relation = mod[2]
              data.save()
              c = "Contact has been modified successfully!!!"
              return render(request, 'modify.html', {'c': c})
           
        except ObjectDoesNotExist:
           return render(request, 'modify.html', {'message': "Oops...Contact not found to modify!!!"})
   return render(request, 'modify.html')

def contactlist(request):
   if request.method=="POST":
      dataset=Contact.objects.all()
      count= True
      return render(request, 'contactlist.html', {'dataset': dataset, 'count': count})
      

   return render(request, 'contactlist.html')
 


# Create your views here.
