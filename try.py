import os
path = "nnUNet_raw\Dataset201_Heart\imagesTr"
for filename in os.listdir(path):
    if filename.endswith(".nii.gz"):
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("0000.nii.gz", "_0000.nii.gz")))