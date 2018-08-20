import os, os.path, sys
fh = open("names.txt", "w")
fh.write('fem = ["fem" ')
path= "C:\\Users\\YOSHIBOO\\Documents\\GitHub\\Kyogokudo.github.io\\img\\fem"
##for path, dirs, files in os.walk(path):
##    for file in files:
##        if file.endswith('.png'):
##            fh.write(', "')
##            nom=file
##            os.path.splitext(nom)[0]
##            fh.write(nom)
##            fh.write('" ')
files = os.listdir('.')
for x in files:
    fh.write(', "')
    files = [os.path.splitext(x)[0]]
    nom=files.pop()
    fh.write(nom)
    fh.write('" ')
fh.close()
print ("fin")
