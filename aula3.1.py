import time

def obter_data_hora():
    hora_atual = time.localtime()
    return time.strftime("%H:%M:%S", hora_atual)

def exibir_relogio():

    try:
        while True:
            hora = obter_data_hora()
            print(hora, end="\r")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nRelogio encerrado.")

exibir_relogio()        
