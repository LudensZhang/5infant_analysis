import pandas as pd
from skbio.stats.ordination import pcoa
from skbio.diversity import beta_diversity
from plotnine import*



if __name__ == '__main__':
    abundance = pd.read_csv('../8folds/abundance.csv', index_col = 0).T
    metadata = pd.read_csv('../8folds/metadata.csv').set_index('SampleID')
    metadata.replace({'B': 'NB'}, inplace = True)

    distance_mat = beta_diversity('braycurtis', abundance, ids = metadata.index.tolist())
    pcoa_result = pcoa(distance_mat, number_of_dimensions=2)
    pcoa_df = pd.DataFrame(pcoa(distance_mat, number_of_dimensions=2).samples.values.tolist(), 
                            columns = ['PC1', 'PC2'], index = abundance.index)
    
    pcoa_plot = (ggplot(pcoa_df, aes(x = 'PC1', y = 'PC2', fill = metadata)) +
                    geom_point(alpha = 0.1, size = 1, show_legend = False) +
                    scale_fill_manual(['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF']) +
                    scale_color_manual(['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF']) +
                    xlim(-0.6, 0.6) +
                    ylim(-0.6, 0.6) +
                    theme_bw() +
                    theme(axis_text = element_text(size = 10, color = 'black'),
                        panel_grid_major = element_blank(), 
                        panel_grid_minor = element_blank(),
                        legend_title = element_blank(),
                        text = element_text(size = 10)) +
			        xlab('PC1') +
			        ylab('PC2'))
    
    pcoa_plot.save('PCoA.png', dpi = 300, height = 70, width = 70, units = 'mm')

    box_1 = (ggplot(pcoa_df, aes(x=metadata, y='PC1', fill=metadata))
			+ geom_boxplot(width=0.3, show_legend=False)
			+ scale_fill_manual(['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF'])
			+ theme_bw()		
			+ theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank())
			+ theme(axis_text = element_text(size = 10, color = 'black'),
           			text = element_text(size = 10))
			+ xlab('')
			+ ylab('PC1')
			+ coord_flip()
   			+ xlim(['NB', '4M', '12M', '3Y', '5Y', 'M'])
		   )
    box_1.save('PC1_box.png', dpi = 300, height = 70/3, width = 70, units = 'mm')

    box_2 = (ggplot(pcoa_df, aes(x=metadata, y='PC2', fill=metadata))
			+ geom_boxplot(width=0.3, show_legend=False)
			+ scale_fill_manual(['#E64B35FF','#4DBBD5FF','#00A087FF','#3C5488FF','#F39B7FFF','#8491B4FF','#91D1C2FF'])
			+ theme_bw()
			+ theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank())
			+ theme(axis_text = element_text(size = 10, color = 'black'),
           			text = element_text(size = 10))
			+ xlab('')
			+ ylab('PC2')
   			+ coord_flip()
			+ xlim(['NB', '4M', '12M', '3Y', '5Y', 'M'])
		   )
    box_2.save('PC2_box.png', dpi = 300, height = 70/3, width = 70, units = 'mm')