**Objective**: Create a figure showing the data in ./data/2d-data.csv. You can choose any appropriate visualization method (e.g., heatmap, contour plot, surface plot, etc.).

**Context**: This dataset consists 2D measurements of samples.

**Plan**:
1. Explore data.
    1. Document insights and understanding of the dataset.
    2. Describing the data structure, key observations, and visualization strategy
2. Data formatting
    1. Load and inspect
    2. Clean/ transform in needed
    3. Save tranformed data and create loading function
3. Visualization
    1. Visualize data, save figure
    2. Create visualization function

**Data Exploration and Insights**:
1. Data shape 2*6000. No nulls in the dataset.
2. Two numerical(float64) column, they share similar statistical summaries. 
    1. The histograms of x and y show that they share similar distribution (Gaussian). 
3. Try scatter plot with transparency. It shows correlation between x and y, but hard to tell the density of data.

**Visualization strategy**
1. Consider Hexbin Plots that can show the correlation and data density.
    1. Tried seaborn hexbin with marginal histograms. It shows clear correlation between x and y. Also shows data points are concentrated in two clusters
2. Tried 2D KDE which clearly shows the correlation and data density.
3. Combine Hexbin plot and Contour Plots
