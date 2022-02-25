"""
Part of example from: https://github.com/scikit-learn-contrib/imbalanced-learn/blob/master/examples/applications/plot_impact_imbalanced_classes.py and https://scikit-image.org/
01.12.2021

"""

from sklearn.datasets import fetch_openml

df, y = fetch_openml("adult", version=2, as_frame=True, return_X_y=True)
df = df.drop(columns=["fnlwgt", "education-num"])


classes_count = y.value_counts()
classes_count

from imblearn.datasets import make_imbalance

ratio = 30
df_res, y_res = make_imbalance(
    df,
    y,
    sampling_strategy={classes_count.idxmin(): classes_count.max() // ratio},
)
y_res.value_counts()


from skimage import data, io, filters

image = data.coins()
edges = filters.sobel(image)
io.imshow(edges)
io.show()