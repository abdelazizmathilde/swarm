def display_status_swarm_robot(id):

    print("-------------------------------------------\n")
    print("--------------- State of Swarm"+ str(id)+" ------------------\n")



def display_data_swarm(table,id):
    print("-------------------------------------------\n")
    print("--------------- Data of Swarm "+str(id)+" ------------------\n")
    for i in range(len(table)):
        print(table[i]+"\n")
    print("-------------------------------------------\n")
