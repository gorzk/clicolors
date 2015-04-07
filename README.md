###
clicolors - Command Line Interface - Colors
Simply Python module to colorize your Linux terminal. 

Usage:
```python
from clicolors import colors

# example 1
    print colors('Example text 1', fg='blue',bg='red',attr='bold')

# example 2
    print colors('Example text 2', 'blue','red','bold')

# example 3
    print colors('Example text 3', fg='yellow')

# example 4
    print colors('Example text 4', 'yellow')

# example 5
    print colors('Example text 5', bg='green')

# example 6
    print colors('Example text 6',attr='underline')

# example 7
    print colors('Example text 6',bg='cyan',attr='underline',fg='black')
```