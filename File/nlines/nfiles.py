def file_read(fname):
    with open(fname, "r") as myfile:
        data = myfile.readlines()
        print(data)

file_read('C:\\Users\Siva Shankari\Documents\WEB_APPL_ARC.rtf')