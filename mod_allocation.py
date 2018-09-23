###################
#Allocation module#
###################

import mod_data as modD

import random

def p2_assignDSA(DSA, final_dic, CCA_dic):
    """
    Assigns all DSA students their CCA
    Returns the final dictionaries
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
    Assigns students to CCAs where the quota exceeds the applicants
    Returns the final dictionaries
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
                        if name in final_dic:
                            pass
                        else:
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
    Calculates the score of applicants, to evaluate who should join
    Returns the final dictionaries
    """
    
    score=0
    score_dict={}
    for name, cat in name_cat.items(): #for each name and cateogory
        if cat=="PERFORMING ARTS": #if its a performing arts cca 
            score=0
            try:
                for placeholder, rank in CCA_ranking[CCA][name]:
                    score=score+20/int(rank)
            except:
                pass
            if name in MEP.dic:
                score = 9001
            score_dict[name]=str(score)
        elif cat=="SPORTS": #if its a sports cca
            score=0
            scoring_details = config_vars["scoring details"][CCA]
            if scoring_details["rankscoring"] == "on":
                try:
                    for placeholder, rank in CCA_ranking[CCA][name].items(): #add rank to score
                        score=score+20/int(rank)
                except KeyError:
                    pass
            else:
                pass

            lst = ["Height", "Weight", "30m", "IPU", "SBJ", "1km"] #hardcoded psychomotor test variables. Change if required.
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
    Allocates students to cca where applicants exceed quota
    Returns the final dictionaries
    """

    cat = ""
    for key, value in nameCat.items(): #theoretically it will all be the same anyway
        cat = value
    quota_int = quota.dic[cat][CCA]

    in_order = []
    for name, score in scorelist.items(): #names in order of score
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
        if name in final_dic:
            pass
        else:
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


def p2_assignMerit(merit_choices):
    """
    Assigns all merit ccas to students
    Returns merit cca final dictionaries
    """

    merit_CCA_dic = {} #clear - merit_CCA_dic is based on most updated final_dic
    for name, CCA in merit_choices.dic.items(): #reverse
        try:
            lst = merit_CCA_dic[CCA]
            lst.append(name)
            merit_CCA_dic[CCA] = lst
        except KeyError:
            merit_CCA_dic[CCA] = [name]

    del merit_CCA_dic[None]

    return merit_choices, merit_CCA_dic
        


def p3_allocateRemainder(quota, master_dic, CCA_dic, final_dic):
    """
    Allocates those students who did not get allocated, or did not submit allocation form
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
            

def p4_reassignment(LOC, quota, psymo, CCA_ranking, MEP, final_dic, CCA_dic, config_vars):
    """
    Reassigns students, based on certain criteria, to increase higher choices
    Returns final dictionaries

    Note to editors and readers: this may look daunting and weird. I've commented some stuff to help
    But I myself, having added on many times, can't read it very well as well.
    A tip would be to look at different parts of the code, do some print tests.
    """

    swap_was_made = True #we will repeat until all possible swaps have been made!!!
    while swap_was_made == True:
        swap_was_made = False
        URC = config_vars["reassignment variables"]["under rank criteria"] #different criteria values
        RDC = config_vars["reassignment variables"]["rank diff criteria"]
        SWC = config_vars["reassignment variables"]["switch rank criteria"]
        SDC = config_vars["reassignment variables"]["score diff criteria"]
        
        student_lst = []
        for name, data in final_dic.items():
            student_lst.append(name)

        choicedic = {}
        for rank, data in LOC.dic.items():
            for name, CCA in data.items():
                try:
                    choicedic[name][rank] = CCA
                except KeyError:
                    choicedic[name] = {rank:CCA}
                
        for name in student_lst:
            rank_current = final_dic[name]["rank"] #rank of current CCA
            score_current = final_dic[name]["score"] #score of current CCA
            try:
                ranks_new = choicedic[name]
            except:
                ranks_new = {} #will become ranks of previously chosen

            if rank_current == "0" or rank_current == "LO1":
                ranks_new = {}
            else:
                end_con = False
                try:
                    del ranks_new["LO1"]
                except KeyError:
                    pass
                for rank in ["LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9"]: #for each rank
                    if rank_current == rank:
                        end_con = True
                        try:
                            del ranks_new[rank]
                        except KeyError:
                            pass
                    else:
                        if end_con == False:
                            try:
                                del ranks_new[rank]
                            except KeyError:
                                pass
                        else:
                            pass

            swapped = False
            another_scoredic = {}
            for rank, CCA in ranks_new.items():
                nameCat = {}
                nameCat[name] = modD.data_to_nameCat(LOC, quota, rank, CCA)[name]
                score_new =  p2_calculate_score(CCA, nameCat, psymo, CCA_ranking, MEP, config_vars)[name] #score of new CCA
                try:
                    for alras_name, data in CCA_dic[CCA].items():
                        student_rank = final_dic[alras_name]["rank"] #exchange student's current rank
                        student_score = final_dic[alras_name]["score"] #exchange student's current score
                        try:
                            choices = choicedic[alras_name]
                        except KeyError:
                            choices = {}

                        student_new_rank, student_new_score = "LO0", 0
                        for choice, cca in choices.items():
                            if cca == final_dic[name]["CCA"]:
                                student_new_rank = choice #exchange student's new rank
                                namecat = {}
                                namecat[name] = modD.data_to_nameCat(LOC, quota, rank, CCA)[name] 
                                student_new_score = p2_calculate_score(CCA, namecat, psymo, CCA_ranking, MEP, config_vars)[name] #exchange student's new score
                            else:
                                pass

                        URC_con = None #URC condition
                        if int(URC[-1]) <= int(rank_current[-1]):
                            URC_con = True
                        else:
                            URC_con = False

                        RDC_con = None #RDC condition
                        if student_new_rank == "LO0":
                            if int(RDC) <= int(rank_current[-1]) - 10:                            
                                RDC_con = True
                            else:
                                RDC_con = False
                        else:
                            if int(RDC) <= int(rank_current[-1]) - int(student_new_rank[-1]):                            
                                RDC_con = True
                            else:
                                RDC_con = False

                        SWC_con = None #SWC condition
                        var = 0
                        if student_new_rank != "LO0":
                            try:
                                if int(SWC) <= (int(rank_current[-1]) + int(student_rank[-1])) - (int(student_new_rank[-1]) + int(rank[-1])):
                                    var = (int(rank_current[-1]) + int(student_rank[-1])) - (int(student_new_rank[-1]) + int(rank[-1]))
                                    SWC_con = True
                                else:
                                    SWC_con = False
                            except TypeError:
                                if int(SWC) <= (int(rank_current[-1]) + student_rank) - (int(student_new_rank[-1]) + int(rank[-1])):
                                    var = (int(rank_current[-1]) + student_rank) - (int(student_new_rank[-1]) + int(rank[-1]))
                                    SWC_con = True
                                else:
                                    SWC_con = False
                        else:
                            try:
                                if int(SWC) <= (int(rank_current[-1]) + int(student_rank[-1])) - (10 + int(rank[-1])):
                                    var = (int(rank_current[-1]) + int(student_rank[-1])) - (10 + int(rank[-1]))
                                    SWC_con = True
                                else:
                                    SWC_con = False
                            except TypeError:
                                if int(SWC) <= (int(rank_current[-1]) + student_rank) - (10 + int(rank[-1])):
                                    var = (int(rank_current[-1]) + student_rank) - (10 + int(rank[-1]))
                                    SWC_con = True
                                else:
                                    SWC_con = False

                        SDC_con = None #SDC condition
                        if int(SDC) >= float(student_score) - float(score_new):
                            SDC_con = True
                        else:
                            SDC_con = False

                        if URC_con == True and RDC_con == True and SWC_con == True and SDC_con == True: #if all conditions are GO
                            dic = {"alras_name":alras_name, "alras_CCA":final_dic[name]["CCA"], "alras_rank":student_new_rank, "alras_score":student_new_score}
                            dic["name_CCA"], dic["name_rank"], dic["name_score"] = CCA, rank, score_new
                            dic["score"] = var
                            try:
                                if dic["score"] >= another_scoredic["key"]["score"]:
                                    another_scoredic["key"] = dic
                                else:
                                    pass
                            except KeyError:
                                another_scoredic["key"] = dic
                        else:
                            pass
                except KeyError as e:
                    pass

                try: #Reassign!
                    asd = another_scoredic["key"]
                    final_dic[asd["alras_name"]] = {"CCA":asd["alras_CCA"], "rank":asd["alras_rank"], "score":asd["alras_score"]}
                    final_dic[name] = {"CCA":asd["name_CCA"], "rank":asd["name_rank"], "score":asd["name_score"]}
                    swap_was_made = True
                except:
                    pass

    CCA_dic = {} #clear - CCA_dic is based on most updated final_dic
    for name, CCA in final_dic.items(): #reverse
        try:
            dic = CCA_dic[CCA["CCA"]]
            dic[name] = {"rank":CCA["rank"],"score":CCA["score"]}
            CCA_dic[CCA["CCA"]] = dic
        except KeyError:
            CCA_dic[CCA["CCA"]] = {name:{"rank":CCA["rank"],"score":CCA["score"]}}


    return final_dic, CCA_dic
