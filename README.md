**june17**
- changed it to app to core
- logger is accessible to whole project through 
- added some new files like `orchestrator.py` `main.py` `scrappers` i will work on them later 
``` py
from core import Logger
logger = Logger.get_logger('name of the file you are workign','where you wanna save your log')
```
and the outpu would look like this
```
logs
├── Data Exporters.log
├── Utils.log
└── notebook.log

1 directory, 3 files
```
---
**june18**  
- Data Exports
    - converted the classes to Dry
    - checked alll the functions
    - changed the logger names 
- Utils 
    - checked all the functions
    - detedted problem in selenium utils
---
**june19**  
- Data exports/ Filesaver
    - refactoring 
    - appding
    - Dry, minimul , dynamic

---
