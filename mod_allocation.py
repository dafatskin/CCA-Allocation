###################
#Allocation module#
###################

import psychomotor

def p2_assignDSA(DSA, final_dic, CCA_dic):
    """
    """

    for name, CCA in DSA.dic.items(): #DSA is a class object
        final_dic[name] = {"CCA":CCA, "rank":0} #Allocation line

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = CCA["rank"]
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:CCA["rank"]}

    print("p2_assignDSA complete")
    
    return final_dic, CCA_dic


def p2_assignUnderQuota(quota, LOC, rank, final_dic, CCA_dic):
    """
    """

    CCAs_left = [] #this for the CCAs in p2_assignByScore

    CCA_LOC = {} #reverse LOF
    for name, CCA in LOC.dic[rank].items():
        try:
            lst = CCA_LOC[CCA]
            lst.append(name)
            CCA_LOC[CCA] = lst
        except KeyError:
            CCA_LOC[CCA] = [name]
        
    for category, dic in quota.dic.items():
        for CCA, quota in dic.items():
            try: #get number of first_choice
                first_for_CCA = len(CCA_LOC[CCA])
            except KeyError:
                first_for_CCA = 0
            try: #get number of assigned students
                alras = len(CCA_dic[CCA])
            except KeyError:
                alras = 0
                
            if first_for_CCA + alras <= quota: #add, if less thatn quota:
                try:
                    for name in CCA_LOC[CCA]:
                        final_dic[name] = {"CCA":CCA, "rank":rank} #Allocation line
                except KeyError:
                    pass
            else:
                CCAs_left.append(CCA)

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = CCA["rank"]
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:CCA["rank"]}
    
    return final_dic, CCA_dic, CCAs_left

  
  def p2_calculate_score(CCA, name_cat, psymo, CCA_ranking, MEP, DSA):
    score=0
    score_dict={}
    for name, cat in name_cat.dic.items():
      if cat=="performing_arts":        
          score=100
          for rank in CCA_ranking[name]:
            score=score+rank
          score_dict[name]=str(score)
      elif cat=="sports":
        score=0
          for rank in CCA_ranking[name]:
            score=score+rank
        psychomotor.run(psymo)
        score_dict[name]=str(score)
      else:
        score=0
          for rank in CCA_ranking[name]:
            score=score+rank
        score_dict[name]=str(score)  
        
    return score_dict
