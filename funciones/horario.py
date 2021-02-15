from prettytable import PrettyTable 
  
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
     "Empresa y Proced.",
     "Programación",
     "ADSOII" ]) 
  
horario.add_column("Miércoles",
    ["Empresa y Proced.",
     "GCHP",
     "Actividades UFV",
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

return(horario)
