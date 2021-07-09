def cambiar_Tamaño_Imagen(imagen):
    img=cv2.imread(imagen)
    img_resize=cv2.resize(img,(443,200))
    return img_resize
