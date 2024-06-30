from ncclient import manager
from ncclient.operations import RPCError

# Datos de conexión al router CSR1000v
host = '192.168.0.100'  # Dirección IP del router CSR1000v
port = 830  # Puerto SSH
username = 'cisco'  # Nombre de usuario SSH
password = 'cisco123!'  # Contraseña de usuario SSH

# Nuevo nombre del router utilizando el apellido Chavez
new_hostname = 'CSR1000v-Chavez'

# Configuración XML para cambiar el nombre del router
config_hostname = f'''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
    </native>
</config>
'''

# Configuración XML para crear la interfaz loopback 11
config_loopback = '''
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback11</name>
            <description>Interfaz de loopback 11</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>11.11.11.11</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
'''

# Función para conectar al router CSR1000v mediante NETCONF y SSH
def connect_to_device():
    try:
        with manager.connect(
                host=host,
                port=port,
                username=username,
                password=password,
                hostkey_verify=False,
                device_params={'name': 'csr'}
        ) as m:
            print(f"Conexión establecida con éxito a {host} mediante NETCONF sobre SSH")

            # Cambiar el nombre del router
            try:
                result_hostname = m.edit_config(target='running', config=config_hostname)
                print(f"Nombre del router cambiado correctamente a {new_hostname}")
            except RPCError as e:
                print(f"Error al cambiar el nombre del router: {e}")

            # Crear la interfaz loopback 11
            try:
                result_loopback = m.edit_config(target='running', config=config_loopback)
                print("Interfaz loopback 11 creada correctamente.")
            except RPCError as e:
                print(f"Error al crear la interfaz loopback: {e}")

    except Exception as e:
        print(f"No se pudo conectar al host {host} mediante NETCONF: {e}")
