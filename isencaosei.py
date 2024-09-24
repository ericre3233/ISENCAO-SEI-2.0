from botcity.core import DesktopBot


def isencaosei(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):

    while (contador < cont):
                       
                     self.wait(1000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])  



                     imagens = ["pesq", "pesq2"]

                     for imagem in imagens:
                        try:
                           if not bot.find( imagem, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagem)
                           bot.click()
                           break  # Se encontrou a imagem, sai do loop
                        except:
                            continue


                     
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(2000)
                     bot.type_down()
                     self.wait(1000)  

                     imagenss = ["nomesei2", "razao"]

                     for imagemm in imagenss:
                        try:
                           if not bot.find( imagemm, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemm)
                           bot.triple_click_relative(82, 43)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           from isencaogerados import isencaogerados
                           isencaogerados(contador, cont, bot=self, self=self)
                   


                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_left()
                     bot.type_left()                     
                     bot.type_keys(["f2", "ctrl", "v"])
                     bot.type_keys(["enter"])  
                     bot.type_up() 
                     bot.type_keys(["alt"])
                     bot.type_keys(["C"])
                     bot.type_keys(["E"])
                     bot.type_keys(["F"])
                     bot.type_keys(["tab"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["pageDown"])
                     
                     
                     imagensss = ["cpf3", "cpf4" ]

                     for imagemmm in imagensss:
                        try:
                           if not bot.find( imagemmm, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemmm)
                           bot.triple_click_relative(46, 46)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem

                     bot.type_keys(["ctrl", "c"])       # Copia
                     bot.type_keys(["ctrl", "tab"])     # Troca de aba
                     bot.type_keys(["f2", "ctrl", "v"]) # Col
                     bot.wait(1000)    
                     bot.type_keys(["enter"])  
                     bot.type_up() 
                     bot.type_keys(["alt"])
                     bot.type_keys(["C"])
                     bot.type_keys(["E"])
                     bot.type_keys(["F"])
                     bot.type_keys(["tab", "tab"])      # Navega com Tab
                     bot.type_keys(["ctrl", "tab"])     # Troca de aba novamente
        


                     imagenssss = ["municipiosei" , "municipiosei2" , "municipiosei3"]

                     for imagemmmm in imagenssss:
                        try:
                           if not bot.find( imagemmmm, matching=0.90, waiting_time=3000):  # Reduzi o waiting_time para 5000 ms
                             self.not_found(imagemmmm)
                           bot.triple_click_relative(46, 46)
                           break  # Se encontrou a imagem, sai do loop
                        except:
                           continue  # Continua tentando a próxima imagem


                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     bot.type_keys(["enter"])  
                     bot.type_up() 
                     bot.type_keys(["alt"])
                     bot.type_keys(["C"])
                     bot.type_keys(["E"])
                     bot.type_keys(["F"])
                     self.enter()
                     bot.type_left()
                     bot.type_keys(["ctrl", "tab"])     




                     if not bot.find( "bloco", matching=0.85, waiting_time=1000):
                         self.not_found("bloco")
                     bot.click()

                     bot.type_keys(["ctrl", "c"])
                      
                     if not bot.find( "assinar", matching=0.85, waiting_time=1000):
                         self.not_found("assinar")
                     bot.click()
#
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(1000)

                     if not bot.find( "marcador", matching=0.85, waiting_time=1000):
                         self.not_found("marcador")
                     bot.click()

                     bot.type_keys(["tab", "tab", "tab", "tab"])
                     bot.type_keys(["enter"])
                     bot.type_keys(["tab", "tab", "tab", "tab"])
                     bot.type_keys(["enter"])
                     bot.type_keys(["alt", "s"])                 
                      

                     
                     contador   = contador + 1
 
      



              
              
              
              
              



       














              






















































































































































































































































































































































































































































































































