from django.shortcuts import render

# Create your views here.
def view1(request):
	name="rama"
	place="mysore"
	c={'Name':name,'Place':place}
	return render(request,'htmlpages/2.html',c)