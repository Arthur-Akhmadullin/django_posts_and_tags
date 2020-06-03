from django.shortcuts import render

def posts_list(request):
	msg_hello = ["Здорово, бакланы!", "Превед медвед!", "Смешарики, в бой!!!"]
	return render(request, 'pt/index.html', {"messages": msg_hello})
	
	
