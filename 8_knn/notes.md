# K Nearest Neighbor (KNN)

## Idea of algorithm

This algorithm can be used for both classification and regression. 

First is the definition of k: number of nearest neighbour for a given point. Normally, we try different k on the model then perform on test data, then evaluate which k produces the most effective on training data.

Both need to calculate the distance (normally euclidean distance) between all points in the dataset. For each point, calculate its distance to all other data points in the dataset, then choose k nearest point (k defined previously).

- Classification: use majority rule: among the points selected, classify the new data point as the majority among the k points selected. 

For example, k=7, so the algorithm choose 7 closest point to the given point. Assuming 4 of them belong to class A, 2 to class B and 1 to class C, the algorithm will classify the data point as class A (given majority of them are As). 

Problem: What if the same point belong to different classes ? Like 3 to class A and 3 to class B: Then we also need to define a tie rule. 

Rule: 

- Choosing odd k 

- Choose randomly between classes

- Weighted between distance (closer = weight more, so we often use formular 1/distance then sum all up)

## Regression

Instead of choosing based on the majority, the algorithm calculate the average between all the nearest points

$\hat{y} = \frac{\sum_{i=1}^{k} w_i y_i}{\sum_{i=1}^{k} w_i}, \quad w_i = \frac{1}{d_i}$

