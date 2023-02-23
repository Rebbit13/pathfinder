# Simple app to find path in rectangle fields

## Input

File input.json
format
```json
{
    "board": [[0, 1], [10, 10], [1, 1]],
    "target": [1, 2]
}
```
## Deploy on *nix systems
Require python >= 3.10

> pip install -r requirements
> 
> python3 main.py

## Output

App draw path to file output.png and write all useful information
to stdout
