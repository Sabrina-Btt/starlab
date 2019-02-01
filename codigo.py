file1 = open("/home/sabrina/star_project/table2.dat","r")
file2 = open("/home/sabrina/star_project/dados.txt" ,"w")
file2.write("Hd/Dm"+ "    " + "SMW")
file2.write("\n")
for linha in file1:
    HDDM= linha[19:27]
    SMW= linha[76:81]
    file2.write(HDDM + "  " + SMW)
    file2.write("\n")
#esta é a segunda modificação
file2.close
file1.close



