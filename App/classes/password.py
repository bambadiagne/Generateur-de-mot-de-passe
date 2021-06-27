from random import sample
ALL_TYPES={'numeric':list('0123456789'),'alphalower':[chr(i) for i in range(97,123)],'alphaupper':[chr(i) for i in range(65,91)],'specialschars':['[', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', ']'],'alphanum':1}
ALL_TYPES['alphanum']=ALL_TYPES['numeric']+ALL_TYPES['alphaupper']+ALL_TYPES['specialschars']+ALL_TYPES['alphalower']  
class Password:
    def __init__(self, password_type, password_length=8):
        
        self.password_length = password_length
        self.password_type = password_type
    
    def gen_password(self,tabMotif):
            
        return ''.join(sample([elt for type_password in tabMotif for elt in  ALL_TYPES[type_password]],int(self.password_length)))
