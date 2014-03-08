from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext
from django.template import Context, Template
from django.http import HttpResponse
from models import  Prof, Cours, descriptif, Programme, authentification
# Create your views here.

#-*- coding: utf-8 -*-

def accueil(request):
    t = get_template('accueil.html')
    return HttpResponse(t.render(Context()))
   # t = """<head> <title>Page d'accueil </title> </head>
    #        <p> Je dois remettre tout ca ce jeudi. </p>
     #   """
    #return HttpResponse(t)
def InterfaceProf(request):
    t = get_template('InterfaceProf.html')
    return HttpResponse(t.render(Context()))

def FormulaireLoginAdmin(request):
    page=get_template('connexion_administrateur\connexionadministrateur.html')
    html = page.render(Context({}))
    return HttpResponse(html)


def FormulaireLoginProf(request):
    page1=get_template('connexion_professeur\connexionprofesseur.html')
    html = page1.render(Context({}))
    return HttpResponse(html)

def FormulaireCompteProf(request):
    page2=get_template('connexion_professeur\Fiches_des_professeurs.html')
    html = page2.render(Context({}))
    return HttpResponse(html)

def EnregistrerProfesseur(request):
    t= get_template('Fiches_des_professeurs.html')
    return HttpResponse(t.render(Context()))

def EnregistrerProfesseur(request):
    ProfNew = Prof(
        nom_prof = request.GET['nom_prof'],
        prenom_prof = request.GET['prenom_prof'],
        profession = request.GET['profession'],
        matiere_enseignee = request.GET['matiere_enseignee'],
        user = request.GET['user'],
        password = request.GET['password']
    )
    ProfNew.save()
    page2=get_template('connexion_professeur\Fiches_des_professeurs.html')
    html = page2.render(Context({}))
#    Prof(nom_prof=nom_prof, prenom_prof =prenom_prof, profession=profession, matiere_enseignee=matiere_enseignee, user=user, password=password).save()
    #return HttpResponse(request,'connexion_professeur\Fiche_des_professeurs.html',locals())
    return HttpResponse(html)

#def login(request):
 #   m = EnregistrerProfesseur().objects.get(username=request.GET['username'])
  #  if m.password == request.GET['password']:
   #     request.session['id'] = m.id
    #    return HttpResponse("You're logged in.")
    #else:
     #   return HttpResponse("Your username and password didn't match.")

    #request render(request,'ProfLogin.html',locals())
    #page2=get_template('connexion_professeur\ProfLogin.html')
    #html = page2.render(Context({}))
    #return HttpResponse(html)

# def CoursSauvegarde(request):
#     t= get_template('Creation_de_cours.html')
#     return HttpResponse(t.render(Context()))

def CoursSauvegarde(request):
    try:
        Ok = Cours(nom_cours  = request.GET['nom_cours'],ressources = request.GET['ressources'],credits = request.GET['credits'])
        Ok.save()
        page2=get_template('connexion_professeur\Creation_de_cours.html')
        html = page2.render(Context({}))
        return HttpResponse(html)
    except:
        page2=get_template('connexion_professeur\Creation_de_cours.html')
        html = page2.render(Context({}))
        return HttpResponse(html)


def coursdescriptif(request):
    try:
        Ok1 = descriptif(code  = request.GET['code'],Titre = request.GET['Titre'],Credits = request.GET['Credits'], LieuEnseignement = request.GET['LieuEnseignement'],gradesemestre = request.GET['gradesemestre'])
        Ok1.save()
        page2=get_template('connexion_professeur\descriptifcours.html')
        html = page2.render(Context({}))
        return HttpResponse(html)
    except:
        page2=get_template('connexion_professeur\descriptifcours.html')
        html = page2.render(Context({}))
        return HttpResponse(html)

def FormProg(request):
    try:
        Ok1 = Programme(domaine  = request.GET['domaine'], mention = request.GET['mention'],specialite = request.GET['specialite'], langue = request.GET['langue'], niveau = request.GET['niveau'])
        Ok1.save()
        page2=get_template('connexion_professeur\programme.html')
        html = page2.render(Context({}))
        return HttpResponse(html)
    except:
        page2=get_template('connexion_professeur\programme.html')
        html = page2.render(Context({}))
        return HttpResponse(html)

def lcours(request):
    # if 'richid' not in request.session:
    #     return redirect('/web/')
    try:
        l=Cours.objects.all()
        return render(request,'connexion_professeur\lcours.html',locals())
    except:
        return render(request,'connexion_professeur\lcours.html',locals())

def lprogramme(request):
    # if 'richid' not in request.session:
    #     return redirect('/web/')
    try:
        l1=Programme.objects.all()
        return render(request,'connexion_professeur\lprogramme.html',locals())
    except:
        return render(request,'connexion_professeur\lprogramme.html',locals())

def ldescriptif(request):
    # if 'richid' not in request.session:
    #     return redirect('/web/')
    try:
        l2=descriptif.objects.all()
        return render(request,'connexion_professeur\ldescriptif.html',locals())
    except:
        return render(request,'connexion_professeur\ldescriptif.html',locals())

def lprofesseur(request):
    # if 'richid' not in request.session:
    #     return redirect('/web/')
    try:
        l3=Prof.objects.all()
        return render(request,'connexion_professeur\lprofesseur.html',locals())
    except:
        return render(request,'connexion_professeur\lprofesseur.html',locals())

def web (request):
    try:
        try:

            ina = authentification.objects.get(user=request.GET['user'])
            inn = authentification.objects.get(password=request.GET['password'])
            if ina.password==request.GET['password']and inn.user==request.GET['user']:
                request.session['richid']=ina.id
                return redirect("/../")
            else:
                return HttpResponse("bad")
        except:
            return render(request,'connexion_professeur\connexionprofesseur.html',locals())
    except:
        return render(request,'connexion_professeur\connexionprofesseur.html',locals())

def login(request):
    return HttpResponse('hbuhbubu')
    try:
        if 'user' in request.GET:
            verification = Prof.objects.get(user=request.GET('user'))
            if verification.password == request.GET['password']:
                request.session['user'] = request.GET['user']
                return redirect('connexion_professeur\ProfLogin.html')
            else:
                pass
        else:
            return HttpResponse('hbuhbubu')
        return render(request,'ProfLogin.html',locals())
    except KeyError:
        pass
        return render(request,'ProfLogin.html',locals())



