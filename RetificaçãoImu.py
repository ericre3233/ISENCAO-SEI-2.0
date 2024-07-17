from botcity.core import DesktopBot
import pyautogui


def RetificaçãoImu(contador, cont, bot: DesktopBot, self: DesktopBot, executation=None):
 
   while (contador < cont):    
                    
                     self.wait(2000)
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_keys(["ctrl", "c"])
                     bot.type_keys(["ctrl", "tab"])     
                     
                     if not bot.find( "pesquisar", matching=0.97, waiting_time=10000):
                        self.not_found("pesquisar")
                     bot.click()
                     

                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["enter"])
                     self.wait(2000)

                     if not bot.find( "dados", matching=0.97, waiting_time=10000):
                         self.not_found("dados")
                     bot.click()
                     
                     self.wait(1000)
                     if not bot.find( "interessado", matching=0.97, waiting_time=10000):
                           self.not_found("interessado")
                     bot.click_relative(94, 65)

                     self.wait(1000)
                     if not bot.find( "interessado", matching=0.97, waiting_time=10000):
                           self.not_found("interessado")
                     bot.double_click_relative(94, 65)
                     
                     try:
                        if not bot.find( "maximizar", matching=0.97, waiting_time=10000):
                           self.not_found("maximizar")
                        bot.click()
                     except:  
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_down()
                        bot.type_keys(["ctrl", "tab"])
                        RetificaçãoImu(contador, cont, bot=self, self=self)

                     if not bot.find( "nome", matching=0.97, waiting_time=10000):
                         self.not_found("nome")
                     bot.triple_click_relative(76, 35)
                     
                     bot.type_keys(["ctrl", "c"])
                     bot.type_down()
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_left()
                     bot.type_left()
                     bot.type_keys(["ctrl", "v"])
                     bot.type_keys(["ctrl", "tab"]) 
                     bot.type_down()
                     bot.type_down()
                     bot.type_down()

                     try:  
                        if not bot.find( "cidade2", matching=0.97, waiting_time=10000):
                           self.not_found("cidade2")
                        bot.click()
                     except:
                        if not bot.find( "fechar2", matching=0.97, waiting_time=10000):
                           self.not_found("fechar2")
                        bot.click()
                        self.wait(1000)    
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_right()
                        bot.type_right()   
                        bot.type_down()    
                        bot.type_keys(["ctrl", "tab"])              
                        RetificaçãoImu(contador, cont, bot=self, self=self)    


                     #if not bot.find( "ccpf", matching=0.97, waiting_time=10000):
                     #    self.not_found("ccpf")
                     #bot.triple_click_relative(46, 37)
                     
                     #try:
                        #if not bot.find( "cnpj", matching=0.97, waiting_time=10000):
                        #   self.not_found("cnpj")
                        #bot.triple_click_relative(57, 32)
                     try:  
                        if not bot.find( "ccpf", matching=0.97, waiting_time=10000):
                           self.not_found("ccpf")
                        bot.triple_click_relative(65, 39)   

                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_right()
                        bot.type_keys(["ctrl", "v"])
                        bot.type_keys(["ctrl", "tab"])                            
                                 
                        bot.right_click()

                        if not bot.find( "pesquisargoo", matching=0.97, waiting_time=10000):
                           self.not_found("pesquisargoo")
                        bot.click()                    
                        self.wait(1000)                     


                        #if not bot.find( "cidade2", matching=0.97, waiting_time=10000):
                        #   self.not_found("cidade2")
                        #bot.click() 
                        pyautogui.click(r'.\resources\cidade2.png')
                        pyautogui.move(-30,10)
                        pyautogui.drag(250,40,0.25)  
                        
                         
                     except:
                        if not bot.find( "CNPJRET", matching=0.97, waiting_time=10000):
                            self.not_found("CNPJRET")
                        bot.triple_click_relative(69, 37)  

                        bot.type_keys(["ctrl", "c"])
                        bot.type_keys(["ctrl", "tab"])
                        bot.type_right()
                        bot.type_keys(["ctrl", "v"])
                        bot.type_keys(["ctrl", "tab"])                            
                                 
                        bot.right_click()

                        if not bot.find( "pesquisargoo", matching=0.97, waiting_time=10000):
                           self.not_found("pesquisargoo")
                        bot.click()                    
                        self.wait(1000)  

                        #if not bot.find( "cidade2", matching=0.97, waiting_time=10000):
                        #   self.not_found("cidade2")
                        #bot.click() 
                        pyautogui.click(r'.\resources\cidade3.png')
                        pyautogui.move(-30,10)
                        pyautogui.drag(250,40,0.25)  

                     if not bot.find( "tradutor", matching=0.97, waiting_time=10000):
                         self.not_found("tradutor")
                     bot.click()

                     try:
                        if not bot.find( "slecionartudo", matching=0.97, waiting_time=10000):
                           self.not_found("slecionartudo")
                        bot.triple_click_relative(66, 69)
                        bot.type_keys(["ctrl", "c"])
                     except:
                        bot.type_keys(["ctrl", "c"]) 

                     if not bot.find( "fechartradutor", matching=0.97, waiting_time=10000):
                         self.not_found("fechartradutor")
                     bot.click()
                     
                     if not bot.find( "fechar2", matching=0.97, waiting_time=10000):
                         self.not_found("fechar2")
                     bot.click()                    
                     
                     bot.type_keys(["ctrl", "tab"])
                     bot.type_right()
                     bot.type_right()
                     bot.type_keys(["ctrl", "v"])
                     bot.type_left()
                     bot.type_down()
                     bot.type_keys(["ctrl", "tab"])

                     contador   = contador + 1
                      
                     #bot.right_click()
                     #bot.type_down()
                     #bot.type_down()
                     #bot.type_down()
                     #bot.type_down()
                     #bot.enter()
                     #self.wait(2000)
                     #bot.enter()
                     #self.wait(3000)
                     #self.paste('Termo')
                     #self.wait(1000)
                     #bot.enter()
                     #self.wait(2000)
                     #bot.type_keys(["tab"])
                     #bot.enter()
                     
                     
                     #if not bot.find( "fechar2", matching=0.97, waiting_time=10000):
                     #    self.not_found("fechar2")
                     #bot.click()
                     #self.wait(1000)
                                         
                     #if not bot.find("explorer", matching=0.97, waiting_time=10000):
                     #    self.not_found("explorer")
                     #bot.click()
                     #self.wait(2000)
                     #bot.enter()
                     #self.wait(3000)

                     #try:
                     #   if not bot.find("cid", matching=0.97, waiting_time=10000):
                     #      self.not_found("cid")
                     #   bot.click()
                     #except:
                     #   bot.type_keys(["ctrl", "w"])
                     #   bot.type_keys(["ctrl", "tab"])
                     #   bot.type_right()
                     #   bot.type_right()
                     #   bot.type_down()
                     #   bot.type_keys(["ctrl", "tab"])
                     #   RetificaçãoImu(contador, cont, bot=self, self=self)      
                    
                     #bot.type_down()
                     #bot.type_down()
                     #bot.type_down()
                     #bot.type_down()
                     

                     #try:
                     #   if not bot.find( "cnpj", matching=0.97, waiting_time=10000):
                     #      self.not_found("cnpj")
                     #   bot.triple_click_relative(57, 32)

                     #except:
                     #   if not bot.find( "cpf", matching=0.97, waiting_time=10000):
                     #      self.not_found("cpf")
                     #   bot.triple_click_relative(65, 39)
                     
                     
                    
                     #bot.type_keys(["ctrl", "c"])
                     #bot.type_keys(["ctrl", "tab"])
                     #bot.type_right()
                     #bot.type_keys(["ctrl", "v"])
                     #bot.type_keys(["ctrl", "tab"]) 
                     #bot.type_keys(["ctrl", "tab"]) 

                     #if not bot.find( "cidade", matching=0.97, waiting_time=10000):
                     #   self.not_found("cidade")
                     #bot.triple_click_relative(29, 36)
                    
                     #bot.type_keys(["ctrl", "c"])
                     #bot.type_keys(["ctrl", "w"])
                     #self.wait(1000)
                     #bot.type_keys(["ctrl", "tab"])
                     #bot.type_right()
                     #bot.type_right()
                     #bot.type_keys(["ctrl", "v"])
                     #bot.type_left()
                     #bot.type_down()
                     #bot.type_keys(["ctrl", "tab"]) 
                     























































































































































































































































































































































































































































































































































































































































































