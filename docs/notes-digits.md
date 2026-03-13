**Objective**: Create a figure showing the UCI ML hand-written digits dataset in ./data/digits-data.csv. Visualize the data in 2D (e.g., using t-SNE) to show the clustering structure. Color the data points by digit class to reveal the similarity and dissimilarity of digit distributions. No need to perform clustering — use the provided digit labels as class membership.

**Context**: This dataset consists of 8×8 pixel images of handwritten digits (0–9) with 64 features per sample.

**Plan**:
1. Explore data.
    1. Document insights and understanding of the dataset.
    2. Describing the data structure, key observations, and visualization strategy
2. Data formatting
    1. Load and inspect
    2. Clean/ transform in needed
    3. Save tranformed data and create loading function
3. Visualization
    1. Visualize the data in 2D (e.g., using t-SNE) to show the clustering structure
    2. Color the data points by digit class to reveal the similarity and dissimilarity of digit distributions.
    3. No need to perform clustering — use the provided digit labels as class membership.
    4. Create visualization function

**Data Exploration and Insights**:
1. Data shape 1797*65, 
    1. 1797 data points, 
    2. 64 pixels and 1 column indicate the digits. 
    3. No nulls in the dataset. 
    4. Each digit has around 180 samples 

**Visualization strategy**
1. 