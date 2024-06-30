vlan_number = int(input("Por favor, ingrese el número de VLAN: "))


if 1 <= vlan_number <= 1005:
    print(f"La VLAN {vlan_number} corresponde al rango normal.")
elif 1006 <= vlan_number <= 4094:
    print(f"La VLAN {vlan_number} corresponde al rango extendido.")
else:
    print(f"El número de VLAN {vlan_number} no es válido. Debe estar entre 1 y 4094.")
