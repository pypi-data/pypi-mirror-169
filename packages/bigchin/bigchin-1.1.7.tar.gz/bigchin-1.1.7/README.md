Description
===========
**This small library contains some useful functions that you would need in the implementation of projects. Every time the library is updated, and many other useful functions are added to it**

Using
===========
Using 1.0
-----------
### In the code below, you can make a small game that depends on luck. With this function, you can specify the chances of "winning" and return *True*, or lose.
```python
from bigchin import perform
my_chance = perform.perchance(50) # 50 - Your chances
if my_chance is True:
    print("Win!")
elif my_chance is False:
    print("lose.")
```
If you win, then you return *True*. In case of defeat - *False*
**Maximum chances: 100**
**Minimum chances: 0** _(Best of all - 1)_



### In the next function you will be able to set your *maximum unit of luck*
```python
from bigchin import perform
my_custom_max_chance = 200 # 200 - Your any number
my_chance = perform.perchances(my_custom_max_chance)
if my_chance > 50:
    print("Win!")
elif my_chance <= 50:
    print("lose.")
```

### If you are working with a large and important project, and you choose numbers as the maximum size, except for the standard ones [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], then you will have to quickly enter into the console - *"y"* _(Operation confirmation)_.
As we know, if you specify the number of the maximum size of the odds except [100, 200, 300, 400, 500, 600, 700, 800, 900, 100], **then you will have a warning where confirmation of the operation is required.**
To skip it, set an additional parameter to *True*
```python
from bigchin import perform
my_custom_max_chance = 450 # 450 - Your any number
my_chance = perform.perchances(my_custom_max_chance, True)
if my_chance > 50:
    print("Win!")
elif my_chance <= 50:
    print("lose.")
```



### In the **system** class, it will be possible to view system functions or information in future updates.
#### Version view (1)
```python
import bigchin
version = bigchin.system.ver()
print(version)
```
#### Version view (2)
```python
from bigchin import system
version = system.ver()
print(version)
```



### There is a small analogue of the *perchance* function. If you need to use several variables at once, then you can use the following function
```python
from bigchin import perform
my_dict_chance = perform.permchance(10, 20, 40) # 10, 20, 40 - Your chances
print(my_dict_chance)
```
In the output we will get *dict* with our variables



### If you are working on some game (Let's say daily-rewards), then you definitely need a system with a *calculation of luck for a certain reward*. In the next function you will be able to implement this
```python
from bigchin import perform
my_chance = perform.сpermchance(30, 60) # 30, 60 - Your chances
print(my_chance)
```
In the console, we will most likely see: - **60**

Let's say you need a program for determining the luck of some boxing, case (gaming) that are designed only on luck. The most expensive rewards will be likely with 10% chances (for example), and the most ordinary ones with 90%. 
The *сpermchance* function simplifies this implementation. Here is an example code corresponding to our above-mentioned "game" designed for luck"
```python
from bigchin import perform
probability_a_price_reward = 10 # 10%
probability_of_usual_reward = 90 # 90 %
result = perform.сpermchance(probability_a_price_reward, probability_of_usual_reward)
if result == probability_a_price_reward:
    print("Win!")
elif result == probability_of_usual_reward:
    print("so-so...")
```
That is, the probability for a **valuable reward is 10%**, and for an **ordinary, standard reward is 90%**