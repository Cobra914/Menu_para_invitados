menu = {
    "- Aperitivo: Guacamole.": ["cilantro fresco",
                                "cebolla",
                                "chile fresco",
                                "ajo",
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
                                                       "ajo",
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

def lista_ingredientes(menu):
    """
    Recibe el menú.
    Devuelve la lista de ingredientes necesarios que hay que comprar para
    la elaboración de cada plato.
    """
    lista = []
    index_plato = 1

    for plato in menu:
        # print(plato)
        for ingrediente in menu[plato]:
            if ingrediente not in lista:
                lista.append(ingrediente)
        
    return lista

print(lista_ingredientes(menu))