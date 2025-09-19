
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

iris = load_iris()
X, y = iris.data, iris.target

clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

with mlflow.start_run():
    mlflow.sklearn.log_model(
        sk_model=clf,
        artifact_path="iris_rf_model",
        registered_model_name="iris_rf_classifier"
    )
    print("Model registered in MLflow")