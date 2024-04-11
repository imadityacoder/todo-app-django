from django import forms
from .models import Todo


# creating a form
class todoForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Todo

		# specify fields to be used
		fields = [
			"title",
			"desc",
		]
