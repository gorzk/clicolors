##clicolors - Command Line Interface::Colors
###Simply Python module to colorize your Linux terminal. 
---
Usage:
```python
from clicolors import colors

# example 1
    print colors('Example text 1', fg='blue',bg='red',attr='bold')
```

```python
# example 2
    print colors('Example text 2', 'blue','red','bold')
```

```python
# example 3
    print colors('Example text 3', fg='yellow')
```

```python
# example 4
    print colors('Example text 4', 'yellow')
```

```python
# example 5
    print colors('Example text 5', bg='green')
```

```python
# example 6
    print colors('Example text 6',attr='underline')
```

```python
# example 7
    print colors('Example text 6',bg='cyan',attr='underline',fg='black')
```
```python
# clicolors Demo
    print colors('clicolors : Lightweight Python script for styling strings in your Linux terminal',fg='black',bg='white',attr='underline')
    print ('Foreground: '+' '.join([colors(color, fg=color) for color in COLORS]))
    print ('Background: '+' '.join([colors(color, bg=color) for color in COLORS]))
    print ('Attributes: '+' '.join([colors(attributes, attr=attributes) for attributes in ATTRIBUTES]))
```
