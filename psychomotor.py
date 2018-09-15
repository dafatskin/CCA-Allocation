 #I am assuming this code is made as a speciallised CCA organizer for RI and as such only included the current CCAs and hardcoded the CCA names and numbers
          #(Golf is not inside as it is now redundant)
          #If you feel that hardconding these numbers are biased fix them. 
          #Either way every student is based off these scores and ranked along the same rubrics
          
def run(psymo):
    if CCA=="BAS":
        if psymo[name]["30m"]<=5.5:
            score+=3
        else:
            score+=1
                  
        if psymo[name]["IPU"]>=10:
          score+=2
        else:
          score+=1
      
      
    elif CCA=="BAD":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1
      
    elif CCA=="FEN":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1

    elif CCA=="CRI":
          if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1

    elif CCA=="CC":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="FLO":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="HOC":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="JUD":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="POLO":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="RUG":
          if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="SAIL":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="SHO":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="SOF":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="SQU":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="SWI":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="TAB":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    elif CCA=="TEN":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1  

    else CCA=="TNF":
        if psymo[name]["Height"]>=170:
          score+=3
        else psymo[name]["Height"]<170:
          score+=2
          
        if psymo[name]["30m"]<=5.5:
          score+=3
        else:
          score+=1
          
        if psymo[name]["SBJ"]>=170:
          score+=3
        else:
          score+=1

