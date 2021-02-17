from prettytable import PrettyTable


def get_horario(dia=None):
    horario = PrettyTable()

    horario.add_column("Hora",
                       ["08:00-10:00",
                        "10:00-12:00",
                        "12:00-14:00",
                        "14:00-15:00"])

    horario.add_column("Lunes",
                       ["Matemáticas",
                        "Electrónica",
                        "ADSOII",
                        "---"])

    horario.add_column("Martes",
                       ["---",
                        "Empresa",
                        "Programación",
                        "ADSOII"])

    horario.add_column("Miércoles",
                       ["Empresa",
                        "GCHP",
                        "Activids.",
                        "---"])

    horario.add_column("Jueves",
                       ["---",
                        "Historia",
                        "Matemáticas",
                        "ADSOII"])

    horario.add_column("Viernes",
                       ["---",
                        "Electrónica",
                        "Programación",
                        "---"])

    if(dia):
        return (horario.get_string(fields=["Hora", dia]))
    else:
        return(horario.get_string())
