#!/bin/env bash

ACCENT="$1"
OUTFILE="$2"

[ -z "$OUTFILE" ] && OUTFILE="custom.theme"

printf "%s" "
# Directory colors
set color_win_dir=default

# Normal text
set color_win_fg=default

# Window background color.
set color_win_bg=default

# Command line color.
set color_cmdline_bg=default
set color_cmdline_fg=default

# Color of error messages displayed on the command line.
set color_error=lightred

# Color of informational messages displayed on the command line.
set color_info=yellow

# Color of currently playing track.
set color_win_cur=$ACCENT

# Color of the separator line between windows in view (1).
set color_separator=black

# Color of window titles (topmost line of the screen).
set color_win_title_bg=$ACCENT
set color_win_title_fg=black

# Status line color.
set color_statusline_bg=$ACCENT
set color_statusline_fg=black

# Color of the line displaying currently playing track.
set color_titleline_bg=default
set color_titleline_fg=$ACCENT

# Color of the selected row which is also the currently playing track in active window.
set color_win_cur_sel_bg=$ACCENT
set color_win_cur_sel_fg=black

# Color of the selected row which is also the currently playing track in inactive window.
set color_win_inactive_cur_sel_bg=default
set color_win_inactive_cur_sel_fg=$ACCENT

# Color of selected row in inactive window.
set color_win_inactive_sel_bg=default
set color_win_inactive_sel_fg=$ACCENT

# Color of selected row in active window.
set color_win_sel_bg=$ACCENT
set color_win_sel_fg=black

# Command line color.
set color_cmdline_bg=default
set color_cmdline_fg=$ACCENT
" > "$OUTFILE"
