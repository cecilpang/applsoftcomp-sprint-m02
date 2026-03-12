**Objective**: Create a figure showing the data in ./data/1d-data.csv. Make sure to label your axes and create a non-misleading data. You can choose any appropriate visualization method (e.g., line plot, bar plot, etc.).

**Context**: This dataset consists of the effect of a treatment for 10 subjects. 

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
1. Data shape 2*20. No nulls in the dataset.
2. One numerical(float64) column. 
3. A string column indicates whether each point is a case or control, with 10 data points in each group.
4. The "cases" group has a higher mean and standard deviation than the "control" group, suggesting more variability. 
5. The maximum value in the "cases" group is notably higher, which could be an outlier; 
6. Accessing the data under log scale, which shows the two large values are not outliers. 

**Visualization**
1. Given the small data size, choose Beeswarm Plots. 
2. Use log scale to handle the large values.
3. Can combine the box plot with swarm plot.
