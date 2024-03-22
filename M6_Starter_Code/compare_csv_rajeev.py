import pandas as pd
df1  = pd.read_csv("collected_data.csv")
df2 = pd.read_csv("final_output.csv")
# diff_df  = pd.concat([df1,df2]).drop_duplicates(keep=False)
# diff_df.to_csv("diff.csv", index=False)
merged_df = pd.merge(df1,df2, how = 'outer', indicator=True)
diff_df = merged_df[merged_df['_merge']!= 'both']
diff_df.drop(columns='_merge',inplace=True)
print (diff_df)