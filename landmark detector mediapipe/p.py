import pickle
with open("face_ld.pkl","rb") as f:
    ld = pickle.load(f)

print(type(ld))
print(ld)
