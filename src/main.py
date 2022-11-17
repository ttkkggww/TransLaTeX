from src.connection import Connection
import src.splitter as Splitter
import zipfile
import argparse
import os
import glob
import datetime
import shutil

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-P","--path",help="Path of the zip file you want to translate.")
    parser.add_argument("-W","--workspace",default="./workspace",help="Temporary workspace location for file operations.")
    parser.add_argument("-T","--tmpdir",default="qawsedrf",help="Temporary workspace location for file operations.")
    return(parser.parse_args())


def main():
    args = get_args()
    zip_path = args.path
    connection = Connection()
    if os.path.exists(args.workspace) == False:
        os.makedirs(args.workspace)
    with zipfile.ZipFile(zip_path) as zip_file:
        zip_file.extractall(os.path.join(args.workspace,args.tmpdir))
        paths = zip_file.namelist()
    save_zip = zipfile.ZipFile(os.path.join(args.workspace\
            ,str(datetime.datetime.now().replace(microsecond=0)).replace(' ','_')\
            +"_translated_"+os.path.basename(args.path)),'w')
    for zip_path in paths:
        if(os.path.splitext(zip_path)[-1]=='.tex'):
            with open(os.path.join(args.workspace,args.tmpdir,zip_path)) as f:
               lines = f.readlines()
            lines , comments = Splitter.remove_comment(lines)
            lines = [''.join(lines)]
            stack = []
            lines,stack = Splitter.split_begin_end(lines,stack)
            lines,stack = Splitter.split_re(lines,stack)
            Splitter.warning_backslash(lines,zip_path)
            tmp = []
            print("translating",zip_path,"...")
            for line in lines:
                tmp.append(connection.translate(line))
            lines = tmp
            lines = Splitter.restore_escape(lines,stack,zip_path)
            with open(os.path.join(args.workspace,args.tmpdir,zip_path),'w') as f:
                for line in lines:
                    f.write(line)
        save_zip.write(os.path.join(args.workspace,args.tmpdir,zip_path),zip_path)
    save_zip.close()
    shutil.rmtree(os.path.join(args.workspace,args.tmpdir))

if __name__ == "__main__":
    main()
