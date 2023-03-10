import bluetooth

# Encuentra todos los dispositivos Bluetooth cercanos
nearby_devices = bluetooth.discover_devices()

# Imprime la lista de dispositivos cercanos
for bdaddr in nearby_devices:
    print(bluetooth.lookup_name(bdaddr), " [", bdaddr, "]")

# Direcciones MAC de los auriculares que deseas conectar
mac_addr1 = 'XX:XX:XX:XX:XX:XX' # Dirección MAC del primer auricular
mac_addr2 = 'YY:YY:YY:YY:YY:YY' # Dirección MAC del segundo auricular

# Conecta el primer auricular
sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock1.connect((mac_addr1, 1))

# Conecta el segundo auricular
sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock2.connect((mac_addr2, 1))

# Fusiona los auriculares
sock1.send(b"\x01\x00")
sock2.send(b"\x01\x01")

# Instalar "Pydroid 3" desde "Google Play Store". En iOS, "Pythonista 3" desde "App Store".
# Reemplazar las direcciones MAC de los auriculares por las direcciones MAC de los auriculares Xiaomi Mi True Wireless Earbuds Basic 2.
# Es posible que se deba otorgar permisos a la app para acceder a la interfaz Bluetooth del dispositivo móvil antes de poder ejecutar el código.
