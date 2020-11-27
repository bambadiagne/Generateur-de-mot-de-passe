from random import sample
ALL_TYPES={'numeric':list('0123456789'),'alphalower':[chr(i) for i in range(97,123)],'alphaupper':[chr(i) for i in range(65,91)],'specialschars':['[', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', ']'],'alphanum':1}
  
class Password:
    def __init__(self, password_type, password_length=8):
        self.password_length = password_length
        self.password_type = password_type
    def gen_password(self,tabMotif):
        if(self.password_type=='alphanum'):
            ALL_TYPES['alphanum']=ALL_TYPES['numeric']+ALL_TYPES['alphaupper']+ALL_TYPES['specialschars']+ALL_TYPES['alphalower']
        
        return ''.join(sample(tabMotif,int(self.password_length)))
