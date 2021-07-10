Batmouse
========

![](https://github.com/tarcisioe/batmouse/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/tarcisioe/batmouse/branch/main/graph/badge.svg)](https://codecov.io/gh/tarcisioe/batmouse)

A library for getting battery status and percentage from wireless mice.

Currently supports Linux's `/sys/class/power_supply` interface only.


Basic usage
===========

`batmouse` can list all known peripherals plugged through the
`get_sys_power_supply_mice` function (for Linux's sys interface):

```python
from batmouse.api import get_sys_power_supply_mice

for mouse in get_sys_power_supply_mice():
    print(mouse.model)
    print(mouse.percentage.value)
    print(mouse.percentage)
```


Contributing
------------

Check our [contributing guide](CONTRIBUTING.md) to know how to develop on
Batmouse and contribute to our project.
