import pandas as pd
from User.Hungarian_subfunctions import* 


#Do row  transformation on all rows,then check for zeroes
#If noot then do all column trannsformations and checck for zeroes
#Check for atleast one zero-.If no 0 start the function again
#if yes->Send for check for unique zeros

def Transform(df,Assigned):
    if df.empty==False:#Condition to avoid infinite loops iin reccurssion
        print(df.size)
        df=changerow(df)
        t=checkforzeros(df)
        
        if t==True:
            assignment(df,Assigned)
            
        else:
            df=changecolumn(df)
            if len(df.index)<2 or len(df.columns)<2:print("DONE")#Condition to avoid infinite loops iin reccurssion
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
    if df.empty is False:#Condition to avoid infinite loops iin reccurssion
        df=rowcheck(df,Assigned)
        df=columncheck(df,Assigned)
        t=checkforzeros(df)
        if len(df.index)<2 or len(df.columns)<2:print("DONE")# Condition to avoid infinite loops iin reccurssion
        else:
            if(t==True):
                assignment(df,Assigned)
            else:
                Transform(df,Assigned)
    else:
        print("DONE")
        return df
            