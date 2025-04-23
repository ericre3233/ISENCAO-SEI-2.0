
from botcity.core import DesktopBot
import pyautogui

def pendencia(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
   #print(f"Imagem {im} encontrada, executando ações.")
   #bot.click()

     

                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"]) 
                                    bot.type_keys(["delete"])  # Agrupando comandos
                                    bot.type_keys(["ctrl", "shift", "-"])
                                    bot.type_keys(["down"] * 2)
                                    bot.type_keys(["enter"])
                                    bot.type_keys(["ctrl", "tab"])
                                    #bot.type_keys(["up"] * 3)
                                    #bot.type_keys(["enter"])
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
                                    bot.type_keys(["ctrl", "c"])
                                    bot.type_keys(["ctrl", "tab"])
                                    bot.type_keys(["ctrl", "alt", "pagedown"])
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
                                    self.wait(1000)
                                    bot.type_keys(["down"] * 8)
                                    bot.type_keys(["enter"])
                                    bot.type_keys(["tab"] * 4)
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["shift" , "tab"] * 2)
                                    bot.type_keys(["enter"])
                                    


                                    if not bot.find( "bloco", matching=0.85, waiting_time=1000):
                                       self.not_found("bloco")
                                    bot.click()
                                    #self.wait(1000)

                                    bot.type_keys(["ctrl", "c"])
                                    
                                    if not bot.find( "assinar", matching=0.85, waiting_time=1000):
                                       self.not_found("assinar")
                                    bot.click()
                           
                                    bot.type_keys(["ctrl", "v"])
                                    bot.type_keys(["enter"])
                                    self.wait(2000)
                                    bot.type_keys(["up"] * 3)
                                    #self.wait(1000)
                                    bot.type_keys(["enter"])
                                    #self.wait(1000)
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
                                    #self.wait(1000)
                                    bot.type_keys(["enter"])          
                                    
                                    bot.type_keys(["ctrl", "tab"]) 
                                    bot.type_keys(["escape"])
                                    bot.type_keys(["ctrl", "alt", "pageup"])                                    
                                    bot.type_keys(["ctrl", "tab"])
                                    #from isencaogerados import isencaogerados

                                                                
                                    from isencaogerados import isencaogerados
                                    isencaogerados(contador, cont, bot=self, self=self)
                                    
                                    #isencaogerados(bot=self, self=self)    
                                 




































