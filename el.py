import wget
import os
import sys
from os import system
# system("node mail.js")
# os.rename('./update/download.wget', './update/x')


def createmail(message):
    contenido = open("./email.txt").read().splitlines()
    # contenido = open("/home/ebossteam/UnattendedInstallation/FULLSTACK/mails/email.txt").read().splitlines()
    contenido.insert(2,"    email: 'brian.cobian@alumnos.udg.mx',")
    contenido.insert(2,"    msg: '"+message+"',")
    # f = open('/home/ebossteam/UnattendedInstallation/FULLSTACK/mails/mail.js', "w")
    f = open('./mail.js', "w")

    f.writelines("\n".join(contenido))
    f.close


def changeBat(fileDirectory):
    with open(fileDirectory,'r') as archivo:
      bandera=0
      versiones=[]
      for linea in archivo:
        linea=linea.rstrip('\n')
        if '193971' in linea or bandera==1:
            bandera=1
            # print(linea)
            versiones.append(linea)
            if 'center' in linea:
              bandera =0
              # print(linea)
      # for x in versiones : 
      #   incio=x.find('>')
      #   print(x[incio+1:incio+3])
      cupos=versiones[len(versiones)-2]
      print('\n'+cupos)
      incio=cupos.find('>')
      cupo=cupos[incio+1:incio+3]

      print('\nLos cupos disponibles son: '+cupo)
      # print( cupo == '31')
      if cupo == '31':
        print('Aun no cambia la agenda')
        msg ='Aun no cambia la agenada'
      else:
        print('Ya puedes agendaarla!!!')
        msg="Ya puedes agendaarla!!!"
        with open('./cline.sh','r') as jajaz:
          for linea in jajaz:
            if 'YA SE ENVIO' in linea:
              print('jaja')
            else:
              createmail(msg)
              system("node mail.js")
        contenido = open("./cline.sh").read().splitlines()
        contenido.insert(2,"YA SE ENVIO")
        f = open('./cline.sh', "w")
        f.writelines("\n".join(contenido))
        f.close
        
      # print(versiones[len(versiones)-2])
        
        
def getverison():
  url = 'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop=202310&cup=D&crsep=IL350'
  output_directory = './update'
  filename = wget.download(url , out=output_directory)
  # print(ACEBASE)
  x=changeBat(filename)
  os.remove(filename)
  return x
 
getverison()
