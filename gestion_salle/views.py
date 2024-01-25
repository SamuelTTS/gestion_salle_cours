from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Salle,Reservation
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def reserver_salle(request):
    if request.method == 'POST':
        salle_id = request.POST.get('salle')
        date_reservation = request.POST.get('date')
        heure_debut = request.POST.get('heure_debut')
        heure_fin = request.POST.get('heure_fin')
        professeur = request.POST.get('professeur')
        matiere = request.POST.get('matiere')

        # Assurez-vous que les valeurs sont valides avant de créer la réservation
        
        salle = Salle.objects.get(pk=salle_id)
        Reservation.objects.create(salle=salle,
                date=date_reservation,
                heure_debut=heure_debut,
                heure_fin=heure_fin,
                professeur=professeur,
                matiere=matiere)

            # Marquer la salle comme non disponible
        salle.disponible = False
        salle.save()

        return HttpResponse("Réservation effectuée avec succès!")
        # else:
        #     return HttpResponse("Erreur: Tous les champs doivent être remplis.")

    # Si la méthode HTTP n'est pas POST, affichez simplement le formulaire
    salles = Salle.objects.filter(disponible=True)
    return render(request, 'reservation.html', {'salles': salles})

def liberer_salle(request):
    result = None

    if request.method == 'POST':
        salle_id = request.POST.get('salle')

        if salle_id :
            salle = get_object_or_404(Salle, id=salle_id)


            reservation_en_cours = Reservation.objects.filter(
                salle=salle,
                terminee=False
            ).first()

            if reservation_en_cours:
                
                reservation_en_cours.terminee = True
                reservation_en_cours.save()

               
                salle.disponible = True
                salle.save()

                result = f"Salle {salle.numero} libérée avec succès!"
            else:
                result = f"Aucune réservation en cours pour la salle {salle.numero} à cette heure."

        else:
            result = "Erreur: Tous les champs doivent être remplis."

    salles_non_disponibles = Salle.objects.filter(disponible=False)

    return render(request, 'liberation.html', {'salles': salles_non_disponibles, 'result': result})


def liste_salles(request):
    salles_disponibles = Salle.objects.all()
    reservations = Reservation.objects.all()
    context = {
        'salles_disponibles': salles_disponibles,
        'reservations': reservations,     
    }

    return render(request, 'liste_salles.html', context)

def new_salles(request):
    return render(request,'ajouter_salles.html')

def acceuil(request):
    return render(request,'acceuil.html')

def ajouter_salle(request):
    if request.method=='POST':

        numero=request.POST.get('numero')
        capacite=request.POST.get('capaciter')
        if Salle.objects.filter(numero=numero).exists():
            messages.error(request, 'Cette salle existe déja.')
            return redirect('new_salles')
        else :
            Salle.objects.create(numero=numero,capacite=capacite)
            messages.success(request, 'salle creer avec succes.')
    
    return redirect('liste_salles')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_salles')
        else:
            messages.error(request, 'username ou mot de passe incorrect.')
    return render(request, 'connexion.html')

def logout1(request):
    logout(request)
    return redirect('login')