#Check if each row and column has atleast one zero in it

#ROW
def checkforzeros(df):
    min_values_row = df.min(axis=1)
    min_values_col = df.min()
    return max(sum(min_values_row),sum(min_values_col))==0
#Changing the column by subtracting the min value(per column) from all the elements in the column
def changecolumn(df):
    for c in df.columns:
        for i  in df.index:
            x=df.at[i,c]
            p= df[c].min()
            print( )
            y=x-p
            df.at[i,c]=y
    print(df,"After column transformation")
    return df
#Changing the row by subtracting the min value(per row) from all the elements in the row
def changerow(df):
    min_value_row = df.min(axis=1)
    for col in df.columns:
        df[col]=df[col]-min_value_row
        
    print(df,"After row transformation")
    return df
#Find the row with  exactly one zero and its place in the row
def rowcheck(df,Assigned):
    c=0;
    pos=0;
    
    for p in df.index:
        print("IN ROW",p)
        c=0
        for i in df.columns:
            x=df.at[p,i]
            print(x,"Element")
            if(x==0):
                #print("Added To",c,x)
                c=c+1;
                pos=i;
        if(c==1):
            print("meow",c,p,pos)
            Assigned[p]=pos
            df = df.drop(p, axis=0)
            df = df.drop(pos, axis=1)
            print(df,"After checking for zeros in row transformation",c)
        
    print(df,"After checking for zeros in row transformation full loop shit",c)
    return df
#Find the column with exactly one zero and its place in the column

def columncheck(df,Assigned):
    pos=0;
    for p in df.columns:
        print(p,"ROw  no")
        c=0;
        for i in df.index:
            x=df.at[i,p]
            print(x,"element")
            if(x==0):
                c=c+1;
                pos=i;
        if(c==1):
            print(c,p,pos,"Star Element")
            df = df.drop(p, axis=1)
            df = df.drop(pos, axis=0)
            Assigned[pos]=p
            print(df,"After checking for zeros in column transformation")
            return df
    print(df,"After checking for zeros in column transformation")
    return df
