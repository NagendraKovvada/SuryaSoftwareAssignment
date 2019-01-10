from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import * 


class ClientView(TemplateView):
	template_name = 'client.html'

	def get_context_data(self,**kwargs):
		query = Client.objects.all()		
		context={'form':query}
		return context

class ExpenseView(TemplateView):
	template_name = 'expense.html'

	def get_context_data(request,id=None):				
		query = Expense.objects.filter(client=id)		
		context={'form':query}
		return context