from src.utils import load_object

model_path = "artifacts/model.pkl"
preprocessor_path = "artifacts/preprocessor.pkl"

model = load_object(model_path)
preprocessor = load_object(preprocessor_path)

print("MODEL TYPE  :", type(model))
print("MODEL VALUE :", model)
print("PREP TYPE   :", type(preprocessor))