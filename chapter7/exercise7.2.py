import math

while True:
    string_val = input("Inserire espressione: ")
    if(string_val == "done"):
        break
    result = eval(string_val)
    print("risulto: "+str(result))
