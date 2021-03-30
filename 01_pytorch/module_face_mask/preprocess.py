import numpy as np
import cv2
import torch
from torch.utils.data import Dataset
from .read_annotation import get_annotation
        
class DATASET(Dataset):
    def __init__(self, image_files, annot_files, transform=None):
        assert len(image_files) == len(image_files)
        self.image_files = image_files
        self.annot_files = annot_files
        self.transform = transform
        
    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        image_file = self.image_files[index]
        annot_file = self.annot_files[index]

        image = cv2.imread(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_x_max, image_y_max, _ = image.shape 
        
        annotation = get_annotation(annot_file)      
        
        # Bounding Box Correction
        boxes = np.array(annotation['boxes'])
        boxes[:, 3] = np.where(boxes[:, 3] > image_x_max, image_x_max, boxes[:, 3])
        boxes[:, 2] = np.where(boxes[:, 2] > image_y_max, image_y_max, boxes[:, 2])
        annotation['boxes'] = boxes.tolist()
        
        if self.transform:
            transformed = self.transform(image=image, bboxes=annotation['boxes'], labels=annotation['labels'])
            image = transformed['image']
            annotation = {
                'boxes': torch.as_tensor(transformed['bboxes'], dtype=torch.float32),
                'labels': torch.as_tensor(transformed['labels'], dtype=torch.int64)
            }            
        return image, annotation