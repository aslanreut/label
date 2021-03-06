import os
import glob
import pandas as pd
def label(path, labels, extension, column_names, save_as):
    os.chdir(path) 
    fnames = glob.glob('*.'+ extension)
    fn_name = [] # filenames containing one of the labels
    fn_class = [] # corresponding label
    
    for fn in fnames:
        for c in labels:
            if c in fn.lower():
                fn_name.append(fn)
                fn_class.append(c)
    df = pd.DataFrame(list(zip(fn_name,fn_class)), columns=column_names)
    df.to_csv(save_as +'.csv', index=False)
