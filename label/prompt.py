from .label import label
import sys

def create_csv():
    print('\nWhere are the files stored?')
    directory = input('e.g. C:/Users/data \nEnter: ').strip()
    #print('Is that correct? Enter to continue, otherwise press n')

    print('\nEnter the labels comma-separated:')
    labels = input('eg. label1,label2,label3\nEnter: ').lower().replace(" ", "").split(",")
    #print(labels)

    print('\nEnter the file extension:')
    extension = input('e.g. wav \ne.g. mp3\ne.g. jpg \nEnter: ').lower().replace(".", "")
    #print(extension)

    print('\nEnter the column names comma-separated:')
    column_names = input('e.g. filename,label\nEnter: ').replace(" ", "").split(",")
    #print(column_names)

    print('\nGive the file a name:')
    store_as = input('e.g. labeled_data\nEnter: ').replace(" ", "").split(".")[0]
    #print(store_as)

    print(
        '\nPlease check your inputs:\nPath:\t\t\t{}\nLabels:\t\t\t{}\nFile extension:\t\t.{}\nColumn names:'
        '\t\t{}\nSave as:\t\t{}.csv\n'.format(directory,labels,extension,column_names,store_as))

    pressed = input('\nPress enter to continue or press n to start again\nEnter: ')
    if pressed.lower().strip()=='n' or pressed.lower().strip()=='no':
        print('\nLets try it again!')
        create_csv()
    else:
        label(directory,labels,extension, column_names,store_as)
        print('Successfully created {}.csv in {}!'.format(store_as, directory))
        

