Useful tools to work with TigerGraph in Python

# Description
    
It consists of one module:

- `tghelper`: helper functions to work with TigerGraph and pyTigerGraph

With two main functions:

- `execute_gsql`: Execute a gsql statement that is stored in a file
- `upload_job`: Uses multiprocessing to upload the file and then executes the loading job for the file

### Examples

```python
import pyTigerGraph
from tghelper import TgHelper
import getpass

my_pwd=getpass.getpass()
tg_conn = pyTigerGraph.TigerGraphConnection(host="http://127.0.0.1", graphname="MyGraph",
                                            username="usr_name", password=my_pwd)
tgh = TgHelper(conn=tg_conn)
tgh.execute_gsql("my_gsql_statement.gsql")

tgh.upload_job(source_ffile="my_data.csv", 
               job="my_loading_job", 
               job_filename="job_filename")

```
# Installation
 
## Normal installation

```bash
pip install tghelper
```

## Development installation

```bash
git clone https://github.com/louisza/tghelper.git
cd tghelper
pip install --editable .
```

## pypi Build reminder (for the developers)

```bash
python3 setup.py sdist bdist_wheel
