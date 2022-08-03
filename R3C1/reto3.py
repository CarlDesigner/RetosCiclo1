#Solucion reto 3 ↓
def AutoPartes(ventas:list):
    diccionario = {}
    for i in ventas:
        if diccionario.get(i[0]) == None:
            diccionario[i[0]] = []
        diccionario[i[0]].append((i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    #print(ventas)
    return diccionario    
    
def consultaRegistro(ventas, idProducto):
    if idProducto in ventas:
        for j in ventas[idProducto]:
            print(f'Producto consultado : {idProducto}  Descripción  {j[0]}  #Parte  {j[1]}  Cantidad vendida  {j[2]}  Stock  {j[3]}  Comprador {j[4]}  Documento  {j[5]}  Fecha Venta  {j[6]} ')      
    else:
        print('No hay registro de venta de ese producto')
        
#Producto consultado : {idProducto} Descripción {dProducto}
#Parte {pnProducto} Cantidad vendida {cvProducto} Stock
#{sProducto}  Comprador  {nComprador}  Documento
#{cComprador} Fecha Venta {fVenta}

ventas = [ 
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'), 
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'), 
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),     
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'), 
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020'),
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')
    ]

print()