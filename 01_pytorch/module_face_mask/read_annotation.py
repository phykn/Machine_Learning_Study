from bs4 import BeautifulSoup

def get_annotation(file): 
    with open(file) as f:
        data = f.read()
    soup = BeautifulSoup(data, "html.parser")
    objs = soup.find_all("object")

    boxes = []
    labels = []
    for obj in objs:
        boxes.append(get_box_coordinate(obj))
        labels.append(get_label(obj))

    annotation = {}
    annotation["bboxes"] = boxes
    annotation["labels"] = labels
    return annotation

def get_box_coordinate(obj):    
    xmin = int(float(obj.find('xmin').text))
    ymin = int(float(obj.find('ymin').text))
    xmax = int(float(obj.find('xmax').text))
    ymax = int(float(obj.find('ymax').text))   
    return [xmin, ymin, xmax, ymax]

def get_label(obj):
    if obj.find('name').text == "without_mask":
        return 0    
    elif obj.find('name').text == "with_mask":
        return 1
    elif obj.find('name').text == "mask_weared_incorrect":
        return 2
    else:
        raise ValueError('Name not in ["without_mask", "with_mask", "mask_weared_incorrect"]')