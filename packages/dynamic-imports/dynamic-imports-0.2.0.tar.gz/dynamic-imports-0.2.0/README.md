## Dynamically discover and import Python modules and classes

### Import a module via module name or file path
```python
from dynamic_imports import import_module
module = import_module('my_package.my_module')
# or
module = import_module('/home/user/my_package/my_module.py')
```
### Import a module attribute
```python
from dynamic_imports import import_module_attr

function = import_module_attr('my_package.my_module', 'my_function')
# or
function = import_module_attr('/home/user/my_package/my_module.py', 'my_function')
```

### Find all modules in a package or nested packages
```python
from dynamic_imports import get_modules

modules = get_modules(
    package=my_package, # str `my_package' works too.
    search_subpackages=True,
    # return the actual module objects, not str names.
    names_only=False,
)

```

### Find all implementations of a base class within a module.
```python
from dynamic_imports import module_class_impl
from my_package.my_module import Base
from my_package import my_module

my_classes = module_class_impl(
    base_class=Base, # str 'Base' works too
    module=my_module,
    names_only=False
)
```

### Find all implementations of a base class within a package.
```python
from dynamic_imports import pkg_class_impl
from my_package.my_module import Base
import my_package

my_classes = pkg_class_impl(
    base_class=Base, # str 'Base' works too.
    package=my_package
    search_subpackages=True,
    names_only=False,
)

```

### Find all instances of a class within a module.
```python
from dynamic_imports import module_class_inst
from my_package import my_module
from my_package.my_module import MyClass

my_classes_instances = module_class_inst(
    module=my_module, # str 'my_package.my_module' works too.
    class_type=MyClass
)
```

### Find all instances of a class within a package.
```python
from dynamic_imports import pkg_class_inst
from my_package.my_module import MyClass
import my_package

my_classes_instances = pkg_class_inst(
    class_type=MyClass,
    package=my_package, # str 'my_package' works too.
    search_subpackages=True,
)
```