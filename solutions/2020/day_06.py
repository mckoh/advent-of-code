
# %%
from functions.functions import get_split_data
data = get_split_data(year=2020, day=6, typ="str")

class QuestionEvaluator:
    
    def __init__(self, data=data):
        
        self.data = data
        
    def count_equal(self):
        
        import re
        from string import ascii_lowercase
        
        groups = self.return_groups()
        
        group_values = list()
        
        for group in groups:
            n = len(group)
            feedback = ""
            for person in group:
                feedback += "".join(sorted(person))
            
            count = 0
            for char in ascii_lowercase:
                if len(re.findall(char, feedback)) == n:
                    count += 1
            
            group_values.append(count)        
            
        return sum(group_values)
    
    def count_equal_part1(self):
        
        import re
        from string import ascii_lowercase
        
        groups = self.return_groups()
        
        group_values = list()
        
        for group in groups:
            n = len(group)
            feedback = ""
            for person in group:
                feedback += "".join(sorted(person))
            
            count = 0
            for char in ascii_lowercase:
                if len(re.findall(char, feedback)) > 0 :
                    count += 1
            
            group_values.append(count)        
            
        return sum(group_values)
    
    def return_groups(self):
        groups = list()
        for element in "\n".join(data).replace("\n\n", "~").split("~"):
            groups.append(element.split("\n"))
        return groups

# %%
# Part 1
qr = QuestionEvaluator()
qr.count_equal()

# %%
# Part 2
