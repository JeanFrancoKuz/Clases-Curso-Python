# match-case es una estructura de control que permite hacer coincidencias de patrones

def match_case_example(value):
    match value:
        case 1:
            return "El valor es uno"
        case 2:
            return "El valor es dos"
        case 3:
            return "El valor es tres"
        case _:
            return "El valor no es ni uno, ni dos, ni tres" 
        
        