import datetime


def dia_de_la_semana():
    dia = datetime.datetime.today().weekday() + 1

    if dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miércoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sábado"
    elif dia == 7:
        return "Domingo"
