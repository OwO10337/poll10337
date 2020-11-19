from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import *

# Create your views here.
# def poll_list(req):
#   polls = models.Poll.objects.all()
#   return render(req, 'poll_list.html', {'polls_list': polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll 

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        options = Option.objects.filter(poll_id=self. kwargs['pk'])
        print(options)
        ctx['option_list'] = options 
        return ctx 

class PollVote(RedirectView):
    def get_redirect_url(self, * args, ** kwargs):
        option = Option.objects. get(id=self. kwargs['oid'])
        option.count += 1 
        option.save()
        return '/poll/{}/'.format(option.poll_id)
       # return '/poll/'+str(option.poll_id)+'/'

class PollCreate(CreateView):
    model = Poll
    fields = ['subject', 'description']
    success_url = '/poll/'

class PollEdit(UpdateView):
    model = Poll
    fields = '__all__'
    success_url = '/poll/'
class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'

