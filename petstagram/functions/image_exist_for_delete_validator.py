
#takes the img name
def img_validator(path):
    path = list(path)
    img = []

    for img_symbol in range(len(path), -1, -1):
        if path[img_symbol - 1] == chr(92):
            break
        img.append(path[img_symbol - 1])

    return ''.join(reversed(img))