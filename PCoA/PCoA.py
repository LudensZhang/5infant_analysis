import pandas as pd



if __name__ == '__main__':
    abundance = pd.read_csv('abundance.csv')
    metadata = pd.read_csv('metadata.csv').set_index('SampleID')
    meta_withbirth = pd.read_csv('meta_withbirth.csv').set_index('SampleID')
    distance = pd.read_csv('distance.csv')
    
    
    for i in distance.index:
        if 'inf' in str(distance.loc[i]):
            print(abundance.columns[i+1])
            metadata = metadata.drop(abundance.columns[i+1])
            meta_withbirth = meta_withbirth.drop(abundance.columns[i+1])
            abundance = abundance.drop([abundance.columns[i+1]], axis=1)
            
    abundance.to_csv('abundance.csv', index=0)
    metadata.to_csv('metadata.csv')
    meta_withbirth.to_csv('meta_withbirth.csv')
            
            