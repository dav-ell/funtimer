# funtimer
Time your functions in less lines of code with this fun function wrapper

```
do_things(arg1, arg2, arg3=True)
```

and time it like this

```
from funtimer import timing
timing(do_things)(arg1, arg2, arg3=True)
```
