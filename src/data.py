from sklearn.datasets import load_diabetes
from pydantic import BaseModel, ConfigDict, Field

Xy = load_diabetes(as_frame=True)

X = Xy.frame.drop(columns=["target"])

y = Xy.frame["target"]  # acts as a "progression index" (higher = worse)


class DiabetesFeatures(BaseModel):
    model_config = ConfigDict(extra="forbid")

    age: float = Field(allow_inf_nan=False)
    sex: float = Field(allow_inf_nan=False)
    bmi: float = Field(allow_inf_nan=False)
    bp: float = Field(allow_inf_nan=False)
    s1: float = Field(allow_inf_nan=False)
    s2: float = Field(allow_inf_nan=False)
    s3: float = Field(allow_inf_nan=False)
    s4: float = Field(allow_inf_nan=False)
    s5: float = Field(allow_inf_nan=False)
    s6: float = Field(allow_inf_nan=False)