menu = {
    "- Aperitivo: Guacamole.": ["cilantro fresco",
                                "cebolla",
                                "chile fresco",
                                "diente de ajo",
                                "tomate",
                                "aguacate maduros",
                                "zumo de limón",
                                "sal"],
    "- Primer plato: Pimientos del piquillo rellenos.": ["huevo",
                                                         "palitos de cangrejo",
                                                         "atun en aceite de oliva",
                                                         "mayonesa",
                                                         "pimientos del piquillo",
                                                         "pimiento verde",
                                                         "pimiento rojo",
                                                         "cebolla",
                                                         "vinagre de vino",
                                                         "sal",
                                                         "aceite de oliva"],

    "- Segundo plato: Solomillo de cerdo agridulce.": ["aceite de oliva",
                                                       "diente de ajo",
                                                       "solomillo de cerdo",
                                                       "cebolla",
                                                       "manzana",
                                                       "tomate concentrado",
                                                       "calabacines en espirales",
                                                       "brandy",
                                                       "vino oporto",
                                                       "ciruelas pasas sin hueso",
                                                       "orejones de albaricoque",
                                                       "mostaza",
                                                       "piñones tostados"],

    "- Postre: Brownie de chocolate con helado de turrón.": ["chocolate amargo 70porciento cacao",
                                                             "mantequilla sin sal",
                                                             "azúcar",
                                                             "huevo",
                                                             "sal",
                                                             "harina de trigo",
                                                             "nueces"],
}

cantidades_gramos_unid = {
    "cilantro fresco": 5,
    "cebolla": 100,
    "chile fresco": 1,
    "diente de ajo": 1,
    "tomate": 120,
    "aguacate maduros": 450,
    "zumo de limón": 1,
    "sal": 1,
    "huevo": 1,
    "palitos de cangrejo": 100,
    "atun en aceite de oliva": 150,
    "mayonesa": 50,
    "pimientos del piquillo": 12,
    "pimiento verde": 50,
    "pimiento rojo": 50,
    "cebolla": 50,
    "vinagre de vino": 25,
    "sal": 0.5,
    "aceite de oliva": 50,
    "aceite de oliva": 60,
    "diente de ajo": 3,
    "solomillo de cerdo": 500,
    "cebolla": 150,
    "manzana": 1,
    "tomate concentrado": 1,
    "calabacines en espirales": 600,
    "brandy": 30,
    "vino oporto": 100,
    "ciruelas pasas sin hueso": 30,
    "orejones de albaricoque": 30,
    "mostaza": 1,
    "piñones tostados": 2,
    "chocolate amargo 70porciento cacao": 250,
    "mantequilla sin sal": 220,
    "azúcar": 380,
    "huevo": 6,
    "sal": 1,
    "harina de trigo": 150,
    "nueces":150,
}


def lista_ingredientes(menu):
    """
    Recibe el menú.
    Devuelve la lista de ingredientes necesarios que hay que comprar para
    la elaboración de cada plato.
    """
    nueva_lista = []
    
    for plato in menu:
        for ingrediente in menu[plato]:
            if ingrediente not in nueva_lista:
                nueva_lista.append(ingrediente)
        
    return nueva_lista

print(lista_ingredientes(menu))