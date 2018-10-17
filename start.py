#############
#Main script#
#############

#CCA Allocation v1.0#

import timeit
import os

import mod_data as modD
import mod_allocation as modA
import mod_presentation as modP

from class_data import *

#variables#
config_file = "Config file.txt"

def main(config_file):
    """
    """

    final_dic, CCA_dic = {}, {}

    #Phase 1 Data#
    config_vars = modD.configure_variables(config_file) #config_vars
    file = config_vars["file names"]["unallocated"] #get name of xlsx file
    master_list = modD.extract_data(file, config_vars) #extract data

    print("Extracting individual sheets...")
    LOC = sheetdata("list_of_choices", modD.data_to_LOC(master_list)) #all indiv sheets
    merit = sheetdata("list_of_merits", modD.data_to_merit(master_list))
    MEP = sheetdata("MEP_students", modD.data_to_MEP(master_list))
    DSA = sheetdata("DSA_students", modD.data_to_DSA(master_list))
    quota = sheetdata("CCA_quota", modD.data_to_quota(master_list))
    psymo = sheetdata("psychomotor", modD.data_to_psychomotor(master_list))

    list_of_CCA = [] #get a list of CCAs
    for key, value in config_vars["data formats"].items():
        list_of_CCA.append(key)
    del list_of_CCA[0:6]

    CCA_ranking = {} #dic of all CCAs
    for cca in list_of_CCA:
        CCA_ranking[cca] = modD.data_to_CCA(master_list, cca)

    print("Phase 1: Data extraction, complete\n")

    #Phase 2 Allocation#
    print("Assigning by score...")
    final_dic, CCA_dic = modA.p2_assignDSA(DSA, final_dic, CCA_dic)
    for rank in ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9"]:
        final_dic, CCA_dic, CCAs_left = modA.p2_assignUnderQuota(quota, psymo, CCA_ranking, MEP, LOC, rank, final_dic, CCA_dic, config_vars) #assign under quota
        for CCA in CCAs_left:
            nameCat = modD.data_to_nameCat(LOC, quota, rank, CCA)
            scorelist = modA.p2_calculate_score(CCA, nameCat, psymo, CCA_ranking, MEP, config_vars)
            final_dic, CCA_dic = modA.p2_allocateByScore(CCA, nameCat, quota, rank, scorelist, final_dic, CCA_dic)
    merit_dic, merit_CCA_dic = modA.p2_assignMerit(merit)
            

    print("Phase 2: Allocation by score, complete\n")

    
    #Phase 3 Allocation#
    print("Assigning remainder...")
    final_dic, CCA_dic = modA.p3_allocateRemainder(quota, master_list, CCA_dic, final_dic)

    for rank in [0, "LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9", 10]:
        count = 0 #test for rank count
        for name, data in final_dic.items():
            if data["rank"] == rank:
                count  = count + 1
            else:
                pass
        print(rank, count)
    print("Phase 3: Allocation of remainder, complete\n")

    #Phase 4 Allocation#
    print("Reassigning...")
    final_dic, CCA_dic = modA.p4_reassignment(LOC, quota, psymo, CCA_ranking, MEP, final_dic, CCA_dic, config_vars)

    for rank in [0, "LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9", 10]:
        count = 0 #test for rank count
        for name, data in final_dic.items():
            if data["rank"] == rank:
                count  = count + 1
            else:
                pass
        print(rank, count)
    print("Phase 4: Reassignment, complete\n")

    #Phase 5 Allocation#
    print("Writing report...")
    #modP.final_report(CCA_dic)
    modP.p5_allocated(final_dic, CCA_dic, CCA_ranking, config_vars)

    os.makedirs("CCA excel sheets")
    os.makedirs("Class excel sheets")
    nameClass = modD.data_to_nameClass(master_list)
    for CCA, data in CCA_dic.items():
        modP.p5_CCAxlsx(final_dic, CCA_dic, merit_CCA_dic, CCA, nameClass, config_vars)
    for CCA, name in merit_CCA_dic.items():
        modP.p5_meritCCAxlsx(merit_dic, merit_CCA_dic, CCA, nameClass, config_vars)
    className = {}
    for name, Class in nameClass.items():
        try:
            lst = className[Class]
            lst.append(name)
            className[Class] = lst
        except:
            className[Class] = [name]
    for Class, names in className.items():
        modP.p5_classxlsx(final_dic, CCA_dic, merit_dic, Class, className, config_vars)
    
    modP.final_report(final_dic,list_of_CCA)
    

    print("Phase 5: Presentation, complete\n")

    print("All complete")
