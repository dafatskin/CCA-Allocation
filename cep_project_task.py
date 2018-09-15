#############
#Main script#
#############

#CCA Allocation v1.0#

import timeit

import mod_data as modD
import mod_allocation as modA

from class_data import *

#variables#
config_file = "config_file.txt"

def main(config_file):
    """
    """

    final_dic, CCA_dic = {}, {}

    #run data processes#
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
    for key, value in config_vars.items():
        for key, value in value.items():
            list_of_CCA.append(key)
    del list_of_CCA[0:6]
    del list_of_CCA[-1]

    CCA_Ranking = {} #dic of all CCAs
    for cca in list_of_CCA:
        CCA_Ranking[cca] = modD.data_to_CCA(master_list, cca)

    print("data processes complete")

    #Phase 2 Allocation#
    print("Assigning by score")
    final_dic, CCA_dic = modA.p2_assignDSA(DSA, final_dic, CCA_dic)
    for rank in ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6", "LO7", "LO8", "LO9"]:
        final_dic, CCA_dic, CCAs_left = modA.p2_assignUnderQuota(quota, LOC, rank, final_dic, CCA_dic) #assign under quota
    #=modA.calculate_score()

    print(final_dic, "\n", CCA_dic)

    print("Phase 1 Allocation complete")


    print("All complete")


start = timeit.default_timer()
main(config_file)
stop = timeit.default_timer()
print("Runtime: ", stop-start)
