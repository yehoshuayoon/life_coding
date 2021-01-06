import argparse
import os

def main(input_folder_path, output_folder_path):
    '''
    This code delete json files in the Takeout>Google_photo folders.
    :param input_folder_path:
    :param output_folder_path:
    :return:
    '''
    file_list = os.listdir(input_folder_path)
    # checkUserFolder = os.popen(f'ls {input_folder_path}/*.*')
    checkUserFolder = os.walk(input_folder_path, topdown=False)
    for i in checkUserFolder:
        file_list = i[-1]
        for file_ in file_list:
            file_extension = file_[file_.rfind('.')+1:]
            # print(file_extension)
            if file_extension == 'json':
                path_file = f'{i[0]}/{file_}'
                os.remove(path_file)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_folder_path', type=str)
    parser.add_argument('-o', '--output_folder_path', type=str)

    args = parser.parse_args()
    input_folder_path = args.input_folder_path
    output_folder_path = args.output_folder_path

    input_folder_path = '/Volumes/Samsung/google_photo/Takeout_merged'
    main(input_folder_path, output_folder_path)
