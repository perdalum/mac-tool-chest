#!/usr/bin/env sh
#
# ascii_plot.sh — draw a horizontal ASCII bar chart from stdin.
#
# Input format (from stdin):
#     label value
#     label value
#     ...
#
# Example:
#     echo "
#     wls 2643
#     Julia 3937
#     Python 6749
#     " | ./ascii_plot.sh
#
# Output (approx):
#     wls    ####################
#     Julia  ############################
#     Python ############################################
#
# The script finds the maximum value and scales all bars
# to fit within a fixed width (default: 50 chars).

bar_width=50    # max bar length

# 1) read all input once and compute max
#    store lines in a temp awk array for second pass
awk -v width="$bar_width" '
{
    data[NR]=$0
    if ($2 > max) max = $2
}
END {
    if (max == 0) max = 1

    for (i = 1; i <= NR; i++) {
        split(data[i], f)
        name = f[1]
        val  = f[2]

        len = int((val / max) * width + 0.5)

        bar = ""
        for (j = 0; j < len; j++) bar = bar "#"

        printf "%-6s %s\n", name, bar
    }
}
'
