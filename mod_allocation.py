###################
#Allocation module#
###################

import mod_data as modD

import random

def p2_assignDSA(DSA, final_dic, CCA_dic):
    """
    """

    for name, CCA in DSA.dic.items(): #DSA is a class object
        final_dic[name] = {"CCA":CCA, "rank":0, "score":9001} #Allocation line

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = {"rank":CCA["rank"],"score":CCA["score"]}
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:{"rank":CCA["rank"],"score":CCA["score"]}}

    print("p2_assignDSA complete")
    
    return final_dic, CCA_dic


def p2_assignUnderQuota(quota, pysmo, CCA_ranking, MEP, LOC, rank, final_dic, CCA_dic, config_vars):
    """
    """
    
    CCAs_left = [] #this for the CCAs in p2_assignByScore

    CCA_LOC = {} #reverse LOC
    for name, CCA in LOC.dic[rank].items():
        try:
            lst = CCA_LOC[CCA]
            lst.append(name)
            CCA_LOC[CCA] = lst
        except KeyError:
            CCA_LOC[CCA] = [name]
        
    for category, dic in quota.dic.items():
        for CCA, quota2 in dic.items():
            scorelist = p2_calculate_score(CCA, modD.data_to_nameCat(LOC, quota, rank, CCA), pysmo, CCA_ranking, MEP, config_vars)
            lst = []
            for key, value in scorelist.items():
                lst.append(key)
                
            try: #get number of first_choice
                first_for_CCA = len(CCA_LOC[CCA])
            except KeyError:
                first_for_CCA = 0
            try: #get number of assigned students
                alras = len(CCA_dic[CCA])
            except KeyError:
                alras = 0

            if first_for_CCA + alras <= quota2: #add, if less than quota:
                try:
                    for name in CCA_LOC[CCA]:
                        var = {"CCA":CCA, "rank":rank, "score":scorelist[name]}
                        final_dic[name] = var #Allocation line
                except KeyError:
                    pass #lol no one wanted to join
            else:
                CCAs_left.append(CCA)

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = {"rank":CCA["rank"],"score":CCA["score"]}
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:{"rank":CCA["rank"],"score":CCA["score"]}}
    
    return final_dic, CCA_dic, CCAs_left

  
def p2_calculate_score(CCA, name_cat, psymo, CCA_ranking, MEP, config_vars):
    """
    """
    
    score=0
    score_dict={}
    for name, cat in name_cat.items():
        if cat=="PERFORMING ARTS":        
            score=10
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
                        score=score+20/int(rank)
                except KeyError:
                    pass
            else:
                pass

            lst = ["Height", "30m", "IPU", "SBJ", "1km"]
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
        else:
            score_dict[name]=str(score)
    
    return score_dict


def p2_allocateByScore(CCA, nameCat, quota, rank, scorelist, final_dic, CCA_dic):
    """
    """

    cat = ""
    for key, value in nameCat.items(): #theoretically it will all be the same anyway
        cat = value
    quota_int = quota.dic[cat][CCA]

    in_order = []
    for name, score in scorelist.items():
        if in_order == []:
            in_order.append(name)
        else:
            added = False
            for name2 in in_order:
                if added == False:
                    if scorelist[name2] < score:
                        in_order.insert(in_order.index(name2), name)
                        added = True
                    else:
                        pass
                else:
                    pass

    try: #get number of assigned students
        alras = len(CCA_dic[CCA])
    except KeyError:
        alras = 0

    pos_left = quota_int - alras

    to_add = in_order[0:pos_left]

    for name in to_add:
        final_dic[name] = {"CCA":CCA, "rank":rank, "score":scorelist[name]} #Allocation line

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = {"rank":CCA["rank"],"score":CCA["score"]}
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:{"rank":CCA["rank"],"score":CCA["score"]}}
    
    return final_dic, CCA_dic


def p3_allocateRemainder(quota, master_dic, CCA_dic, final_dic):
    """
    """

    unassigned = []
    for name, data in master_dic["classlist"][0].items():
        if name in final_dic: #alr assigned
            pass
        else:
            unassigned.append(name)
    del unassigned[0]

    notfilled = [1]
    allassigned = False
    while notfilled != [] and allassigned != True:
        notfilled = []
        for category, dic in quota.dic.items():
            for cca, quota2 in dic.items():
                try:
                    if len(CCA_dic[cca]) < quota2:
                        notfilled.append(cca)
                    else:
                        pass
                except KeyError:
                    notfilled.append(cca)

        for cca in notfilled:
            if unassigned != []:
                index = random.randint(0, len(unassigned)-1)
                final_dic[unassigned[index]] = {"CCA":cca, "rank":10, "score":0}
                del unassigned[index]
            else:
                allassigned = True
        
    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = {"rank":CCA["rank"],"score":CCA["score"]}
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:{"rank":CCA["rank"],"score":CCA["score"]}}
    
    return final_dic, CCA_dic
            

def p4_reassignment(final_dic, CCA_dic):
    """
    """

    student_lst = []
    for name, data in final_dic.items():
        print(score)

    return final_dic, CCA_dic

