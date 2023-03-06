# Dictionary Concetenation
dict1 = {"Brand": "OnePlus"}
dict2 = {"Name": "Oneplus 8 pro"}
dict3 = {"Year": "2020"}
dict4 = {"Camera": "48mp with HDR and true tone"}

dict5 = {**dict1, **dict2, **dict3, **dict4}

print(dict5)
