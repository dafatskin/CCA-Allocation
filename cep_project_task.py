#############
#Main script#
#############
#Do something with this
if not os.path.isdir("DirectoryName"):
    os.makedirs("DirectoryName")

if not os.path.isfile('FileName.xlsx'):
    wb = openpyxl.Workbook()  
    dest_filename = 'FileName.xlsx' 
    wb.save(os.path.join('DirectoryName', dest_filename), as_template=False)

#CCA Allocation v1.0#

import timeit

import mod_data as modD
import mod_allocation as modA
import mod_present as modP

from class_data import *

#variables#
config_file = "config_file.txt"

def main(config_file):
    """
    """

    final_dic, CCA_dic = {}, {}

    #Phase 1 Data#
    config_vars = modD.configure_variables(config_file) #config_vars
    file = config_vars["file names"]["unallocated"] #get name of xlsx file
    master_list = modD.extract_data(file, config_vars) #extract data

    print("Extracting individual sheets...")
    LOC = sheetdata("list_of_firsts", modD.data_to_LOC(master_list)) #all indiv sheets
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
    print("Assigning by score")
    final_dic, CCA_dic = modA.p2_assignDSA(DSA, final_dic, CCA_dic)
    for rank in ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9"]:
        final_dic, CCA_dic, CCAs_left = modA.p2_assignUnderQuota(quota, psymo, CCA_ranking, MEP, LOC, rank, final_dic, CCA_dic, config_vars) #assign under quota
        for CCA in CCAs_left:
            nameCat = modD.data_to_nameCat(LOC, quota, rank, CCA)
            scorelist = modA.p2_calculate_score(CCA, nameCat, psymo, CCA_ranking, MEP, config_vars)
            final_dic, CCA_dic = modA.p2_allocateByScore(CCA, nameCat, quota, rank, scorelist, final_dic, CCA_dic)

    print("Phase 2: Allocation by score, complete\n")
    
    #Phase 3 Allocation#
    print("Assigning remainder")
    final_dic, CCA_dic = modA.p3_allocateRemainder(quota, master_list, CCA_dic, final_dic)

    print("Phase 3: Allocation of remainder, complete\n")

    #Phase 4 Allocation#
    print("Reassigning")
    final_dic, CCA_dic = modA.p4_reassignment(final_dic, CCA_dic)

    #Phase 5 Presentation#
    print("Presenting")
    modP.final_report()
    
    

    print(len(final_dic))
##    print(final_dic, "\n", CCA_dic)


    print("All complete")
