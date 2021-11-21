import os, shutil

parent_folders = {
    'Images': [ 'ai', 'bmb', 'gif', 'ico', 'jpeg', 'jpg', 'max', 'obj', 'png', 'ps', 'psd', 'svg', 'tif', 'tiff', '3ds', '3dm'],
    'Text File': [ 'doc', 'docx', 'odt', 'msg', 'pdf', 'rtf', 'tex', 'txt', 'wks', 'wps', 'wpd'],
    'Executable Files': [ 'apk', 'bat', 'bin', 'cgi', 'com', 'exe', 'jar', 'py', 'wsf', 'ipynb'],
    'Audios': ['aif', 'cda', 'iff', 'mid', 'midi', 'mp3', 'mpa', 'wav', 'wma', '3g2', '3gp'],
    'Spreadsheets': ['ods', 'xlr', 'xls', 'xlsx'],
    'Presentations': ['key', 'odp', 'pps', 'ppt', 'pptx'],
    'Database Files': ['accdb', 'csv', 'dat', 'db', 'dbf', 'log', 'mdb', 'pdb', 'sav', 'sql', 'tar'],
    'Web Files': [ 'asp', 'aspx', 'cer', 'cfm', 'cgi', 'pl', 'css', 'htm', 'html', 'js', 'part', 'php', 'rss', 'xhtml'],
    'System Related File': [ 'bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'icns', 'ico', 'ini', 'lnk', 'msi', 'sys', 'tmp']
}

def main():
    """ The function to where program start"""
    path= get_path()
    files = os.listdir(path)
    count = 0
    for file in files:
        if os.path.isfile(os.path.join(path, file)) is True:
            if movefile(file, path) is True:
                count += 1
                print(count, 'item moved out of', count_movable_item(path, files))

def get_path():
    """ The function to take path"""
    try:
        path = input("Enter path: ")
    except:
        print("Address not found")
    else:
        return path

def move(path, extension, file, folder_name):
    """ The Function to create and move files to its respective locations """
    
    if os.path.exists(os.path.join(path, folder_name)) is False:
        os.makedirs(os.path.join(path, folder_name))

    # It Other folder exit then check whether sub folder is exit or not
    if os.path.exists(os.path.join(path, folder_name)):
        # It sub folder does not exit then create it
        if os.path.exists(os.path.join(path, folder_name, extension)) is False:
            os.makedirs(os.path.join(path, folder_name, extension))

        # if Sub folder exit then move file into it
        if os.path.exists(os.path.join(path, folder_name, extension)):
            try:
                shutil.move(os.path.join(path, file), os.path.join(path, folder_name, extension))
            except:
                print('The destination already has a file named', file)
                return False
            else:
                return True

def movefile(file, path):
    """ Function to check extension and decide which file to move in which directory """
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    extension_found = False

    for folder_name in parent_folders:
        if extension in parent_folders[folder_name]:
            extension_found = True
            return move(path, extension, file, folder_name)

    # If any file is unkown or extension is not known then move it to other folders
    if extension_found is False:
        # Checking if Other folder does not exit then create it
        return move(path, extension, file, 'Other')
        # pass

def count_movable_item(path, files):
    """ Function to count number of movable files """
    total_movable_file = 0
    for file in files:
        if os.path.isfile(os.path.join(path, file)) is True:
            total_movable_file += 1
    return total_movable_file

# The program start from here
main()