#Importando a biblioteca "Pika", responsável por fazer a conexão com o Rabbit
import pika

# Conectando com o nosso broker que está localizado no Localhost.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#Criando o canal de conexão que as mensagens irão transitar.
canal = connection.channel()

# Criando um nome para fila.
canal.queue_declare(queue='thompson-queue')

# Pronto. Até aqui, tudo o que precisávamos para estabelecer a conexão e 
# enviar a mensagem já foi feito. 
# Agora iremos preparar a nossa mensagem para ser enviada.

#variavel auxiliar para rodar um menu simples de interface.
aux = 1

#importar dados "datetime" para melhorar a visualização da interface.
from datetime import datetime, timezone

#mensagem inicial ao iniciar o sender
print("Bem vindo ao ZapZap")

#menu
while aux != 2:
    
        #variavel 'msg' irá receber a mensagem digitada a seguir pelo usuario que irá para fila.
        msg = str(input("Digite aqui sua mensagem: "))
        
        #instanciando canal e publicando mensagem na fila com parâmetros para o destinatário.
        canal.basic_publish(exchange='', routing_key='thompson-queue',body=msg)
        
        #instanciando objeto do tipo datetime
        data_atual = datetime.now()
        
        #Printando mensagem digitada para o sender, informando que a mensagem foi enviada com a hora.
        print(data_atual, ": - Enviada.")
        
connection.close()
