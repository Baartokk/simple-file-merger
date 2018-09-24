import os, time

path = 'files_to_merge/'
file_format = 'txt'
header = False

#---------------------------------------------------------------------

list_of_files = [item for item in os.listdir(path) if '.{0}'.format(file_format) in item]

print('Merging...')   
 
with open('000_merge_{0}.{1}'.format(time.strftime("%Y-%m-%d_%H%M%S"), file_format), 'w', encoding = '1250', newline = '') as newFile:
    for idx, file in enumerate(list_of_files):            
        with open(path + file, 'r', encoding = '1250', newline = '') as rFile:
            
            rFile.readline() if idx > 0 and header else 0
            for line in rFile:
                newFile.write(line)

print('Done.\nFiles merged: {0}'.format(len(list_of_files)))
