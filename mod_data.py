#############
#data module#
#############

import openpyxl

import timeit


def configure_variables(config_file):
    """
    """

    print("configuring variables...")
    
    dic = {} #will return to config_vars

    try: #test (and open) file
        fp = open(config_file, "r")
    except IOError:
        print(e)
        print("The config file has been moved or renamed.")
        print("Please return it back to this directory or rename it to 'Config file'.")
    data = fp.readlines()
    fp.close()

    section = "None" #different section = different data format

    to_add = {}
    for line in data: #each line
        if line[:2] == "--" and line[8:].strip("\n") != section: #new section?
            section = line[8:].strip("\n")
            to_add = {}
        elif line[:2] == "--" and line[8:].strip("\n") == section: #end of section?
            dic[section[:-2]] = to_add
            section = "None"
            to_add = {}
        else:
            if section == "data formats--": #section specifying data form
                elements = line.strip("\n").split(":")
                elements.append(elements[1].split(","))
                del elements[1]
                areas = []
                
                for i in range(len(elements[1])): #for each container
                    var = elements[1][i].split("-")
                    areas.append({"slice_coords":[var[0], var[1]], "ID_header":var[2]})
                    
                elements.append(areas)
                del elements[1]

                to_add[elements[0]] = elements[1]
            elif section == "file names--": #section specifying file names
                elements = line.strip("\n").split(":")
                to_add[elements[0]] = elements[1]
            elif section == "None":
                pass
            else:
                print("Error occured on line 50: section '{}' not found".format(section))
                
    return dic
            
            
def extract_data(file, config_vars):
    """
    """

    print("extracting data...")
    
    dic = {} #will return to master_list
    
    try: #test (and open) file
        fp = open(file, "r")
    except IOError as e:
        print(e)
        print("File: '{}' not found. Please check the config file.".format(file))
        

    wb = openpyxl.load_workbook(file) #open workbook
    sheet_names = wb.sheetnames #get names of all sheets

    for name in sheet_names: #for every sheet in the workbook
        sheet = wb[name] #define the worksheet
        sheet_list = []

        areas = config_vars["data formats"][name]

        sheet_list = extract_sheet(file, name, areas) #see extract_sheet

        dic[name] = sheet_list #define sheet as a list of data containers

    fp.close()

    return dic


def extract_sheet(file, sheetname, areas):
    """
areas: [{slice_coords:[], ID_header:""]
    """

    lst = [] #will return to sheet_data

    try: #test (and open) file
        fp = open(file, "r")
    except IOError as e:
        print(e)
        print("File: '{}' not found. Please check the config file.".format(file))

    wb = openpyxl.load_workbook(file) #open workbook

    try: #test (and open) spreadsheet
        ws = wb[sheetname]
    except KeyError as e:
        print(e)
        print("Sheet: '{}' not found. Please check the config file.".format(sheetname))

    for i in areas: #for each area
        area = ws[i["slice_coords"][0]:i["slice_coords"][1]]
        area_dic = {}
        ID_value = ""

        for row in area: #for each row in area
            row_dic = {}

            for cell in row: #for each cell in row
                col_letter = cell.column #this be column of cell
                header = ws[col_letter + i["slice_coords"][0][1:]].value #this be header value of cell
                if header == i["ID_header"]: #if its the ID column
                    ID_value = cell.value #get the ID value
                else:
                    row_dic[header] = cell.value #define column of ID as value

            area_dic[ID_value] = row_dic #define ID of area as column

        lst.append(area_dic) #add to list of areas

    fp.close()    
    return lst
            

def data_to_LOS(dic):
    """
    """

    final_lst = []

    dic_classlist = dic["classlist"][0]

    for key, value in classlist.items():
        final_lst.append(key)

    del final_lst[0]

    return final_lst

def data_to_LOC(dic):
    """
    """

    final_dic = {} #will return to list_of_firsts
    
    dic_choices = dic["choices"][0] #the relevant sheet

    pdic = {"LO1":"CORE1", "LO2":"CORE2", "LO3":"CORE3", "LO4":"CORE4", "LO5":"CORE5", "LO6":"CORE6", "LO7":"CORE7", "LO8":"CORE8", "LO9":"CORE9"}
    qdic = {}
    for key, value in pdic.items():
        for NRIC, choices in dic_choices.items():
            qdic[NRIC] = choices[value]
        final_dic[key] = qdic
        qdic = {}

    return final_dic


def data_to_MEP(dic):
    """
    """

    final_lst = []

    dic_MEP = dic["MEP"][0]

    for key, value in dic_MEP.items():
        final_lst.append(key)

    del final_lst[0]
  
    return final_lst
    
    
def data_to_DSA(dic):
    """
    """

    final_dic = {} #will return to DSA_students

    dic_DSA = dic["DSA"][0] #the relevant sheet

    for key, value in dic_DSA.items():
        final_dic[key] = value["Sports"]

    del final_dic["Name"]
    
    return final_dic


def data_to_quota(dic):
    """
    """

    final_dic = {} #will return to CCA_quota

    dic_quota = dic["ccaquota"] #the relevant sheet

    for dic in dic_quota: #SPORTS, UNIFORMED GROUPS, etc.
        groupname = ""
        groupdic = {}
        for key, value in dic.items(): #SPORTS: {}
            if value[None] == None:
                final_dic[groupname] = groupdic
                groupname = key
                groupdic = {}
            else:
                groupdic[key] = value["QUOTA"]
        final_dic[groupname] = groupdic

    del final_dic[""]
    
    return final_dic


def data_to_psychomotor(dic):
    """
    """

    final_dic = {} #will return to psychomotor

    dic_psymo = dic["psychomotor"][0] #the relevant sheet

    for key, value in dic_psymo.items():
        del value["AGE"]
        final_dic[key] = value

    del final_dic["Name"]

    return final_dic


def data_to_CCA(dic, CCA):
    """
    """

    final_dic = {}

    dic_CCA = dic[CCA][0]

    for key, value in dic_CCA.items():
        try:
            del value["Class"]
        except:
            del value["CLASS"]
        final_dic[key] = value

    return final_dic


def data_to_nameCat(dic, quota, CCA):
    """
    """

    dic_quota = quota

    for category, dic_CCAs in dic_quota.items():
        for cca, quota in dic_CCAs.items():
            if cca == CCA:
                return category
            else:
                pass
    
    


#Test zone#
##start = timeit.default_timer()
##config_vars = configure_variables("Config file.txt")
##stop = timeit.default_timer()
##print("Runtime: ", stop-start)
##print("")
##
##start1 = timeit.default_timer()
##master_list = extract_data("unallocated.xlsx", config_vars)
##stop1 = timeit.default_timer()
##print('Runtime: ', stop1-start1)
##print("")
##
##start2 = timeit.default_timer()
##list_of_firsts = data_to_LOF(master_list)
##stop2 = timeit.default_timer()
##print('Runtime: ', stop2-start2)
##print("")
##
##start3 = timeit.default_timer()
##DSA_students = data_to_DSA(master_list)
##stop3 = timeit.default_timer()
##print('Runtime: ', stop3-start3)
##print("")
##
##print('Total runtime: ', stop3-start)
