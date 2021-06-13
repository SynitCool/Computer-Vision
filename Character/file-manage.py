import os
import shutil

# Initialize variable
current_path = os.getcwd()
new_dir = ["train_image", "test_image"]


# Make dir of new_dir
for dr in new_dir:
    if os.path.exists(dr):
        break
    join = os.path.join(current_path, dr)
    os.mkdir(join)
    
# Copy to files
for path, dirs, files in os.walk(current_path):
    current_dir = path.split("\\")[-1]
    dest_trn = os.path.join(current_path, "train_image")
    dest_tst = os.path.join(current_path, "test_image")
    if current_dir == "learn":
       for file in files:
           src = os.path.join(path, file)
           shutil.copy(src,dest_trn)
    if current_dir == "test":
        for file in files:
            src = os.path.join(path, file)
            shutil.copy(src, dest_tst)
           