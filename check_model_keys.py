import pickle

# Load the model file
with open('model.pkl', 'rb') as file:
    model_dict = pickle.load(file)

# Check the type and keys
print("Loaded object type:", type(model_dict))

# If it's a dictionary, print its keys
if isinstance(model_dict, dict):
    print("Keys in model.pkl:", model_dict.keys())
else:
    print("model.pkl is not a dictionary.")
