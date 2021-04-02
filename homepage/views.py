from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone



class HomepageView(generic.ListView):
    template_name = 'homepage/homepage.html'

    # In case we define a comportment in the homepage linked with a DATABASE we have to set this function
    def get_queryset(self):
        """

        """
        return

# Vote contain paramaters that link with the question ID
def register(request):
    if request.method == 'GET':
        prenom = request.GET['prenom']
        email =  request.GET['email']
        password = request.GET['password']
        # Vérifie que l'émail n'exite pas.
        # hasher le mot de pass
        # ajouter dans la base de donnée
        # renvoyer un message à l'utilisateur
        return render(request, 'homepage/register.html',{'message':'Merci ' + prenom + ' de vous êtes enregistrer '})
    else:
        return render(request, 'homepage/register.html',{'message':'erreur'})