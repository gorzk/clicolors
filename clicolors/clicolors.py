#!/usr/bin/env python

# Copyright (c) 2014-2015 Krzysztof Gorzynski <gorzynskikrzysztof@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


__version__ = '0.1'

# General text attributes
ANSI = "\033["
ANSI_RESET = "\033[0m"
ATTRIBUTES = ('default', 'bold', 'italic', 'dim', 'underline', 'blink', 'reverse', 'hidden')

# Fore and background attributes
COLORS = ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'default')

def colors(text, fg=None, bg=None, attr=None):
    if fg:
        if fg in COLORS:
            fore = str(30+COLORS.index(fg))
    else: fore='39'

    if bg:
        if bg in COLORS:
            back=str(40+COLORS.index(bg))
    else: back='49'

    if attr:
        if attr in ATTRIBUTES:
            style=str(ATTRIBUTES.index(attr))
    else: style='10'
    return str(ANSI+ ''.join(fore+';'+back+';'+style)+'m')+text+ANSI_RESET

def demo():
    print colors('clicolors : a simple python script for styling strings in the terminal',fg='black',bg='white',attr='underline')
    print ('Foreground: '+' '.join([colors(color, fg=color) for color in COLORS]))
    print ('Background: '+' '.join([colors(color, bg=color) for color in COLORS]))
    print ('Attributes: '+' '.join([colors(attributes, attr=attributes) for attributes in ATTRIBUTES]))

if __name__=='__main__':
    demo()

