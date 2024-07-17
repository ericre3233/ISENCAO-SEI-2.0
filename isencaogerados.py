from botcity.core import DesktopBot



def isencaogerados(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):

    while (contador < cont):
                       
                     self.wait(1000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     
                     #if not bot.find( "pesquisar", matching=0.97, waiting_time=10000):
                     #    self.not_found("pesquisar")
                     #bot.click()
                     
                     if not bot.find( "pesq", matching=0.97, waiting_time=10000):
                         self.not_found("pesq")
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
                     
                        try:
                            if not bot.find( "razao", matching=0.97, waiting_time=10000):
                                self.not_found("razao")
                            bot.triple_click_relative(82, 63)
                        except:                                               
                            from isencaosei import isencaosei  
                            bot.type_keys(["ctrl", "tab"])
                            #bot.type_down()
                            bot.type_keys(["ctrl", "tab"])
                            isencaosei(contador, cont, bot=self, self=self) 
                            self.wait(2000)                                                           


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
                     
                     try:
                        if not bot.find( "cpf2", matching=0.97, waiting_time=10000):
                            self.not_found("cpf2")
                        bot.triple_click_relative(45, 59)
                     except:
                        if not bot.find( "cnpjj", matching=0.97, waiting_time=10000):
                            self.not_found("cnpjj")
                        bot.triple_click_relative(40, 65)
                          

                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     bot.type_keys(["tab", "tab" ])
                     bot.type_keys(["ctrl", "tab"])

                     try:       
                        if not bot.find( "municipio2", matching=0.97, waiting_time=10000):
                            self.not_found("municipio2")
                        bot.triple_click_relative(500, 182) 
                     except: 
                        if not bot.find( "cnpjjj", matching=0.97, waiting_time=10000):
                            self.not_found("cnpjjj")
                        bot.triple_click_relative(410, 162)
                                    

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
                      
                     if not bot.find( "pesq", matching=0.97, waiting_time=10000):
                         self.not_found("pesq")
                     bot.click()
                     
                     contador   = contador + 1
 
      



              
              
              
              
              



       














              






















































































































































































































































































































































































































































































