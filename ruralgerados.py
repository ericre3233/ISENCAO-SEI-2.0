from botcity.core import DesktopBot

def ruralgerados(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):

    while (contador < cont):
                       
                     self.wait(1000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     
                     if not bot.find( "pesquisar", matching=0.97, waiting_time=10000):
                         self.not_found("pesquisar")
                     bot.click()
                     
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(2000)
                     bot.type_down()
                     self.wait(1000)  

                     try:                   
                    
                        if not bot.find( "nome2", matching=0.97, waiting_time=10000):
                            self.not_found("nome2")
                        bot.triple_click_relative(91, 60)  

                     except:        

                        from ruralsei import ruralsei
                        ruralsei(contador, cont, bot=self, self=self)                                                            


                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_left()
                     bot.type_left()                     
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     bot.type_keys(["tab"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["pageDown"])
                     
                     if not bot.find( "cpf2", matching=0.97, waiting_time=10000):
                         self.not_found("cpf2")
                     bot.triple_click_relative(45, 59)

                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     bot.type_keys(["tab", "tab" ])
                     bot.type_keys(["ctrl", "tab"])
                            
                     if not bot.find( "municipio2", matching=0.97, waiting_time=10000):
                        self.not_found("municipio2")
                     bot.triple_click_relative(505, 182)                    

                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     self.enter()
                     bot.type_left()
                     bot.type_keys(["ctrl", "tab"])                      
                      
                     #if not bot.find( "pesquisar", matching=0.97, waiting_time=10000):
                     #    self.not_found("pesquisar")
                     #bot.click()
                     contador   = contador + 1
 
      



              
              
              
              
              



       














              






















































































































































































































































































































































































































































































