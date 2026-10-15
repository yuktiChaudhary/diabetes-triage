from sklearn.datasets import load_diabetes

Xy = load_diabetes(as_frame=True)

X = Xy.frame.drop(columns=["target"])

y = Xy.frame["target"]  # acts as a "progression index" (higher = worse)
