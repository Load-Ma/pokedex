from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import Poke


def getAllPokemon(request):
    result = []
    pokemon_count = 152

    colors = {
        "fire": '#FDDFDF',
        "grass": '#DEFDE0',
        "electric": '#FCF7DE',
        "water": '#DEF3FD',
        "ground": '#f4e7da',
        "rock": '#d5d5d4',
        "fairy": '#fceaff',
        "poison": '#98d7a5',
        "bug": '#f8d5a3',
        "dragon": '#97b3e6',
        "psychic": '#eaeda1',
        "flying": '#F5F5F5',
        "fighting": '#E6E0D4',
        "normal": '#F5F5F5',
        "ice": '#94dfff',
        "ghost": '#d48aeb'
    }

    for i in range(1, pokemon_count):
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json()
        print(getPokemonType(res))
        result.append({
            "id": i,
            "name": getPokemonName(i),
            "img": getImage(res),
            "type" : getPokemonType(res),
            "color": colors[getPokemonType(res)]
        })

    context = {
        'pokemons': result,
    }
    return render(request, 'accueil.html', context)


def getPokemon(request, number):
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{number}").json()
    pokemon = {
        'name': getPokemonName(number),
        'images': getImage(res),
        'abilities': getPokemonAbilities(res),
        'stats': getPokemonStats(res),
    }
    context = {
        'pokemon': pokemon,
        'nextPokemon': nextPokemon(number),
        'previousPokemon': previousPokemon(number),
        'team': getTeam(),
    }
    return render(request, 'index.html', context)


def getPokemonName(number):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{number}').json()
    name = ""
    for item in res['names']:
        if item['language']['name'] == 'fr':
            name = item['name']
            break
    return name


def getPokemonAbilities(pokemon):
    retour = {
        'first': pokemon['abilities'][0]['ability']['name'],
        'second': ""
    }
    if pokemon['abilities'][-1]['ability']['name'] == pokemon['abilities'][0]['ability']['name']:
        retour.update({'second': ""})
    else:
        retour.update({'second': pokemon['abilities'][1]['ability']['name']})
    return retour


def getPokemonType(pokemon):

    return  pokemon['types'][0]['type']['name']



def getPokemonStats(pokemon):
    retour = {
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'sa': pokemon['stats'][3]['base_stat'],
        'sd': pokemon['stats'][4]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'type1': pokemon['types'][0]['type']['name'],
        'type2': ''
    }

    if pokemon['types'][-1]['type']['name'] == pokemon['types'][0]['type']['name']:
        retour.update({'type2': ""})
    else:
        retour.update({'type2': pokemon['types'][1]['type']['name']})

    return retour


def getImage(pokemon):
    return {
        'back_default': pokemon['sprites']['back_default'],
        'back_shiny': pokemon['sprites']['back_shiny'],
        'front_default': pokemon['sprites']['front_default'],
        'front_shiny': pokemon['sprites']['front_shiny'],
    }


def getPokemonPick(pokemon, default):
    if default:
        return pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
    else:
        return pokemon['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']


def previousPokemon(number):
    if number - 1 <= 0:
        number = 1
    else:
        number -= 1
    return f"http://127.0.0.1:8000/pokemon/{number}"


def nextPokemon(number):
    if number + 1 >= 251:
        number = 251
    else:
        number += 1
    return f"http://127.0.0.1:8000/pokemon/{number}"


@csrf_exempt
def addPokemon(request):
    if request.method == 'POST':
        pokeid = request.POST.get('pokemonId')
        default = request.POST.get('default')
        if default == "true":
            default = True
        elif default == "false":
            default = False
        if len(Poke.objects.filter(id_pokemon=pokeid)) == 0:
            if Poke.objects.count() <= 6:
                res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokeid}").json()
                img = getPokemonPick(res, default)
                poke = Poke.objects.create(id_pokemon=pokeid, url_pokemon=img)
                poke.save()
                return JsonResponse({"success": True, "img": img, "id": pokeid})
    return JsonResponse({"success": False, "img": None})


@csrf_exempt
def removePokemon(request):
    if request.method == 'POST':
        pokeid = request.POST.get('pokemonId')
        if len(Poke.objects.filter(id_pokemon=pokeid)) > 0:
            Poke.objects.filter(id_pokemon=pokeid).delete()
            return JsonResponse({"success": True, "id": pokeid})
        else:
            return JsonResponse({"success": False})


def getTeam():
    p = Poke.objects.all()
    mate = {
        "mate1": "",
        "mate2": "",
        "mate3": "",
        "mate4": "",
        "mate5": "",
        "mate6": "",
    }
    for i in range(6):
        try:
            mate.update({f"mate{i+1}": {
                "url": p[i].url_pokemon,
                "id": p[i].id_pokemon
            }})
        except:
            mate.update({f"mate{i+1}": ""})
    return mate
