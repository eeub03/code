
"""
Created on Sat Oct 12 13:28:49 2019

@author: Joseph Morgan
@name: Grammatical Herding in Python
@version: 0.1a
"""
import src.Herd.Herd as Herd
Herd1 = Herd.Herd()

for i in range(700):
    if Herd1.herd[i].invalid:
        continue
    else:
        print("PHENOTYPE")
        print(Herd1.herd[i].phenotype)