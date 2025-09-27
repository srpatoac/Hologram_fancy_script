import pyautogui
import time
import pyperclip

# Propiedades por defecto
PROPS_HOLO = {
    'scale': "1.5",
    'background': "transparent",
    'textshadow': "true",
    'billboard': "VERTICAL",
    'rotatepitch': "0",
    'visibility': "MANUAL"
}

PROPS_LORE = PROPS_HOLO.copy()
PROPS_LORE['scale'] = "1"  # Scale diferente para el lore

def enviar_comando(comando):
    time.sleep(0.1)
    pyautogui.press('t')
    time.sleep(0.1)
    pyautogui.press('backspace')
    time.sleep(0.1)
    pyperclip.copy(comando)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)

def generar_comandos(nombre, lineas, props):
    cmds = [f"/fancyholograms:hologram create text {nombre}"]
    cmds.append(f"/fancyholograms:hologram edit {nombre} setline 1 {lineas[0]}")
    for i, linea in enumerate(lineas[1:], start=2):
        cmds.append(f"/fancyholograms:hologram edit  {nombre} addline {linea}")
    cmds.append(f"/fancyholograms:hologram edit  {nombre} scale {props['scale']}")
    cmds.append(f"/fancyholograms:hologram edit {nombre} background {props['background']}")
    cmds.append(f"/fancyholograms:hologram edit  {nombre} textshadow {props['textshadow']}")
    cmds.append(f"/fancyholograms:hologram edit {nombre} billboard {props['billboard']}")
    cmds.append(f"/fancyholograms:hologram edit {nombre} rotatepitch {props['rotatepitch']}")
    cmds.append(f"/fancyholograms:hologram edit {nombre} visibility {props['visibility']}")
    return cmds

def crear_holograma(nombre, props):
    lineas = []
    print("Escribe las líneas de texto del holograma (Enter vacío para terminar):")
    while True:
        linea = input(f"Línea {len(lineas)+1}: ")
        if linea == "":
            break
        lineas.append(linea)
    if not lineas:
        print(" Debes escribir al menos una línea")
        return None
    return generar_comandos(nombre, lineas, props)

def main():
    print("=== Generador de Hologramas Fancy automático ===")
    time.sleep(1)

    while True:
        nombre = input("\nNombre del holograma: ").strip()
        if not nombre:
            print(" Debes ingresar un nombre válido")
            continue

        # Holograma principal
        cmds = crear_holograma(nombre, PROPS_HOLO)
        if not cmds:
            continue
        
        print("\n--- Comandos generados ---")
        for c in cmds:
            print(c)

        # Lore automático
        lore = input(f"\n¿Quieres crear un holograma lore para '{nombre}'? (s/n): ").strip().lower()
        if lore == "s":
            nombre_lore = f"{nombre}_lore"
            print(f"\nCreando holograma lore: {nombre_lore}")
            cmds_lore = crear_holograma(nombre_lore, PROPS_LORE)
            if cmds_lore:
                print("\n--- Comandos generados para lore ---")
                for c in cmds_lore:
                    print(c)
                cmds += cmds_lore

        print("\nEn 3 segundos comenzará a pegarse en Minecraft...")
        time.sleep(3)
        for cmd in cmds:
            print(f"Enviando: {cmd}")
            enviar_comando(cmd)

        otra = input("\n¿Quieres crear otro holograma? (s/n): ").strip().lower()
        if otra != "s":
            print("\n🎉 Todos los hologramas enviados a Minecraft.")
            break

main()
