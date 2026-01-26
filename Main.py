class Friend:
    
    def __init__ (self, name = '', birthday = -1, edu_bg, how_meet = '', likes = [], dislikes = [], hobbies = [], add_info = [], rs = '', CAA = -1):
        self.name = name
        self.birthday = birthday
        self.edu_bg = e_i()
        self.how_meet = how_meet
        self.likes = likes
        self.dislikes = dislikes
        self.hobbies = hobbies
        self.add_info = add_info
        self.rs = rs
        self.CAA = CAA
        
    def attr_change (self,attr,i): # attr will be the attr they want to change, i will be the new info
        if attr.lower() == "name":
            self.name = i
        elif attr.lower() == "birthday":
            self.birthday = i
        elif attr.lower() == "edu_bg":
            self.edu_bg = i
        elif attr.lower() == "how_meet":
            self.how_meet = i
        elif attr.lower() == "likes":
            self.likes = i
        elif attr.lower() == "dislikes":
            self.dislikes = i
        elif attr.lower() == "hobbies":
            self.hobbies = i
        elif attr.lower() == "extra" or attr.lower() == "add info":
            self.add_info = i
        elif attr.lower() == "rs":
            self.rs = i
        elif attr.lower() == "caa":
            self.caa = i
        
    def attr_display (self,attr):
        if attr.lower() == "name":
            return "Name",self.name
        elif attr.lower() == "birthday":
            return "Birthday",self.birthday
        elif attr.lower() == "edu_bg":
            return self.edu_bg ## Not correct, need to use the display function frm edu_bg
        elif attr.lower() == "how_meet":
            return "How we met",self.how_meet
        elif attr.lower() == "likes":
            return "Likes:",self.likes
        elif attr.lower() == "dislikes":
            return "Dislikes:",self.dislikes
        elif attr.lower() == "hobbies":
            return "Hobbies",self.hobbies
        elif attr.lower() == "extra" or attr.lower() == "add info":
            return "Additional Info:",self.add_info # Wrong display
        elif attr.lower() == "rs":
            return "Relationship:",self.rs
        elif attr.lower() == "caa":
            return "CAA:",self.caa
        
class educational_institute as e_i:
    
    def __init__ (self,sch,years_studied,nxt_sch):
        self.sch = None
        self.years_studied = -1
        self.nxt_sch = None
        
    def sch_change (self,new_sch):
        self.sch = new_sch
    
    def year_change (self,new_year):
        self.years_studied = new_year
        
    def nxt_change (self,pointer):
        self.nxt_sch = pointer
        
    
        

