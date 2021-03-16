from django.shortcuts import render
from .filter import OrderFilter
from .forms import Grocery_BagForm
from .models import Grocery_Bag


# Create your views here.
def Dashboard(request):
    stu = Grocery_Bag.objects.all()
    My_filter = OrderFilter()

    return render(request, 'dashboard.html', {'stu': stu,'My_filter':My_filter})


def Dashboard1(request):
    stu = Grocery_Bag.objects.all()
    print(stu)
    return render(request, 'first.html', {'stu': stu})


def delete_Grocery_Bag(request, pk):
    st = Grocery_Bag.objects.get(id=pk)
    if request.method == "POST":
        st.delete()
        print(st)
    context = {'item': st}
    return render(request, 'delete.html', context)


def update_Employee(request, pk):
    stu = Grocery_Bag.objects.get(id=pk)
    form = Grocery_BagForm(instance=stu)
    if request.method == 'POST':
        form = Grocery_BagForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'update.html', context)


def customer(request):
    Grocery = Grocery_Bag.objects.get()
    My_filter=OrderFilter()


    context = {'customer': Grocery,'My_filter':My_filter}
    return render(request, 'search.html', context)

def delete_Employee(request, pk):
    st = Grocery_Bag.objects.get(id=pk)
    if request.method == "POST":
        st.delete()
        print(st)
    context = {'item': st}
    return render(request, 'delete.html', context)
def feed(request):
    form = Grocery_BagForm()
    if request.method == 'POST':
        form = Grocery_BagForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'list.html', context)
