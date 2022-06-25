from django.shortcuts import render
DATA = {
    'omlet': {
    'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'blini': {
        'мука, г': 200,
        'яйца, шт': 2,
        'масло, г': 10,
        'молоко, мл': 400,
    }
}

def recipe(request, food):
    context = {
        "recipe": {},
    }
    koef = int(request.GET.get("serving",1))
    if food in DATA:
        for keys,values in DATA[food].items():
            DATA[food][keys] = values * koef
        context['recipe'] = DATA[food]
    return render(request, 'calculator/index.html', context)


