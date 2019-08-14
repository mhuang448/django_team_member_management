from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import TeamMember
from django.views import generic
from django.urls import reverse

class IndexView(generic.ListView):
    template_name = 'team/index.html'
    context_object_name = 'team_member_list'

    def get_queryset(self):
    # Return the last five published questions (not including those set to be
    # published in the future).
        return TeamMember.objects.all().order_by('id')

class DetailView(generic.DetailView):
    model = TeamMember
    template_name = 'team/detail.html'
    context_object_name = 'member'

def add(request):
    member = TeamMember()
    return render(request, 'team/add.html', {'member' : member})

#actually handles the data inputted in the form in the add viewpage
def addEdit(request):
        member = TeamMember()
        member.first_name = request.POST['first_name']
        member.last_name = request.POST['last_name']
        member.email = request.POST['email']
        member.phone_number = request.POST['phone_number']
        if request.POST['admin_status'] == '1':
            member.admin_status = False
        else:
            member.admin_status = True
        member.save()
        return HttpResponseRedirect(reverse('team:index'))

class EditView(generic.DetailView):
    model = TeamMember
    template_name = 'team/edit.html'
    context_object_name = 'member'

#actually handles the data inputted in the form in the member edit page
def memberEdit(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    member.first_name = request.POST['first_name']
    member.last_name = request.POST['last_name']
    member.email = request.POST['email']
    member.phone_number = request.POST['phone_number']
    if request.POST['admin_status'] == '1':
        member.admin_status = False
    else:
        member.admin_status = True
    member.save()
    return HttpResponseRedirect(reverse('team:index'))

def delete(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    member.delete()
    return HttpResponseRedirect(reverse('team:index'))


# def edit(request, member_id):





# Create your views here.
