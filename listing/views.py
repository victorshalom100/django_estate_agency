from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Properties
from accounts.models import Users

# Create your views here.
def categories(request):
    houses = Properties.objects.order_by('-list_date')
    
    context = {
        'properties' : houses
    }
    
    return render(request, 'listing/categories.html', context)


def agents(request):
    agents = Users.objects.order_by('-reg_date').filter(is_superuser=False)
    
    context = {
        'agents' : agents
    }
    
    return render(request, 'listing/agents.html', context)



@login_required(login_url='login')

#this is collecting the name of input field in html nd saving in a variable
def createPost(request):
    name = request.POST['name'] 
    location = request.POST['location']
    type = request.POST['type']
    status = request.POST['status']
    area = request.POST['area']
    bed = request.POST['bed']
    bath = request.POST['bath']
    garage = request.POST['garage']
    desc = request.POST['desc']
    price = request.POST['price']
    photo = request.FILES.get('file')
    price = request.POST['price']
    agent_id = request.user

    try:
        items = Properties(agent_id=agent_id, name=name, location=location, ptype=type, status=status, bed=bed, bath=bath, garage=garage, area=area, description=desc, photo=photo, price=price)
        items.save()

        messages.success(request,'Post uploaded successfully')
        return redirect('dashboard')

    except Exception as e:
        print(e)
        messages.error(request, 'Error saving details')
        return redirect('dashboard')

def single(request, agent_id):
    agent = get_object_or_404(Users, pk=agent_id)
    
    houses = Properties.objects.order_by('-list_date').filter(agent_id=agent.id)
    
    context = {
        'agent' : agent,
        'pcount': len(houses),
        'properties' : houses
    }
    
    return render(request, 'listing/agentsingle.html', context)



def findSingle(request, listing_id):
    property = get_object_or_404(Properties, pk=listing_id)
    
    context = {
        'property' : property
    }
    
    return render(request, 'listing/property.html',context)
 