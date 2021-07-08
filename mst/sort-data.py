import os
import pandas as pd


if __name__ == '__main__':
    os.mkdir('5-years')
    os.mkdir('12-months')
    os.mkdir('5-years/cesarean-section')
    os.mkdir('5-years/verginal-delivery')
    os.mkdir('12-months/cesarean-section')
    os.mkdir('12-months/verginal-delivery')
    
    metadata_withbirth = pd.read_csv('meta_withbirth.csv')
    metadata = pd.read_csv('metadata.csv')
    abundance = pd.read_csv('abundance.csv')
    
    C_index = []
    C_12M_queries = []
    C_5Y_queries = []
    C_sources = []
    
    for i in metadata_withbirth.index:
        if ':C' in metadata_withbirth.loc[i, 'Env']:
            C_index.append(i)
    C_metadata = metadata.loc[C_index]
    C_metadata.columns = ['SampleID', 'Env']
    C_abundance = abundance[C_metadata['SampleID']]
    C_abundance.insert(0, 'Samples', abundance['Samples'])
    
    for i in C_metadata.index:
        if ':5Y' in C_metadata.loc[i, 'Env']:
            C_5Y_queries.append(i)
        elif ':12M' in C_metadata.loc[i, 'Env']:
            C_12M_queries.append(i)
        else:
            C_sources.append(i)
            
    C_sources_metadata = metadata.loc[C_sources]      
    C_sources_metadata.columns = ['SampleID', 'Env']
    C_sources_abundance = abundance[C_sources_metadata['SampleID']]
    C_sources_abundance.insert(0, 'Samples', abundance['Samples'])
    
    C_12M_metadata = metadata.loc[C_12M_queries]      
    C_12M_metadata.columns = ['SampleID', 'Env']
    C_12M_abundance = abundance[C_12M_metadata['SampleID']]
    C_12M_abundance.insert(0, 'Samples', abundance['Samples'])
    
    C_5Y_metadata = metadata.loc[C_5Y_queries]      
    C_5Y_metadata.columns = ['SampleID', 'Env']
    C_5Y_abundance = abundance[C_5Y_metadata['SampleID']]
    C_5Y_abundance.insert(0, 'Samples', abundance['Samples'])
    
    V_index = []
    V_12M_queries = []
    V_5Y_queries = []
    V_sources = []
    
    for i in metadata_withbirth.index:
        if ':V' in metadata_withbirth.loc[i, 'Env']:
            V_index.append(i)
    V_metadata = metadata.loc[V_index]
    V_metadata.columns = ['SampleID', 'Env']
    V_abundance = abundance[V_metadata['SampleID']]
    V_abundance.insert(0, 'Samples', abundance['Samples'])
    
    for i in V_metadata.index:
        if ':5Y' in V_metadata.loc[i, 'Env']:
            V_5Y_queries.append(i)
        elif ':12M' in V_metadata.loc[i, 'Env']:
            V_12M_queries.append(i)
        else:
            V_sources.append(i)
            
    V_sources_metadata = metadata.loc[V_sources]      
    V_sources_metadata.columns = ['SampleID', 'Env']
    V_sources_abundance = abundance[V_sources_metadata['SampleID']]
    V_sources_abundance.insert(0, 'Samples', abundance['Samples'])
    
    V_12M_metadata = metadata.loc[V_12M_queries]      
    V_12M_metadata.columns = ['SampleID', 'Env']
    V_12M_abundance = abundance[V_12M_metadata['SampleID']]
    V_12M_abundance.insert(0, 'Samples', abundance['Samples'])
    
    V_5Y_metadata = metadata.loc[V_5Y_queries]      
    V_5Y_metadata.columns = ['SampleID', 'Env']
    V_5Y_abundance = abundance[V_5Y_metadata['SampleID']]
    V_5Y_abundance.insert(0, 'Samples', abundance['Samples'])
    
    metadata.to_csv('5-years/cesarean-section/metadata.csv', index=0)
    metadata.to_csv('5-years/verginal-delivery/metadata.csv', index=0)
    metadata.to_csv('12-months/cesarean-section/metadata.csv', index=0)
    metadata.to_csv('12-months/verginal-delivery/metadata.csv', index=0)
    C_sources_metadata.to_csv('C-source.csv', index=0)
    V_sources_metadata.to_csv('V-source.csv', index=0)
    
    C_5Y_abundance.to_csv('5-years/cesarean-section/queries.tsv', sep='\t', index=0)
    C_12M_abundance.to_csv('12-months/cesarean-section/queries.tsv', sep='\t', index=0)
    C_sources_abundance.to_csv('5-years/cesarean-section/sources.tsv', sep='\t', index=0)
    C_sources_abundance.to_csv('12-months/cesarean-section/sources.tsv', sep='\t', index=0)
    C_metadata.to_csv('meta-sample.csv', index=0)
    
    V_5Y_abundance.to_csv('5-years/verginal-delivery/queries.tsv', sep='\t', index=0)
    V_12M_abundance.to_csv('12-months/verginal-delivery/queries.tsv', sep='\t', index=0)
    V_sources_abundance.to_csv('5-years/verginal-delivery/sources.tsv', sep='\t', index=0)
    V_sources_abundance.to_csv('12-months/verginal-delivery/sources.tsv', sep='\t', index=0)
    
    
          
    
    
    