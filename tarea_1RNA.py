
import mnist_loader
import network
import pickle


training_data, validation_data , test_data = mnist_loader.load_data_wrapper() #introducimos las imagenes de mnist como nuestros datos de prueba

training_data = list(training_data) #hacemos que nuestros datos de entrenamiento tengan forma de lista 
test_data = list(test_data) #lo mismo que el paso anterior pero con los datos de prueba

# Creamos un objeto del tipo Network 
estruc = [784,30,10]
network =network.Network([784,30,10])

# Llamemos a la funcion SGD para configurar y entrenar la red
network.SGD(training_data, 30, 30, 3.0, test_data=test_data)



#archivo = open("red_prueba1.pkl",'wb')
#pickle.dump(net,archivo)
#archivo.close()
#exit()

#leer el archivo
#rchivo_lectura = open("red_prueba1.pkl",'rb')
#et = pickle.load( archivo_lectura)
#rchivo_lectura.close()
#rchivo = open("red_prueba1.pkl",'wb')
#ickle.dump(net,archivo)
#rchivo.close()
#xit()e
