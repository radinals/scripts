#!/usr/bin/env python3
import eyed3
from os import path, walk
from sys import argv
from pathlib import Path
from getopt import getopt
import filetype

def print_help():
    exit(
        """
    \r auto-tag - (Re)tags audio files in a specified directory.
    \r usage:    auto-tag [option] [value]    edit tags of the files in the directory
    \r Options:
    \r -t, --target {directory}    Specify a target directory.
    \r -f, -format {format}        Specify how the program looks for the tag by the filename.\n
    \r                              Available Format Flags:
    \r                               - %a: Track Artist  - %b: Album Artist
    \r                               - %t: Track Title   - %A: Album Name
    \r                               - %y: Track Year
    \r                               - %n: Track Number
    \r                              Default Format: "%a - %A - %t"\n
    \r -s, --seperator {seperator} Specify the sepeator in the filename
    \r                              Default seperator: " - "\n
    \r --help                      Display this help information then exit\n
    \r report bugs/issues at https://github/radinals/scripts/issues
    """
    )


# return a dict of the tag elements of a file
def get_file_tags(file, seperator, flag_format):
    file_tags = {}

    # remove the extention
    # split them by seperator
    fileElements = ((file.split(Path(file).suffix))[0]).split(seperator)

    # check if the number of format flag is more than the file elements
    if len(flag_format) != len(fileElements):
        print(f're-check the "format" arguments! Stopped at {file}')
        raise ValueError

    for i, v in enumerate(flag_format):
        file_tags[v] = fileElements[i]

    return file_tags

# list the files in the entered directory
def list_audio_files(targetDir):
    return [path.join(f_path, f)
            for f_path, _, f_list in walk(targetDir) for f in f_list
            if filetype.is_audio(path.join(f_path, f))]


def retag_files(file, tag_format, seperator, clear_tags=False):
    file_tags = get_file_tags(path.basename(file), seperator, tag_format)

    print(f"\nfile = {file}")
    try:
        audiofile = eyed3.load(file)
        if clear_tags:
            audiofile.tag.clear()

        for k in file_tags.keys():
            if k == "%a":
                audiofile.tag.artist = file_tags[k]
                print(f"artist = {file_tags[k]}")
            if k == "%t":
                audiofile.tag.title = file_tags[k]
                print(f"title = {file_tags[k]}")
            if k == "%A":
                audiofile.tag.album = file_tags[k]
                print(f"album = {file_tags[k]}")
            if k == "%b":
                audiofile.tag.album_artist = file_tags[k]
                print(f"album artist = {file_tags[k]}")
            if k == "%n":
                audiofile.tag.track_num = file_tags[k]
                print(f"num = {file_tags[k]}")
            if k == "%y":
                print(f"year = {file_tags[k]}")
                audiofile.tag.original_release_date = file_tags[k]

        audiofile.tag.save()
    except IndexError:
        exit(
            f"an error occured when editing {file} tag:check if file is named correctly"
        )
    except AttributeError:
        exit(f"{file} tag:check if file is named correctly")


def get_arguments():
    valid_flags = ["%a", "%t", "%A", "%b", "%n", "%y"]
    try:
        opts, args = getopt(
            argv[1:], "t:f:s:h", ["target=", "format=", "seperator=", "help"]
        )

    except:
        exit("unknown option, please see --help to see avaliable options..")

    target_location = None
    seperator = None
    clear_tags = False
    filename_format = []

    if len(opts) > 0:
        for opt, arg in opts:
            if opt in ["-h", "--help"]:
                print_help()

            if opt in ["-t", "--target"]:
                if path.isdir(arg):
                    target_location = arg
                else:
                    exit(f"{arg} does not exist!.")

            if opt in ["-f", "--format"]:
                formats = arg.split()
                for f in formats:
                    if f in valid_flags:
                        filename_format.append(f)

            if opt in ["-s", "--seperator"]:
                seperator = arg
            
            if opt in ["-c", "--clear-tags"]:
                clear_tags = True
    else:
        print_help()

    if target_location == None or len(filename_format) < 0:
        exit("Insufficient arguments!")

    if seperator == None:
        seperator = " - "

    if len(filename_format) == 0:
        filename_format = ["%a", "%A", "%t"]

    return {"dir": target_location, "format": filename_format, "seperator": seperator, "clear_tags": clear_tags}


def main():
    arguments = get_arguments()
    file_list = list_audio_files(arguments["dir"])

    for f in file_list:
        retag_files(f, arguments["format"], arguments["seperator"], arguments["clear_tags"])


if __name__ == "__main__":
    main()
