#!/usr/bin/bash
DownloadDirFiles=( "$HOME/Downloads"/* )
DownloadStorage="$HOME/Downloads/.storage"
for file in "${DownloadDirFiles[@]}"
do
	[ ! -f "$file" ] && continue
    tStamp="$(stat -c "%y" "$file" | cut -d " " -f1)"
    fType="$(file -p -b "$file" | cut -d " " -f1)"
    mkdir -p "$DownloadStorage/$tStamp/$fType"
    mv -n "$file" "$DownloadStorage/$tStamp/$fType" && \
        echo "moved $file to $tStamp/$fType" || \
        echo "failed to move $file $tStamp"
done
