from django.shortcuts import render,HttpResponseRedirect,reverse,HttpResponse,Http404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy



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