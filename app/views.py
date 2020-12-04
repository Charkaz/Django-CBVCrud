from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse,Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .serializers import KitabSerializer


#############################
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import KitabSerializer
from .models import Kitab

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

###############################3


from django.views.generic.edit import FormView
from .models import Kitab
from .forms import kitabQeydView

class KitabListView(ListView):
    model = Kitab
    paginate_by = 10
    def get_queryset(self, *args, **kwargs): 
        qs = super(KitabListView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
        return qs
    def get_context_data(self,*args,**kwargs):
        context = super(KitabListView,self).get_context_data(*args,**kwargs)
        context['sistem'] = "Alisan"
        return context

class KitabDetailView(DetailView):
    model = Kitab



class KitabCreateView(CreateView):
    def get(self,request,*args,**kwargs):
        context = {'form':kitabQeydView()}
        return render(request,'book-create.html',context = context)

    def post(self, request, *args, **kwargs):
        form = kitabQeydView(request.POST,request.FILES)
        if form.is_valid():
            #print(repr(KitabSerializer()))
            book = form.save()
            return HttpResponseRedirect(reverse_lazy('book-detail', args=[book.slug]))
        return render(request, 'book-create.html', {'form': form})


class KitabDeleteView(DeleteView):
    model = Kitab
    success_url = reverse_lazy('index')


class KitabUpdateView(UpdateView):
    model = Kitab
    template_name = 'book-update.html'
    #fields = ['kitab_ad','kitab_janr','kitab_onsoz','kitab_seh','kitab_yazar','stokda','sekil']
    form_class = kitabQeydView
    success_url = reverse_lazy('index')


@api_view(['GET', 'POST'])
def kitab_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Kitab.objects.all()
        serializer = KitabSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KitabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def kitab_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        kitab = Kitab.objects.get(pk=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KitabSerializer(kitab)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KitabSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kitab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)