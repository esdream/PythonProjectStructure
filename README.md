## Project Structure of Python
This is a project structure of Python.


### Directory Tree
The directory-tree was built as follow.
```
MODULETEST
├─data
├─doc
└─module_package
    ├─subpackage1
    │  └─subpackage11
    ├─subpackage2
    └─test
```

+ data: where you store your project data.
+ doc: where you store your doc.
+ module_package: a demo python package to store your major codes of this project. You should create a `__init__.py` in every package and its subpackages so that Python will add all packages in module tree.
    + subpackage1, subpackage2, subpcakge11: demo directories of subpackages.
    + test: where you store your unit test of your package.

The `README.PY` and `.gitignore` should be established in the root of project.


### Importation
If you import other module in same package, you should use absolute path of package for unification of outside and inside of package. for instance, if you want import `module_package/subpackage1/foo1.py` in `module_package/subpackage2/foo2.py`, you should add write code as follow:
```python
from module_package.subpackage1 import foo1
```

Similarly, if you import module out of package(in this case you import `module_package/subpackage1/foo1.py` in `test.py`), you can write code as follow:
```python
from module_package.subpackage1 import foo1
```


### Execution
If you want execute module in the package, you should confirm that your execution directory in the project, and execute following shell:
```shell
python -m 'module_refer_to_package'
```
For instance, you want execute `module_package/subpacakge1/foo1.py`, you should write shell as follow:
```shell
ptyhon -m module_package.subpackage1.foo1
```