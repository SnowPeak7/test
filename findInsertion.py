'''
Author: SnowPeak7
Date: 2021-11-01 19:30:29
LastEditTime: 2021-11-01 21:11:22
LastEditors: SnowPeak7
Description: 
FilePath: /02.My_Code/01.Find_insertion/findInsertion.py
Allways remember:Ignorance is fatal
'''


SamPath = '/Users/snowpeak7/Desktop/CHEM_ECO/rice_bgx/03.18_insertion/py.test'

##Generally the SAM file is very big, 'with' can properly 
# handle this because  is contain build in Bufferhandler
count = 1
with open(SamPath,'r') as in_sam:
    for line_sam in in_sam:
        line_sam = line_sam.rstrip()
        flag = int(line_sam.split('\t')[1])
        if (0x2 & flag) != 0:      ##0x2 & flag == 0, means not proper pair
            print(count)
            count += 1
        else:
            print(line_sam.split('\t')[0])
        
