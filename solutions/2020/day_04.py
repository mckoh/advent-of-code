
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=4, typ="str")

class PassportEngine:

    def __init__(self, data):
        self.data = data

    def  _seperate_passports(self):
        """Takes the input data and turns them into a list of passport
        strings which are then returned.
        """
        
        return "\n".join(self.data).replace("\n\n", "~").replace("\n", " ").split("~")

    def _passport_to_dict(self, passport):
        """Converts a given passport string into a passport dictionary
        and returns it.
        """
        
        output_dict = dict()
        for item in passport.split(" "):
            key = item.split(":")[0]
            value = item.split(":")[1]
            output_dict[key] = value
        return output_dict
    
    def _process_passports(self):
        """Iterates over list of passports and returns a list of 
        passport dictionaries.
        """
        
        p = self._seperate_passports()
        pp = list()
        for passport in p:
            pp.append(self._passport_to_dict(passport=passport))
        return pp
    
    def count_valid(self, *args, **kwargs):
        """Processes passport by passport from a passport dictionary
        and validates each passport by applying each field's validation
        rule
        """
        
        pp = self._process_passports()
        valid = 0
        for p in pp:
            
            if (
                self._val_byr(p, *args, **kwargs) and 
                self._val_cid(p, *args, **kwargs) and 
                self._val_ecl(p, *args, **kwargs) and 
                self._val_iyr(p, *args, **kwargs) and 
                self._val_hcl(p, *args, **kwargs) and
                self._val_hgt(p, *args, **kwargs) and 
                self._val_eyr(p, *args, **kwargs) and 
                self._val_pid(p, *args, **kwargs)
            ):
                valid += 1

        return valid
    
    # Below you can find all passport field validation rules
    
    # DONE
    def _val_byr(self, passport, optional=False, part=2):
        """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
        
        key = "byr"
        if key in passport.keys():
            if part==2:
                value = passport[key]
                if len(value) == 4:
                    if int(value) >= 1920 and int(value) <= 2002:
                        return True
                    else:
                        return False
                else:
                    return False
            elif part == 1:
                return True
        else:
            return optional
    
    # DONE
    def _val_iyr(self, passport, optional=False, part=2):
        """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
        
        key = "iyr"
        if key in passport.keys():
            if part==2:
                value = passport[key]
                if len(value) == 4:
                    if int(value) >= 2010 and int(value) <= 2020:
                        return True
                    else:
                        return False
                else:
                    return False
            elif part==1:
                return True
        else:
            return optional
    
    # DONE
    def _val_eyr(self, passport, optional=False, part=2):
        """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
        
        key = "eyr"
        if key in passport.keys():
            if part==2:
                value = passport[key]
                if len(value) == 4:
                    if int(value) >= 2020 and int(value) <= 2030:
                        return True
                    else:
                        return False
                else:
                    return False
            elif part==1:
                return True
        else:
            return optional
    
    # DONE
    def _val_hgt(self, passport, optional=False, part=2):
        """hgt (Height) - a number followed by either cm or in:
            
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        """
        
        key = "hgt"
        if key in passport.keys():
            if part==2:
                measure = passport[key][-2:]
                if measure in ["cm", "in"]:
                    value = int(passport[key][:-2])
                    if measure == "cm":
                        if value >= 150 and value <= 193:
                            return True
                        else:
                            return False
                    elif measure == "in":
                        if value >= 59 and value <= 76:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif part == 1:
                return True
        else:
            return optional
    
    # DONE
    def _val_hcl(self, passport, optional=False, part=2):
        """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
        
        from string import ascii_lowercase, digits
        
        key = "hcl"
        if key in passport.keys():
            if part==2:
                prefix = passport[key][0]
                value = passport[key][1:]
                if prefix == "#":
                    if len(value) == 6:
                        for char in value:
                            if char not in ascii_lowercase + digits:
                                return False
                        return True
                    else:
                        return False
                else:
                    return False
                        
                return True
            elif part == 1:
                return True
        else:
            return optional
    
    # Done
    def _val_ecl(self, passport, optional=False, part=2):
        """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
        
        key = "ecl"
        if key in passport.keys():
            if part==2:
                value = passport[key]
                if len(value) == 3:
                    if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        return True
                    else:
                        return False
                else:
                    return False
            elif part == 1:
                return True
        else:
            return optional
    
    # Done
    def _val_pid(self, passport, optional=False, part=2):
        """pid (Passport ID) - a nine-digit number, including leading zeroes."""
        
        from string import digits
        
        key = "pid"
        if key in passport.keys():
            if part==2:
                value = passport[key]
                if len(value) == 9:
                    for char in value:
                        if char not in digits:
                            return False
                    return True
                else:
                    return False
            elif part == 1:
                return True
        else:
            return optional

    # Done
    def _val_cid(self, passport, optional=True, part=2):
        """cid (Country ID) - ignored, missing or not."""
        
        key = "cid"
        if key in passport.keys():
            return True
        else:
            return optional
        
# %%

def test_birth():
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    pe = PassportEngine(data=data)
    assert pe._val_byr(passport={"byr": "1920"})
    assert pe._val_byr(passport={"byr": "2002"})
    assert pe._val_byr(passport={"byr": "1980"})
    assert not pe._val_byr(passport={"byr": "1910"})
    assert not pe._val_byr(passport={"byr": "2003"})
    assert not pe._val_byr(passport={"byr": "20030"})
    
def test_issue():
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    pe = PassportEngine(data=data)
    assert pe._val_iyr(passport={"iyr": "2010"})
    assert pe._val_iyr(passport={"iyr": "2020"})
    assert pe._val_iyr(passport={"iyr": "2015"})
    assert not pe._val_iyr(passport={"iyr": "2009"})
    assert not pe._val_iyr(passport={"iyr": "2021"})
    assert not pe._val_iyr(passport={"iyr": "20090"})
    
def test_expansion():
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    pe = PassportEngine(data=data)
    assert pe._val_eyr(passport={"eyr": "2020"})
    assert pe._val_eyr(passport={"eyr": "2030"})
    assert not pe._val_eyr(passport={"eyr": "2010"})
    assert not pe._val_eyr(passport={"eyr": "2040"})
    assert not pe._val_eyr(passport={"eyr": "20040"})

def test_height():
    """hgt (Height) - a number followed by either cm or in:
        
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    pe = PassportEngine(data=data)
    assert pe._val_hgt(passport={"hgt": "150cm"})
    assert pe._val_hgt(passport={"hgt": "160cm"})
    assert pe._val_hgt(passport={"hgt": "193cm"})
    assert pe._val_hgt(passport={"hgt": "59in"})
    assert pe._val_hgt(passport={"hgt": "65in"})
    assert pe._val_hgt(passport={"hgt": "76in"})
    assert not pe._val_hgt(passport={"hgt": "45in"})
    assert not pe._val_hgt(passport={"hgt": "90in"})
    assert not pe._val_hgt(passport={"hgt": "140cm"})
    assert not pe._val_hgt(passport={"hgt": "200cm"})

def test_country_id():
    """cid (Country ID) - ignored, missing or not."""
    pe = PassportEngine(data=data)
    assert pe._val_cid(passport={"cid": "AT"})
    assert pe._val_cid(passport={"vid": "AT"})

def test_hair_color():
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
    pe = PassportEngine(data=data)
    assert pe._val_hcl(passport={"hcl": "#123456"})
    assert pe._val_hcl(passport={"hcl": "#abcdef"})
    assert pe._val_hcl(passport={"hcl": "#123avb"})
    assert pe._val_hcl(passport={"hcl": "#abc123"})
    assert not pe._val_hcl(passport={"hcl": "#123ABC"})
    assert not pe._val_hcl(passport={"hcl": "#ABCDEF"})
    assert not pe._val_hcl(passport={"hcl": "123456"})
    assert not pe._val_hcl(passport={"hcl": "#"})
    assert not pe._val_hcl(passport={"hcl": "#1234567"})
    assert not pe._val_hcl(passport={"hcl": "#12345"})
    assert not pe._val_hcl(passport={"vid": "#abc123"})
    
def test_passport_id():
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    pe = PassportEngine(data=data)
    assert pe._val_pid(passport={"pid": "012345678"})
    assert pe._val_pid(passport={"pid": "000000000"})
    assert pe._val_pid(passport={"pid": "112345678"})
    assert not pe._val_pid(passport={"pid": "A12345678"})
    assert not pe._val_pid(passport={"pid": "A1234567A"})
    assert not pe._val_pid(passport={"pid": ""})
    assert not pe._val_pid(passport={"vid": "A12345678"})

def test_eye_color():
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    pe = PassportEngine(data=data)
    assert pe._val_ecl(passport={"ecl": "amb"})
    assert pe._val_ecl(passport={"ecl": "blu"})
    assert pe._val_ecl(passport={"ecl": "brn"})
    assert pe._val_ecl(passport={"ecl": "gry"})
    assert pe._val_ecl(passport={"ecl": "grn"})
    assert pe._val_ecl(passport={"ecl": "hzl"})
    assert pe._val_ecl(passport={"ecl": "oth"})
    assert not pe._val_ecl(passport={"ecl": "ABC"})
    assert not pe._val_ecl(passport={"ecl": "123"})
    assert not pe._val_ecl(passport={"ecl": "othbrn"})
    
test_country_id()
test_hair_color()
test_passport_id()
test_eye_color()
test_height()
test_expansion()
test_issue()
test_birth()

# %%
# Part 1
pe = PassportEngine(data=data)
pe.count_valid(part=1)

# %%
# Part 2
pe = PassportEngine(data=data)
pe.count_valid(part=2)