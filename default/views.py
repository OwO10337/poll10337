from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView

# Create your views here.
# def poll_list(req):
#   polls = models.Poll.objects.all()
#   return render(req, 'poll_list.html', {'polls_list': polls})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll 

    def get_context_date(self, **kwargs):
        ctx = super().get_context_data(**kwagrs)
        options = Option.objects.filter(poll_id=self. kwargs['pk'])
        ctx['option_list'] = options 
        return ctx 

class PollVote(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects. get(id=self. kwargs['old'])
        option.count += 1 
        option.save()
        return '/poll/{}/'.format(option.poll id)
       # return '/poll/'+str(option.poll_id)+'/'
