# Disclaimer

This project is a best-effort project. Not everything described here might be optimal, but it worked well for my specific cases. If you have any suggestions, please file an issue or merge request.

# What is this

This is a template for creating new python projects with a proper structure.

The template focusses on the following function:

- Correct way of importing stuff
- Runnable unittests:<br>
  `python3 -m unittest`
- Runnable by specifying the main folder:<br>
  `python3 ./my_package`
- Runnable by specifying only the package in your CLI:<br>
  `my_package`<br>
  (After building and install)

**Be very careful to change the basic structure in this template. Imports might break without you even realizing it for a long time**


# How to use 

* Do global search & replace:<br>
  search: `my_package` <br>
  replace: `<YOUR PACKAGE NAME>`
* Customize my_package/setup.cfg 
* No need to customize my_package/pyproject.toml
* Understand, that the **entry point for this project** is:<br>
   `src/my_package/my_package/main/main.py:main_function()`



# build / install

see [readme in subdir](./src/readme.md)



# Developing this template

- Be careful: before testing, if unittesting or `python my_package` works, make sure to uninstall the package first (`pip uninstall my_package`)<br>
After `pip install .`-ing, imports get resolved differently; Things might work, even if they should break




# References

I used the following references to come up with this template

* 10+ hours of trial & error
* Slowly introducing the topic, but not going all the way<br>
  https://dev.to/demianbrecht/entry-points-in-python-34i3
* Same information as (1)<br>
  https://packaging.python.org/en/latest/tutorials/packaging-projects/
* Explains the "very important" part here<br>
  https://setuptools.pypa.io/en/latest/userguide/entry_point.html