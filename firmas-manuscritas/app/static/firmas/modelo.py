def modelo_h5(ruta):
    new_model=keras.models.load_model(ruta)
    return new_model

def modelo_pkl(ruta):
    new_model=joblib.load(ruta)
    return modelo_pkl
