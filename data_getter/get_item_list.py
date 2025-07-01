

def get_player_list(nfiles, path):
    files = path + "table_data_{}.txt"
    names=[]

    for nf in range(1,nfiles,1):
        file_name = files.format(nf)

        f=open(file_name,"r")
        lines=f.readlines()
        
        for x in lines:
            item = x.split('\t')[5]
            names.append(item.strip())
        f.close()


    names_set = set(names)
    names_list = list(names_set)

    with open("./data/player_list_check.txt", 'w') as myfile:
        for ply in names_list:
            myfile.write(ply + "\n")

    return names_list
