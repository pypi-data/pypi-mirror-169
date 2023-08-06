# pemap
Pemap is simple python library for associating ordinary python object
with value. Value for object helps in performing most operations on object
and getting more information on it.

Value can be used get items or sort them instead of the object directly. An object with its value forms **item** and multiple items forms **block**. 
Block can also be kept inside item which would result in nested blocks since 
block may contains another block if that item is used within block.

> Value can be any python object.


### Install
Enter this to your command-line application:
```bash
pip install pemap
```

### Usage

First import pemap to use its functions
```python
import pemap
```

Creates item which is combination of object with its value. Realise that 
value can be another type than integer or number. Value and object
item can be accessed using methods. 


```python
marry_item = pemap.create_item("Marry", 30)
john_item = pemap.create_item("John", 10)
ricky_item = pemap.create_item("Ricky", 40)

marry_item.get_object() # 'Marry'
marry_item.get_value() # 30

#marry_item.set_value(20)
#marry_item.get_value() # 20
```

After creating items you may consider creating block object to hold the 
items. Block makes it easy to work with multiple items such as accessing 
them based on their values.

```python
# List of items to use with block
items = [marry_item, john_item, ricky_item]
# Creates block object containing items
items_block = pemap.create_block(items)

items_block.get_values() # ['Marry', 'John', 'Ricky']
items_block.get_objects() # ['Marry', 'John', 'Ricky']
```
> Block object contain even more methods.


It is possible to have nested blocks in that items of block contain another
block. Accessing items within nested block can be hard with previous 
example. But it can be simple if using `pemap.create_deep_block()` instead
of `pemap.create_block()` which does not take into account nested blocks.

```python
# Create first block with items
first_block_items = [marry_item, john_item, ricky_item]
first_block = pemap.create_block(items)
# Now create item from block and give value of 300.
first_block_item = pemap.create_item(first_block, 300)

# Create item for second block
first_block_item = pemap.create_item(first_block_item)

# Create ben item and followed by second block.
# Realise that second block contains first block with items.
ben_item = pemap.create_item("Ben", 100)
second_block_items = [ben_item, first_block_item]
second_block = pemap.create_deep_block(second_block_items)

# Underlying objects from first block can be accessed in second block.
# First block has been eliminated but its items remained.
second_block.get_objects() # ['Ben', 'Marry', 'John', 'Ricky']
```

Block can be converted to other python objects like dictionary, tuple 
and value queue. This only takes into account block items excluding
useful data like block value.

```python
items = [marry_item, john_item, ricky_item]
items_block = pemap.create_block(items)

items_block.to_tuple() 
# ((10, 'John'), (30, 'Marry'), (40, 'Ricky'))
items_block.to_dict() 
# {10: 'John', 30: 'Marry', 40: 'Ricky'}
items_block.to_multi_dict() 
# {10: {'John'}, 30: {'Marry'}, 40: {'Ricky'}}
```


Most of block methods are available as functions ready to be used on items
without creating block object. 
```python
items = [marry_item, john_item, ricky_item]
pemap.items_to_tuple(items) 
# ((10, 'John'), (30, 'Marry'), (40, 'Ricky'))
pemap.extract_objects(items)
# ['Marry', 'John', 'Ricky']
```

### License
[MIT license](https://github.com/sekgobela-kevin/pemap/blob/main/LICENSE)
