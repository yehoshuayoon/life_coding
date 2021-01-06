import argparse
import os
import shutil

from lib import util

def main(input_folder_path_list, output_folder_path):
    '''
    This code delete json files in the Takeout>Google_photo folders.
    :param input_folder_path:
    :param output_folder_path:
    :return:
    '''
    for input_folder_path in input_folder_path_list:
        file_list = os.listdir(input_folder_path)
        # checkUserFolder = os.popen(f'ls {input_folder_path}/*.*')
        checkUserFolder = os.walk(input_folder_path, topdown=False)
        for i in checkUserFolder:
            folder_path = i[0]
            folder_name = folder_path.split('/')[-1]
            new_folder_path = f'{output_folder_path}/{folder_name}'
            # print(f'{folder_name}  --  {folder_path}  -->  {new_folder_path}')
            util.create_folder(new_folder_path)
            file_list = i[2]

                # print(f'{i[0]} -- {i[1]}')
            for file_ in file_list:
                file_path = f'{folder_path}/{file_}'
                new_file_path = new_folder_path+'/'+file_
                try:
                    f = open(new_file_path, 'r')
                except:
                    shutil.move(file_path, new_folder_path+'/')



if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--input_folder_path', type=str)
    # parser.add_argument('-o', '--output_folder_path', type=str)
    # args = parser.parse_args()
    input_folder_path_list = [
        '/Volumes/Samsung/google_photo/Takeout/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 2/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 3/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 4/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 5/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 6/Google 포토',
        '/Volumes/Samsung/google_photo/Takeout 7/Google 포토',
    ]
    output_folder_path = '/Volumes/Samsung/google_photo/Takeout_merged/Google 포토'

    main(input_folder_path_list, output_folder_path)
