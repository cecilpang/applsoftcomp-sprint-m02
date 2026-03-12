**Objective**: Create a figure showing the data in ./data/1d-data.csv. Make sure to label your axes and create a non-misleading data. You can choose any appropriate visualization method (e.g., line plot, bar plot, etc.).

**Context**: This dataset consists of the effect of a treatment for 10 subjects. 

**Plan**:
~~1. Explore data.~~ 
    ~~1. Document insights and understanding of the dataset.~~
    ~~2. Describing the data structure, key observations, and visualization strategy~~
2. Data formatting
    1. Load and inspect
    2. Clean/ transform in needed
    3. Save tranformed data and create loading function
3. Visualization
    1. Visualize data, save figure
    2. Create visualization function

**Data Exploration**:
1. Data shape 2*20. 
2. One numerical(float64) column. 
3. A string column indicates whether each point is a case or control, with 10 data points in each group.
4. There's no nulls
5. The "cases" group has a higher mean and standard deviation than the "control" group, suggesting more variability. The maximum value in the "cases" group is notably higher, which could be an outlier; a log scale might be appropriate for visualization.
6. The swarm plot reveals two clear outliers.

**Visualization strategy**
1. Given the small data size, consider Beeswarm Plots
