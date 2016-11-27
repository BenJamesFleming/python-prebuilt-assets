# Import Single Output Class
import sys
sys.path.append("../")
from SingleOutput import SingleOutput

output_string="This String Will Output {0} More Times, Loop #{1}"
amount_to_loop=10000
SingleOutput(output="\n\n  This Programm Will Output A String "+str(amount_to_loop)+" Time\n  Using The Single Output Function\n")

for x in range(0,amount_to_loop):
    temp_str=output_string
    temp_str=temp_str.format(str(int(amount_to_loop-x-1)), str(str(x+1)+"/"+str(amount_to_loop)))
    SingleOutput(output=temp_str)

input("Program Is Paused")
