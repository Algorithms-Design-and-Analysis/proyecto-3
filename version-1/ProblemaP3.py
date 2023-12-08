# Sergio Franco Pineda (202116614), Lina María Ojeda Amaya (202112324), Germán Alberto Rojas Cetina (202013415) 

class ProblemaP3:
    #Donantes de la mayor donacion
    donors=set()

    #Mayor donacion realizada
    highest_donation=0
    #Dinero que tiene cada una de las personas
    donors_money=[]

    #Conocidos que tiene cada persona. La llave es un numero y el valor es un set con los conocidos
    knowns={}

    def maximum_donation():
        for i in range(1,len(ProblemaP3.donors_money)):
            #Lista de conocidos de la persona i
            current_knowns=ProblemaP3.knowns[i]
            #Dinero maximo actual
            current_money=ProblemaP3.donors_money[i]
            #Donador actual
            current_donors={i}

            #Por cada conocido de la persona i
            for known in current_knowns:

                current_money=ProblemaP3.donors_money[i]
                current_donors={i}

                #Conocidos 
                neighbor_knowns=ProblemaP3.knowns[known]

                #Se revisa que se conozcan mutuamente
                if i in neighbor_knowns:
                    current_donors.add(known)
                    current_money+=ProblemaP3.donors_money[known]

                #Por cada conocido de la persona i
                for known2 in current_knowns:
                    counter=0
                    if known2 != known:
                        neighbors_known2=ProblemaP3.knowns[known2]
                        
                        for connected_known in current_donors:
                            if neighbors_known2.__contains__(connected_known):
                                counter+=1
                            else:
                                break
                        if counter==len(current_donors):
                            current_donors.add(known2)
                            current_money+= ProblemaP3.donors_money[known2]

                if current_money> ProblemaP3.highest_donation:
                    ProblemaP3.highest_donation=current_money
                    ProblemaP3.donors=current_donors

        print(f"{ProblemaP3.highest_donation} {' '.join(map(str, ProblemaP3.donors))}")


if __name__ == "__main__":
    casos = int(input())

    for _ in range(casos):
        linea = input().split()
        ProblemaP3.donors_money = [0] + [int(x) for x in linea]
        ProblemaP3.knowns = {}

        for i in range(1, len(linea) + 1):
            conocidos_linea = input().split()
            conocidos_actuales = {int(x) for x in conocidos_linea}
            ProblemaP3.knowns[i] = conocidos_actuales

        ProblemaP3.maximum_donation()
        # Modificacion variables
        ProblemaP3.highest_donation = 0
        ProblemaP3.donors = set()