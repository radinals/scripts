#!/usr/bin/bash

download_dir_files=( "$HOME/Downloads"/* )
storage_path="$HOME/Downloads/.storage"

if [ ! -d "$storage_path" ]; then
    echo "No path named, '$storage_path', creating now..."
    mkdir -p "$storage_path"
    echo "Done..."
fi

clear_empty_file()
{
    echo "Clearing Empty Directories at '$storage_path'..."
    find "$storage_path" -type d -empty -delete
    echo "Done.."
}

get_file_type()
{
    local filename
    local ext
    local fname
    local filetype

    filename="$(basename "$1")"
    ext="${filename##*.}"
    fname="${filename%.*}"

    filetype=""

    case "${ext}" in
        txt) filetype="plaintext" ;;
        cpp) filetype="source_cpp" ;;
        tar) filetype="archive_tar" ;;
        zip) filetype="archive_zip" ;;
        7z) filetype="archive_7z" ;;
        docx) filetype="doc_msdocx" ;;
        pptx) filetype="doc_mspptx" ;;
        pdf) filetype="doc_pdf" ;;
        epub) filetype="doc_epub" ;;
        md) filetype="markdown" ;;
        mp4) filetype="video_mp4" ;;
        AppImage) filetype="appimage" ;;
        jpg) filetype="image_jpg" ;;
        png) filetype="image_png" ;;
        webp) filetype="image_webp" ;;
        # *)  ;;
    esac

    case "${fname}" in
        LICENSE) filetype="plaintext" ;;
        # *)  ;;
    esac

    [ -z "$filetype" ] && filetype="$(file -p -b "$file" | cut -d " " -f1)"

    echo "$filetype"
}

for file in "${download_dir_files[@]}"
do
	[ ! -f "$file" ] && continue

    time_stamp="$(stat -c "%y" "$file" | cut -d " " -f1)"

    file_type="$(get_file_type "$file" )"

    mkdir -p "$storage_path/$time_stamp/$file_type"

    mv -n "$file" "$storage_path/$time_stamp/$file_type" && \
        echo "Moved $(basename "$file") to $time_stamp/$file_type" || \
        echo "Failed to Move $file $time_stamp"
done

clear_empty_file
