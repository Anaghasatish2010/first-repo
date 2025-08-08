import os
from PIL import Image

class ImageDataset:
    def __init__(self, root):
        self.root = root
        self.filenames = os.listdir(self.root)

    def __len__(self):
        return len(self.filenames)
    
    def __getitem__(self, idx):
        img = Image.open(self.root+ '/'+self.filenames[idx])
        return img

ds = ImageDataset("images")
print(ds.filenames)
print(len(ds))
print(ds[2])
img = ds[1]
img.show()