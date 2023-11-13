# Add workspace folder to PYTHONPATH
## Add lines in settings.json 
```json
"terminal.integrated.env.windows": {"PYTHONPATH": "${workspaceFolder}"},
"jupyter.notebookFileRoot": "${workspaceFolder}",
```
settings.json can be located in /workspacefolder/.vscode/ if you want it to be specific to your project.  

This manipulation prevents from typing
```py
import sys
sys.path.append(workspacefolder)
```