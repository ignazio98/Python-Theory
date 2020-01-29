"""
FILE

to read a file we use open() , it create a python object and connect the file with 
the object, after this we can read and write on the file.
"""

output = open("C:/Users/damic/OneDrive/Desktop/EsPython/es.txt", "w")
output.write('ciao mi stai leggendo da un file')
output.close()

output = open("C:/Users/damic/OneDrive/Desktop/EsPython/es.txt")
ris = output.read()
print(ris)
output.close()


lines = [
    'prima riga di questo file:\n'
    'seconda'
    'terza'
]

output = open("C:/Users/damic/OneDrive/Desktop/EsPython/es.txt", "w")
output.writelines(lines)
output.close
output = open("C:/Users/damic/OneDrive/Desktop/EsPython/es.txt")
print(output.read())