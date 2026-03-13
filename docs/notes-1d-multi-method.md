**Objective**: Create a figure showing the data in ./data/1d-multi-method-data.csv. Highlight "Proposed" against "Baseline 1" and "Baseline 2", .... "Baseline 9" by using preattentive visual encoding. Make sure to (1) label your axes, (2) create a non-misleading visualization, and (3) highlight "Proposed" effectively.

**Context**: This dataset consists of measurements (i.e., "AUC-ROC") of samples using multiple methods. 

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
1. Data shape 2*100. No nulls in the dataset.
2. Each row capture the AUCROC using specified method. 
3. There are total 10 different methods: Baseline_1 to Baseline_9 and Proposed. Each method has 10 AUCROC values, with different mean. Also notice the standard deviation is small, so data points are concentrated.
4. The jittered scatter plot validates that the AUCROC values of each method are centered at mean.

**Visualization strategy**
1. To highlight the "Proposed" method, make the following enhancements of the jittered scatter plot:
    1. Ordering methods by mean of AUCROC, and show mean of AUCROC explicitly
    2. Highlight the "Proposed" method with different color