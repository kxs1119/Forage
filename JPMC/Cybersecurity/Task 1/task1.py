import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    # read the file 
    df = pd.read_csv(file)
    return df

def exercise_1(df):
    # put column names in a list
    df_list = []
    for cols in df.columns:
        df_list.append(cols)
    return df_list
   
def exercise_2(df, k):
    # returning the first k rows
    rows = df.head(k)
    return rows
def exercise_3(df, k):
    # passing a random sample of k data from the df
    sample = df.sample(k)
    return sample

def exercise_4(df):
    # Return a list of the unique transaction types.
    types = df.type.unique()
    return types

def exercise_5(df):
    # Return a Pandas series of the top 10 transaction destinations with frequencies.
    # needs to be a count of the transactions that denotes to frequencies
    des_freq = df['nameDest'].value_counts().head(10)
    return des_freq
def exercise_6(df):
    # Return all the rows from the dataframe for which fraud was detected.
    fraud_rows = []
    for i, rows in df.iterrows():
        if rows['isFraud'] == 1:
            fraud_rows.append(rows)
    return fraud_rows

def exercise_7(df):
    # Bonus. Return a dataframe that contains the number of distinct destinations that each source has interacted with to, sorted in descending order. 
    pass
def visual_1(df):
    def transaction_counts(df):
        # TODO
        return df['type'].value_counts()
            
    def transaction_counts_split_by_fraud(df):
        # TODO
        return df.groupby(by=['type','isFraud']).size()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transactions')
    axs[0].set_xlabel('Trasactions types')
    axs[0].set_ylabel('Frequency')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Fraud Detection Occurences')
    axs[1].set_xlabel('Fraud type')
    axs[1].set_ylabel('Frequency')
    fig.suptitle('Visual 1')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return

def visual_2(df):
    def query(df):
    cash_out = df[df['type']=='CASH_OUT'] # extracting the types that are equal to the given subject
    return cash_out[['oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']] # returning the types within other columns

    plot = query(df).plot.scatter(x='newbalanceOrig',y='newbalanceDest') # creating thhe scatter plot with origin at x and destination at y
    plot.set_title('Origin account balance delta v')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    plt.show()
    return

def exercise_custom(df):
    labels = []
    for i in df['type'].unique():
        labels.append(i)
    return df['type'].value_counts(),labels
    
def visual_custom(df):
    types,label = exercise_custom(df)
    fig,ax = plt.subplots()
    ax.pie(types,labels=label,
           shadow=True, autopct='%1.1f%%')