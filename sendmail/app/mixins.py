from django.shortcuts import render

class ObjectMixins:
    model = None 
    template = None
    def get(self, request):
        object=self.model.objects.all()
        print(self.model.__name__.lower())  
        return render(request, self.template, {self.model.__name__.lower():object} )