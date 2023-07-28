import re

# define reference values for categorical data
types = ['APARTMENT', 'HOUSE']
regions = ['Brussels', 'Flanders', 'Wallonie']
provinces = ['Antwerp', 'Brussels', 'East Flanders', 'Flemish Brabant', 'Hainaut', 'Limburg', 
             'Liège', 'Luxembourg', 'Namur', 'Walloon Brabant', 'West Flanders']
districts = ['Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne', 'Brugge', 'Brussels', 
             'Charleroi', 'Dendermonde', 'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 
             'Halle-Vilvoorde', 'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven', 
             'Liège', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons', 'Mouscron', 
             'Namur', 'Neufchâteau', 'Nivelles', 'Oostend', 'Oudenaarde', 'Philippeville', 
             'Roeselare', 'Sint-Niklaas', 'Soignies', 'Thuin', 'Tielt', 'Tongeren', 'Tournai', 
             'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']
conditions = ['NEW|AS_NEW', 'JUST_RENOVATED', 'GOOD', 'TO_BE_DONE_UP', 
              'TO_RENOVATE', 'TO_RESTORE', 'UNKNOWN']
epcscores = ["A", "B", "C", "D", "E", "F", "G"]


# functions
def check_type(type):
    """ Check if property type is in the list of property types,
        Convert to all upper case before the check,
        Return status and updated type """
    is_type = False
    type = type.upper() 
    if type in types: 
        is_type = True
    return is_type, type

def check_region(region):
    """ Check if region is in the list of regions,
        Capitalize the case before the check,
        Return status and updated region """
    is_region = False
    region = region.capitalize()
    if region in regions: 
        is_region = True
    return is_region, region

def check_province(province):
    """ Check if province is in the list of provinces,
        Convert to title case before the check,
        Return status and updated province """
    is_province = False
    province = province.title()
    if province in provinces: is_province = True
    return is_province, province

def check_district(district):
    """ Check if district is in the list of districts,
        Capitalize the case before the check,
        Return status and updated district """
    is_district = False
    district = district.capitalize()
    if district in districts: is_district = True
    return is_district, district

def check_postal_code(code):
    """ Check if the input is a legitimate postal code,
        Return status """
    is_postal_code = False
    if re.match(r"^[1-9][0-9]{3}$", code): is_postal_code = True
    return is_postal_code

def check_condition(condition):
    """ Check if condition is in the list of conditions,
        Convert to upper case and replace spaces with underscores before check,
        Return status and updated condition """
    is_condition = False
    condition = condition.upper().replace(" ", "_")
    if condition in conditions: is_condition = True
    return is_condition, condition

def check_epcscore(epcscore):
    """ Check if epsScore is in the list of epcScores,
        Convert to upper case before check,
        Return status and updated score """
    is_epcscore = False
    epcscore = epcscore.upper()
    if epcscore in epcscores: is_epcscore = True
    return is_epcscore, epcscore

def is_number(number):
    """ Check if the variable is a number: float or integer,
        Return status """
    is_number = False
    if type(number) in [float, int]: is_number = True
    return is_number


# main function
def check_input_data(data_dict):
    """ Performs checks of the input data:
        - Normalizes some categorical values,
        - Checks some numerical values to be other than zero,
        - Compiles dictionary with error messages per data entry
        Returns: status, error dictionary, updated property data dictionary """
    
    status = 200
    # 200 - OK, 204 - no content, 206 - partial content, 
    # 400 - bad request, 404 - not found, 
    # 406 - not acceptable, 421 - misdirected request
    errors = dict()
    
    for key, value in data_dict.items():
        if key == "type":
            is_type, type_fixed = check_type(value)
            if is_type:
                data_dict[key] = type_fixed
            else:
                errors[key] = "Please, fix property type: has to be HOUSE or APARTMENT"
        elif key == "region":
            is_region, region_fixed = check_region(value)
            if is_region:
                data_dict[key] = region_fixed
            else:
                errors[key] = "Please, fix the region: Brussels, Flanders, or Wallonie"
        elif key == "province":
            is_province, province_fixed = check_province(value)
            if is_province:
                data_dict[key] = province_fixed
            else:
                errors[key] = "Please, fix the province"
        elif key == "district":
            is_district, district_fixed = check_district(value)
            if is_district:
                data_dict[key] = district_fixed
            else:
                errors[key] = "Please fix the district"
        elif key == "postalCode":
            is_postal_code = check_postal_code(value)
            if not is_postal_code:
                errors[key] = "Please, fix the postal code: 4 digit string"
            else:
                continue
        elif key == "bedroomCount":
            if not is_number(value):
                errors[key] = "Bedroom count has to be a number"
            elif value <= 0:
                errors[key] = "Bedroom count can't be zero or negative value"
            else:
                continue
        elif key == "netHabitableSurface":
            if not is_number(value):
                errors[key] = "Habitual surface has to be a number"
            elif value <= 0:
                errors[key] = "Habitual surface can't be zero or negative value"
            else:
                continue
        elif key == "condition":
            is_condition, condition_fixed = check_condition(value)
            if is_condition:
                data_dict[key] = condition_fixed
            else:
                errors[key] = "Please, fix property condition"
        elif key == "epcScore":
            is_epcscore, epcscore_fixed = check_epcscore(value)
            if is_epcscore:
                data_dict[key] = epcscore_fixed
            else:
                errors[key] = "Please, fix epcScore: A to G (single letter, upper case)"
        elif key == "bathroomCount":
            if not is_number(value) or value < 0:
                errors[key] = "Bathroom count has to be a number: 0 or greater"
            elif value == 0 and data_dict["showerRoomCount"] == 0:
                errors[key] = "Bathroom count or shower room count: One has to be greater than zero"
            else:
                continue
        elif key == "showerRoomCount":
            if not is_number(value) or value < 0:
                errors[key] = "Shower room count has to be a number: 0 or greater"
            elif value == 0 and data_dict["bathroomCount"] == 0:
                errors[key] = "Shower room count or bathroom count: One has to be greater than zero"
            else:
                continue
        elif key == "toiletCount":
            if not is_number(value) or value < 0:
                errors[key] = "Toilet count has to be a number: 1 or greater"
            elif value == 0:
                errors[key] = "Toilet count has to be greater than zero"
            else:
                continue
        elif key == "hasGarden":
            if value and data_dict["gardenSurface"] == 0:
                errors[key] = "Please, provide garden surface or change value to false"
            elif not value and data_dict["gardenSurface"] > 0:
                errors[key] = "Please, change value to true or adjust garden surface to zero"
            else:
                continue
        elif key == "hasTerrace":
            if value and data_dict["terraceSurface"] == 0:
                errors[key] = "Please, provide terrace surface or change value to false"
            elif not value and data_dict["terraceSurface"] > 0:
                errors[key] = "Please, change value to true or adjust terrace surface to zero"
            else:
                continue
        elif key == "gardenSurface":
            if not is_number(value) or value < 0:
                errors[key] = "Garden surface has to be a number: zero or greater"
            elif value == 0 and data_dict["hasGarden"]:
                errors[key] = "Please, adjust garden surface or set hasGarden to false"
            elif value > 0 and not data_dict["hasGarden"]:
                errors[key] = "Please, adjust to zero or set hasGarden to true"
            else:
                continue
        elif key == "terraceSurface":
            if not is_number(value) or value < 0:
                errors[key] = "Terrace surface has to be a number: zero or greater"
            elif value == 0 and data_dict["hasTerrace"]:
                errors[key] = "Please, adjust terrace surface or set hasTerrace to false"
            elif value > 0 and not data_dict["hasTerrace"]:
                errors[key] = "Please, adjust to zero or set hasTerrace to true"
            else:
                continue
        elif key == "land":
            if not is_number(value) or value < 0:
                errors[key] = "Land has to be a number: zero or greater"
        else:
            continue
    
    # adjust status according to errors length
    if len(errors) > 0: 
        status = 400
        errors["status"] = status
        errors["description"] = "Bad request"

    return status, errors, data_dict
