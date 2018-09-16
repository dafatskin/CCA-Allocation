###################
#Allocation module#
###################


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

  
 def p2_calculate_score(CCA, name_cat, psymo, CCA_ranking, MEP, config_vars):
    score=0
    score_dict={}
    for name, cat in name_cat.items():
        if cat=="PERFORMING ARTS":        
            score=100
            try:
                for placeholder, rank in CCA_ranking[CCA][name]:
                    score=score+int(rank)
            except:
                pass
            score_dict[name]=str(score)
        elif cat=="SPORTS":
            score=0
            scoring_details = config_vars["scoring details"][CCA]
            if scoring_details["rankscoring"] == "on":
                try:
                    for placeholder, rank in CCA_ranking[CCA][name].items():
                        score=score+int(rank)
                except KeyError:
                    pass
            else:
                pass

            lst = ["Height", "30m", "IPU", "SBJ"]
            for i in lst:
                var = psymo.dic[name][i]
                if var == None:
                    var = 0
                else:
                    pass
                if var>=float(scoring_details[i]["criteria"]):
                    score+=float(scoring_details[i]["other"])
                else:
                    score+=float(scoring_details[i]["default"])

            score_dict[name]=str(score)  
    
    return score_dict
