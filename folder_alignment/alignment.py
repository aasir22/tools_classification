import os
import shutil

# path = r'C:/Users/LENOVO/Desktop/Projects/Deep Learning Projects/Mechanical tools classfication/Mechanical Tools Image dataset'
# l = os.listdir(path)
# new_path = r'C:/Users/LENOVO/Desktop/Projects/Deep Learning Projects/Mechanical tools classfication/final_dataset'
# for i in l:
#     os.mkdir(new_path + f'/{i}')

class Align:

    def __init__(self):
        self.train_des = r'C:\Users\LENOVO\Desktop\Projects\Deep Learning Projects\Mechanical tools classfication\final_dataset\train'
        self.test_des = r'C:\Users\LENOVO\Desktop\Projects\Deep Learning Projects\Mechanical tools classfication\final_dataset\test'
        self.val_des = r'C:\Users\LENOVO\Desktop\Projects\Deep Learning Projects\Mechanical tools classfication\final_dataset\val'
        self.path = r'C:/Users/LENOVO/Desktop/Projects/Deep Learning Projects/Mechanical tools classfication/Mechanical Tools Image dataset'

    def seperatefolder(self):
        """method = seperatefolder
        this method seperate train test and val folders
        """
        folders = os.listdir(self.path)
        for folder in folders:
            new_path = os.path.join(self.path, folder)
            train_val = os.listdir(new_path)[:round(len(os.listdir(new_path)) * 0.8)]
            train = train_val[:round(len(train_val) * 0.8)]
            for img in train:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.train_des, folder))


            test = os.listdir(new_path)[len(train_val):]
            for img in test:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.test_des, folder))


            val = train_val[len(train):]
            for img in val:
                shutil.copy(os.path.join(new_path, img), os.path.join(self.val_des, folder))

if __name__ == '__main__':
    align = Align()
    align.seperatefolder()