
import mnist.pkl
import network
import pickle


training_data, validation_data , test_data = mnist.pkl.load_data_wrapper() #introducimos las imagenes de mnist como nuestros datos de prueba

training_data = list(training_data) #hacemos que nuestros datos de entrenamiento tengan forma de lista 
test_data = list(test_data) #lo mismo que el paso anterior pero con los datos de prueba
net=network.Network([256,10,10])

#archivo = open("red_prueba1.pkl",'wb')
#pickle.dump(net,archivo)
#archivo.close()
#exit()

#leer el archivo
archivo_lectura = open("red_prueba1.pkl",'rb')
net = pickle.load( archivo_lectura)
archivo_lectura.close()
archivo = open("red_prueba1.pkl",'wb')
pickle.dump(net,archivo)
archivo.close()
exit()
