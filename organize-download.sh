#!/usr/bin/bash
DownloadDir="$HOME/Downloads"
DownloadDirContent=( "$DownloadDir"/* )
DownloadStorage="$DownloadDir/.storage"
for file in "${DownloadDirContent[@]}"
do
	if [ ! -d "$file" ]; then
		tStamp="$(stat -c "%y" "$file" | cut -d " " -f1)"
		fType="$(file -p -b "$file" | cut -d " " -f1)"
		mkdir -p "$DownloadStorage/$tStamp/$fType"
		mv -n "$file" "$DownloadStorage/$tStamp/$fType" && \
			echo "moved $file to $tStamp/$fType" || \
			echo "failed to move $file $tStamp"
	fi
done
