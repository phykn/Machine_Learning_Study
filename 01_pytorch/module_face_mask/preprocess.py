import cv2
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
        annotation = get_annotation(annot_file)      
        
        if self.transform:
            transformed = self.transform(image=image, bboxes=annotation['bboxes'], labels=annotation['labels'])
            image = transformed['image']
            annotation = {'bboxes':transformed['bboxes'], 'labels':transformed['labels']}            
        return image, annotation