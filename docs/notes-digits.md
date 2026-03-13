**Objective**: Create a figure showing the UCI ML hand-written digits dataset in `./data/digits-data.csv`. Visualize the data in 2D with a nonlinear embedding such as t-SNE, and color points by the provided digit label to reveal clustering structure.

**Context**: This dataset consists of 8×8 pixel images of handwritten digits (0–9) with 64 features per sample.

**Data Exploration and Insights**:
1. Data shape 1797*65, contains:
    1. 1797 samples, 
    2. Each sample is an 8 x 8 image flattened into 64 pixel-intensity features. 
    3. One column 'digit' stores the class label in 0-9.
    4. Each digit has around 180 samples 
2. Applied PCA from 64 to 2 vs from 64 to 30. 
    1. 64 -> 2 explained_variance:  0.29
    2. 64 -> 30 explained_variance:  0.96

**Visualization strategy**
1. Split the data into features X and labels y.
2. Create 2D views of the dataset:
   1. Only PCA from 64 features to 2D
   2. First PCA from 64 to 30, to make t-SNE faster and stable. Then t-SNE from 30 to 2D
3. Plot each 2D embeddings with color mapping for digits 0-9.