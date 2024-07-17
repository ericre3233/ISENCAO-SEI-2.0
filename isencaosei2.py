from botcity.core import DesktopBot



def isencaosei2(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
 
   while (contador < cont):    
                    
                     self.wait(2000)
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

                     if not bot.find( "requer", matching=0.97, waiting_time=10000):
                        self.not_found("requer")
                     bot.click()

                     bot.type_down() 
                     self.wait(1000)
                     
                     try:
                          
                        #if not bot.find( "nome3", matching=0.97, waiting_time=10000):
                        #    self.not_found("nome3")
                        #bot.triple_click_relative(50, 46)
                         
                        if not bot.find( "nome3", matching=0.97, waiting_time=10000):
                            self.not_found("nome3")
                        bot.triple_click_relative(82, 47)
                         
                         

                     except: 
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_down()
                        from isencaosei import isencaosei
                        isencaosei(contador, cont, bot=self, self=self)
                        

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

                     if not bot.find( "cpf3", matching=0.97, waiting_time=10000):
                         self.not_found("cpf3")
                     bot.triple_click_relative(46, 43)

                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     bot.type_keys(["tab", "tab" ])
                     bot.type_keys(["ctrl", "tab"])

                     try:
                           if not bot.find( "enderr", matching=0.97, waiting_time=10000):
                              self.not_found("enderr")
                           bot.triple_click_relative(520, 35)
                              
                     except:
                           if not bot.find( "enderrr", matching=0.97, waiting_time=10000):
                                 self.not_found("enderrr")
                           bot.triple_click_relative(381, 42)
                   
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["f2", "ctrl", "v"])
                     self.backspace()
                     self.backspace()
                     self.enter()
                     bot.type_left()
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["tab", "tab", "tab", "tab", "tab"])
                     from isencaosei import isencaosei
                     isencaosei(contador, cont, bot=self, self=self)
                     contador   = contador + 1




              
              
              
              
              



       














              










































































































































































































































































































































































































































































































































































