# run
```
python3 my_package
```


# unit testing
```
cd ./my_package
python3 -m unittest   
```



## Install & run (for testing):
```
pip install .
# run project
my_package
```



# Build Project (for distributing and system install):

```
pip install build # <-- only if not yet installed
python -m build
```

This will create a `./dist/[...].tar.gz` package. <br>
This file could not be ...
- ... [distributed on PyPI](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives)
- ... installed via `pip install ./dist/[...].tar.gz`


