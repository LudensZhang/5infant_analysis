import pandas as pd
import numpy as np
from plotnine import*

abundance =  pd.read_csv('../8folds/abundance.csv', index_col = 0)
file_report = pd.read_csv('../file_report.txt', sep = '\t', index_col = 1)['sample_alias']
metadata = pd.read_csv('../8folds/metadata.csv', index_col = 0)
file_report = file_report.loc[set(metadata.index) & set(file_report.index)]

# Filter samples that collected along complete series
file_report = file_report.str.split('-', expand = True)
samples_group_count = file_report[file_report[1] != 'M'].groupby(0).count()
target_index = samples_group_count[samples_group_count == 5].dropna().index    # 120 samples

report_reindex = file_report.reset_index().set_index(0)
target_id = report_reindex[report_reindex[1] != 'M'].loc[target_index]['run_accession']
target_metadata = report_reindex.set_index('run_accession', drop = True).loc[target_id]
target_metadata.rename(columns = {1: 'Env'}, inplace = True)
target_abundance = abundance[target_metadata.index]

# Group the trajectory
trajectory_1 = ['Bifidobacterium',
                'Enterococcus',
                'Lactobacillus',
                'Streptococcus',
                'Enterobacteriaceae',
                'Rothia',
                'Veillonella']

trajectory_2 = ['[Ruminococcus]',
                '[Eubacterium]',
                'Eggerthella',
                'Fusobacterium',
                'Haemophilus']

trajectory_3 = ['Bacteroides',
                'Faecalibacterium',
                'Roseburia',
                'Akkermansia',
                'Prevotella',
                'Ruminococcus',
                'Lachnospiraceae']

trajectory_4 = ['Methanobrevibacter',
                'Coriobacteriaceae',
                'Desulfovibrio',
                'Christensenellaceae',
                'cc_115',
                'S24-7',
                'Catenibacterium']

# Sum each age group
def SumByAge(age):
    age_id = target_metadata[target_metadata['Env'] == age].index
    return(target_abundance[age_id].sum(axis = 1))

age_df = pd.concat([SumByAge('NB'), 
                    SumByAge('4M'),
                    SumByAge('12M'),
                    SumByAge('3Y'),
                    SumByAge('5Y')], ignore_index = True, axis = 1)

age_df.columns = ['NB', '4M', '12M', '3Y', '5Y']

# Calculate each genera in all samples
def CalculateTrajectory(trajectory):
    trajectory_df = pd.DataFrame(np.zeros((len(trajectory), 5)), 
                                 columns = ['NB', '4M', '12M', '3Y', '5Y'],
                                 index = trajectory)
    for genera in trajectory:
        for tax in target_abundance.index:
            if genera in tax:
                trajectory_df.loc[genera] += age_df.loc[tax]

    return trajectory_df
        
    
plot_df_1 = CalculateTrajectory(trajectory_1)
plot_df_2 = CalculateTrajectory(trajectory_2)
plot_df_3 = CalculateTrajectory(trajectory_3)
plot_df_4 = CalculateTrajectory(trajectory_4)

# Plot
