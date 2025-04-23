import threading
import time
from botcity.core import DesktopBot
import keyboard
import pyautogui

execucao_permitida = False

def monitorar_tecla(contador, cont, bot: DesktopBot, self: DesktopBot):
      while (contador < cont):   
                     
         global execucao_permitida
         while True:
            if keyboard.is_pressed('t'):
                  execucao_permitida=True
                  #from pendencia import pendencia
                  pendencia(contador, cont, bot=self, self=self)
                  time.sleep(0.5)  # Delay para evitar múltiplas chamadas rápidas

def isencaogerados2(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
   global execucao_permitida
   

   while (contador < cont): 
                     
                  self.wait(1000)
                  bot.type_keys(["ctrl", "tab"])
                  bot.type_keys(["ctrl", "c"])
                  bot.type_keys(["ctrl", "tab"])  
                  if not bot.find( "pesq", matching=0.85, waiting_time=1000):
                     self.not_found("pesq")
                  bot.click()
                  bot.type_keys(["ctrl", "v"])
                  bot.type_keys(["enter"])
                  threading.Thread(target=monitorar_tecla, args=(contador, cont, bot, self), daemon=True).start()
                  self.wait(4000)
                  if not execucao_permitida:                   
                    
                        bot.type_keys(["down"] * 3) 
                        #self.wait(1000)
                        

                        img = ["pdf"]
                        for im in img:
                           try:
                              if not bot.find(im, matching=0.85, waiting_time=1000):
                                    self.not_found(im)
                                    print(f"Imagem {im} não encontrada.")
                                    bot.type_keys(["up"] * 2)
                                    self.wait(2000)
                              else:
                                    print(f"Imagem {im} encontrada, executando ações.")
                                    bot.click()
                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"]) 
                                    bot.type_keys(["delete"])  # Agrupando comandos
                                    bot.type_keys(["ctrl", "shift", "-"])
                                    bot.type_keys(["down"] * 2)
                                    bot.type_keys(["enter"])
                                    bot.type_keys(["ctrl", "tab"])
                                    bot.type_keys(["up"] * 3)
                                    bot.type_keys(["enter"])
                                    if not bot.find( "requerivazio", matching=0.85, waiting_time=1000):
                                       self.not_found("requerivazio")
                                    bot.click()
                                    imgreq = ["requerimento", "requerimento2"]
                                    for img in imgreq:
                                       try:
                                          if not bot.find( img, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                             self.not_found(img)
                                          bot.triple_click_relative(82, 57)
                                          break  # Se encontrou a imagem, sai do loop
                                       except:
                                          continue   
                                    self.wait(1000)                                 
                                    bot.type_keys(["ctrl", "c"])
                                    bot.type_keys(["ctrl", "tab"])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "alt", "pagedown"])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "l"  ])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "v"])
                                    self.wait(2000)
                                    bot.type_keys(["enter"])
                                    self.wait(1000)
                                    bot.type_keys(["escape"])
                                    self.wait(1000)
                                    bot.type_keys(["down"] * 1) 
                                    bot.type_keys(["ctrl", "c"])
                                    bot.type_keys(["ctrl", "tab"])
                                    if not bot.find( "novo", matching=0.85, waiting_time=1000):
                                       self.not_found("novo")
                                    bot.click()
                                    self.wait(1000)
                                    bot.type_keys(["down"] * 8)
                                    bot.type_keys(["enter"])
                                    bot.type_keys(["tab"] * 4)
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["shift" , "tab"] * 2)
                                    bot.type_keys(["enter"])
                                    self.wait(3000)

                                    if not bot.find( "bloco", matching=0.85, waiting_time=1000):
                                       self.not_found("bloco")
                                    bot.click()                                    

                                    bot.type_keys(["ctrl", "c"])
                                    
                                    if not bot.find( "assinar", matching=0.85, waiting_time=1000):
                                       self.not_found("assinar")
                                    bot.click()
                                    self.wait(1000)
                           
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["enter"])
                                    self.wait(5000)
                                    bot.type_keys(["up"] * 3)
                                    #self.wait(1000)
                                    bot.type_keys(["enter"])
                                    #self.wait(1000)
                                    pyautogui.move(-60,30)
                                    #self.wait(1000)

                                    if not bot.find( "relogio", matching=0.85, waiting_time=1000):
                                       self.not_found("relogio")
                                    bot.click()
                                    if not bot.find( "prazo", matching=0.85, waiting_time=1000):
                                       self.not_found("prazo")
                                    bot.click()
                                    bot.type_keys(["shift" , "tab"] * 3)
                                    bot.type_keys("10")
                                    #self.wait(1000)
                                    bot.type_keys(["enter"])          
                                    
                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"])
                                    bot.type_keys(["ctrl", "alt", "pageup"])                                    
                                    bot.type_keys(["ctrl", "tab"])     
                                    isencaogerados2(contador, cont, bot=self, self=self)
                                 
                                    
                           except Exception as e:
                              continue         

                        imgreq = ["requerimento", "requerimento2"]
                        for img in imgreq:
                           try:
                              if not bot.find( img, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                 self.not_found(img)
                              bot.triple_click_relative(82, 57)
                              break  # Se encontrou a imagem, sai do loop
                           except:
                              continue
                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_keys(["right"] * 6)
                        bot.type_keys(["f2", "ctrl", "v"])
                        bot.type_keys(["backspace"] * 2) 
                        bot.type_keys(["tab"])  
                        bot.type_keys(["left"] * 9)
                        bot.type_keys(["ctrl", "tab"])



                        imagens = ["nomegerados1", "nomegerados2", "razao", "razao2"]
                        for imagem in imagens:
                           try:
                              if not bot.find( imagem, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                 self.not_found(imagem)
                              bot.triple_click_relative(82, 63)
                              break  # Se encontrou a imagem, sai do loop
                           except:
                              continue                                   
                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        #bot.type_keys(["left"] * 2)                  
                        bot.type_keys(["f2", "ctrl", "v"])
                        bot.type_keys(["backspace"] * 2)
                        bot.type_keys(["tab"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_keys(["down"] * 6)

                        
                        imagenss = ["cpfgerados1", "cpfgerados2", "cnpjgerados1", "cnpjgerados2"  ]
                        for imagemm in imagenss:
                           try:
                              if not bot.find( imagemm, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                 self.not_found(imagemm)
                              bot.triple_click_relative(45, 59)
                              break  # Se encontrou a imagem, sai do loop
                           except:
                              continue  # Continua tentando a próxima imagem                          
                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_keys(["f2", "ctrl", "v"])
                        bot.type_keys(["backspace"] * 2)
                        bot.type_keys(["tab", "tab" ])
                        bot.type_keys(["ctrl", "tab"])

                     
                        imagensss = ["municipio", "municipio2", "municipio3" ]
                        for imagemmm in imagensss:
                           try:
                              if not bot.find( imagemmm, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                 self.not_found(imagemmm)
                              bot.triple_click_relative(66, 59)
                              break  # Se encontrou a imagem, sai do loop
                           except:
                              continue  # Continua tentando a próxima imagem        
                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_keys(["f2", "ctrl", "v"])
                        bot.type_keys(["backspace"] * 2)
                        self.enter()
                        bot.type_left()
                        bot.type_keys(["ctrl", "tab"])            

                        self.wait(1000)
                        if not bot.find( "bloco", matching=0.85, waiting_time=1000):
                           self.not_found("bloco")
                        bot.click()

                        bot.type_keys(["ctrl", "c"])
                        
                        if not bot.find( "assinar", matching=0.85, waiting_time=1000):
                           self.not_found("assinar")
                        bot.click()
                        self.wait(1000)

                        bot.type_keys(["ctrl", "v"])
                        bot.type_keys(["enter"])
                        self.wait(5000)
                        bot.type_up() 
                        #self.wait(1000)
   

                        if not bot.find( "marcador", matching=0.85, waiting_time=1000):
                           self.not_found("marcador")
                        bot.click()

                        bot.type_keys(["tab", "tab", "tab", "tab"])
                        bot.type_keys(["enter"])
                        bot.type_keys(["tab", "tab", "tab", "tab"])
                        bot.type_keys(["enter"])
                        bot.type_keys(["alt", "s"])

                        #bot.type_keys(["ctrl", "up"])  # Isso geralmente solta a tecla Ctrl
                        #bot.type_keys(["shift", "up"])

                   
                  else:
                      break     #break
                       
                  contador = contador + 1 

def pendencia(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
   #print(f"Imagem {im} encontrada, executando clsações.")
   #bot.click()
  
                                    global execucao_permitida
                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"]) 
                                    bot.type_keys(["delete"])  # Agrupando comandos
                                    bot.type_keys(["ctrl", "shift", "-"])
                                    bot.type_keys(["down"] * 2)
                                    bot.type_keys(["enter"])
                                    self.wait(2000)
                                    bot.type_keys(["ctrl", "tab"])
                                    #bot.type_keys(["up"] * 3)
                                    #bot.type_keys(["enter"])
                                    self.wait(2000)
                                    if not bot.find( "requerivazio", matching=0.85, waiting_time=1000):
                                       self.not_found("requerivazio")
                                    bot.click()
                                    self.wait(1000)
                                    imgreq = ["requerimento", "requerimento2"]
                                    for img in imgreq:
                                       try:
                                          if not bot.find( img, matching=0.85, waiting_time=1000):  # Reduzi o waiting_time para 5000 ms
                                             self.not_found(img)
                                          bot.triple_click_relative(82, 57)
                                          break  # Se encontrou a imagem, sai do loop
                                       except:
                                          continue      
                                    self.wait(2000)                                 
                                    bot.type_keys(["ctrl", "c"])
                                    bot.type_keys(["ctrl", "tab"])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "alt", "pagedown"])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "l"  ])
                                    self.wait(1000)
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["enter"])
                                    self.wait(1000)
                                    bot.type_keys(["escape"])
                                    self.wait(1000)
                                    bot.type_keys(["down"] * 1) 
                                    bot.type_keys(["ctrl", "c"])
                                    bot.type_keys(["ctrl", "tab"])
                                    if not bot.find( "novo", matching=0.85, waiting_time=1000):
                                       self.not_found("novo")
                                    bot.click()
                                    bot.type_keys(["down"] * 8)
                                    bot.type_keys(["enter"])
                                    bot.type_keys(["tab"] * 4)
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["shift" , "tab"] * 2)
                                    bot.type_keys(["enter"])
                                    


                                    if not bot.find( "bloco", matching=0.85, waiting_time=1000):
                                       self.not_found("bloco")
                                    bot.click()
                                    self.wait(1000)

                                    bot.type_keys(["ctrl", "c"])
                                    
                                    if not bot.find( "assinar", matching=0.85, waiting_time=1000):
                                       self.not_found("assinar")
                                    bot.click()
                           
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["enter"])
                                    self.wait(2000)
                                    bot.type_keys(["up"] * 3)
                                    self.wait(1000)
                                    bot.type_keys(["enter"])
                                    self.wait(1000)
                                    pyautogui.move(-60,30)
                                    self.wait(1000)

                                    if not bot.find( "relogio", matching=0.85, waiting_time=1000):
                                       self.not_found("relogio")
                                    bot.click()
                                    if not bot.find( "prazo", matching=0.85, waiting_time=1000):
                                       self.not_found("prazo")
                                    bot.click()
                                    bot.type_keys(["shift" , "tab"] * 3)
                                    bot.type_keys("10")
                                    self.wait(1000)
                                    bot.type_keys(["enter"])          
                                    
                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"])
                                    bot.type_keys(["ctrl", "alt", "pageup"])                                    
                                    bot.type_keys(["ctrl", "tab"])
                                    #from isencaogerados import isencaogerados

                                    execucao_permitida = False
                                    from isencaogerados2 import isencaogerados
                                    isencaogerados2(contador, cont, bot=self, self=self)
                                    #isencaogerados(bot=self, self=self)    
                                 












































































































































































































































































































