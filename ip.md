## Adversarios, motivaciones del adversario y tipos de ataques


Amenazas comunes

### Instalaciones físicas:

-   Amenazas de Hardware
    
-   “” Ambiente (medidores temperatura, ubicación de baños)
    
-   “” Eléctricas (no tener polo a tierra, supresor de picos)
    
-   “” mantenimiento (no actualizar equipos)
    

  

Ataques de reconocimiento:

Usar software para identificar, IPs MACs (info de la red)

  

Ataques de acceso:

-   Recuperación de datos
    
-   Obtener acceso
    
-   Aumentar los privilegios de acceso (su)

Ataques de contraseña

  
  

HOST A HOST

  

Modelo antiguo

  

Modelo basado en estándares

  
  

## MODELO OSI  

- 7 Aplicacion
FTP
HTTP (hipertexto) port 80
HTTPS (hipertexto) port 443
Socket
Telnet → port 23
DNS → port 
SMTP → port 25 e-mail

- 6 Presentacion


- 5 Sesion


- 4 Transporte
Circuitos virtuales
Protocolos:
	- Orientado a conexion: TCP
	- No orientado a conexion: UDP
PDU segmento
Dispositivos:
	- Firewalls, IDS, IPS, 

- 3 Red
Protocolos de enrutamiento y enrutables
PDU (Protocol data unit)
packages (paquetes)
datagram
Protocolos de enrutamiento → cual es el mejor camino entre un origen y un destino
throughput → medida efectiva puede llegar a ser igual a la capacidad del medio
Protocolo enrutables → lleva la unidad de informacion (ej: ip)
Switch L3 (conmutacion y enrutamiento), Routers

- 2 Enlace de datos
MAC (6 octetos, 3+3, OVI + Admin)
SAP (Service access point)
Switches L2 (VLAN), IEEE 802.1Q, IEEE 802.4, IEEE 802.5 (Token Ring), IEEE 802.11, Access point (AP) concentracion lan, bridge (L2)
MAN → IEEE 802.6
WAN → SDLC y HDLC (protocolo estandar)

- 1 Fisica (electrica y mecanica, funcional, db9, db24)  db9 -> 9 pines
manchester, hubs (repetidores de medio, dividen el ancho de banda) topologias (anillo, estrella, estrella extendida)

> OSI (networking) TCP/IP (física)


## Peer to Peer



## TCP/IP

- 4 Aplicacion (OSI: app, pres sesion)
- 3 Transporte
- 2 Internet (OSI: red)
- 1 Acceso a red (OSI: fisica, data link)






## TCP/IP - datagramas

## Caracteristicas del protocolo de internet
datagram 
5 octetos x 4 = 20 x  
Type of service:
- delay

Longitud del paquete
	- 2^16

Identificación:
Fragmentos

TTL → vigencia de un datagrama en la red
Protocol → 

Direccion IP origen
Direccion IP destino
Opciones (seguimiento, troubleshooting)



## Clases de direccion IP: el primer octeto

A B C 
- Clase A →0 xxxxx Host Host Host 
- Clase B →1 0 xxxxx Red Host  Host 
- Clase A →1 1 0 xxxxx Red Red Host 
> IANA ICAN
