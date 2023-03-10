import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def SIMILARITY_VECTOR(df):
    # combine all strings:
    df2 = df.drop(['id','User_id','Email','Phone','Email','Skill_certificates','ID_Proof','Timestamp','Type_of_User','Pair_Found','Paired_with'],axis=1)
    print(df2.head())
    # ## Add all columns into one so that it forms a STRING
    df2['data'] = df2[df2.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1)
    print(df2['data'].head())
    ## Apply vectorization to that columns
    vectorizer = CountVectorizer()
    vectorized = vectorizer.fit_transform(df2['data'])
    print(vectorizer.get_stop_words())
    # Apply a Similarity Cosine based on thier vectorization
    similarities = cosine_similarity(vectorized)
    print(similarities)
    return similarities
def FORMING_DATAFRAME(similarities,df,original):
    df = pd.DataFrame(similarities, columns=df['Name'], index=df['Name']).reset_index()
    df = df.loc[df.index.drop_duplicates()]
    print(df.head())
    #### Making our rows=Requests and Columns=Volunteers
    # Divide the dataframe into two groupd  based on "TYPE"
    gr = original.groupby('Type_of_User')
    df1=gr.get_group('Volunteer')
    df1
    df2=gr.get_group('Request')
    df2
    #For Columns
    #for Request
    for i in df2['Name']:
        c=-1
        for  j in df.columns:
            c=c+1
            if(i==j):
                df=df.drop(j,axis=1)
                print(j)
    # For ROWS
    # for Volunteer
    for i in df.index:
        c=-1
        for j in df.columns:
            if(j==df.at[i,'Name']):
                print(i)
                df=df.drop(i,axis=0)
                break
    df = df.drop("Name", axis=1)
    df
    #As we want to maxmiaze the Similarity,We  first  subtract the dataframme max  from the complete Datafame
    max_by_columns = df.max(axis=1)
    df_max = max(max_by_columns)
    print(df_max)
    df = df_max-df
    df
    return df