import pandas as pd
from User.Hungarian_subfunctions import* 
def check_for_recursion(df):
    count=0
    for c in df.columns:
        res=(df[c] == 0).all()
        if(res==False):
            print(res,"HERE",c)
            count=count+1
    return count

#Do row  transformation on all rows,then check for zeroes
#If noot then do all column trannsformations and checck for zeroes
#Check for atleast one zero-.If no 0 start the function again
#if yes->Send for check for unique zeros

def Transform(df,Assigned):
    M=check_for_recursion(df)
    if df.empty==False or M>0:#Condition to avoid infinite loops iin reccurssion
        print(df.size)
        df=changerow(df)
        t=checkforzeros(df)
        
        if t==True:
            assignment(df,Assigned)
            
        else:
            df=changecolumn(df)
            M=check_for_recursion(df)
            if len(df.index)<2 or len(df.columns)<2 or M==0:print("DONE")#Condition to avoid infinite loops iin reccurssion
            else:
                t=checkforzeros(df)
                if(t==True):
                    assignment(df,Assigned)
                else:
                    Transform(df,Assigned)
        print(df)
    else:
        print("DONE")
        return df
#Check for unique zeros by row
#Delete that row and column
#Check for atleast one zero

#Check for unique zeros by column
#Delete that   row and column
#Check for atleast one zero->If yes start the same function again

def assignment(df,Assigned):
    M=check_for_recursion(df)
    if df.empty is False  or M>0:#Condition to avoid infinite loops iin reccurssion
        df=rowcheck(df,Assigned)
        df=columncheck(df,Assigned)
        t=checkforzeros(df)
        M=check_for_recursion(df)
        if len(df.index)<2 or len(df.columns)<2 or M==0:print("DONE")# Condition to avoid infinite loops iin reccurssion
        else:
            if(t==True):
                assignment(df,Assigned)
            else:
                Transform(df,Assigned)
    else:
        print("DONE")
        return df
            