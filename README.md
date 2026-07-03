### Overview 

My self taught notebook on the subject Data Analytics

## Part 1: EDA

Date 07.03.26

Learn how to use matplotlib

1. Create canvas

```
# in inches
fig, ax = plt.subplots(figsize=(width, length)) 
```

2. Draw plot inside canvas, graph type
```
# Create the plot inside the canvas, x can be df['column name], y can be df['column name']
ax.(plot name)(x, y, color = plt.cm.tab20(range(5)))
ax.set_xlabel("X name")
ax.set_ylabel("Y name")
ax.set_title("Graph name")
```
3. Sorting things up

```
df.sort_values("by what category in the df", ascending=True/False).head()
```