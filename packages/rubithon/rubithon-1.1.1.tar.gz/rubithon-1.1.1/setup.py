#!/bin/python
import re
from sys import argv
from setuptools import setup, find_packages
requires = ["requests", "pycryptodome==3.10.1", "urllib3", "tqdm", "rich", "websocket-client"]
version = "1.1.1"
readme = """
<p align="center">
    <a href="https://github.com/irmilad/rubika">home</a>
    <br>
    <b>rubithon for rubika client, python 3 | milad heidari</b>
    <br>
    <a href="https://github.com/irmilad/rubx/blob/main/README.md">
        document
    </a>
    •
    <a href="https://github.com/irmilad">
        github
</p>

# Rubika Client for python 3

<div align="center">

![issues](https://img.shields.io/github/issues/IRMilad/rubika)
![forks](https://img.shields.io/github/forks/IRMilad/rubika)
![version](https://img.shields.io/badge/version-v--22.6.7--beta-yellow)
![stars](https://img.shields.io/github/stars/IRMilad/rubika)
![license](https://img.shields.io/github/license/IRMilad/rubika)
![icon](https://github.com/IRMilad/rubika/raw/main/icon.png)
</div>


# install 

```pip install rubithon```

# exmaple 

```python 
import asyncio
from rubithon import Client, models, handlers


async def main():
    async with Client(session='rubika') as client:
        @client.on(handlers.MessageUpdates(models.author_guid() == client._guid))
        async def updates(update):
            await update.reply('`hello` __from__ **rubika**')
        await client.run_until_disconnected()

asyncio.run(main())
```


# [methods](https://github.com/IRMilad/rubika/blob/main/rubika/gadgets/methods.py) class

* ## You can find the list of methods in the [methods.json](https://github.com/IRMilad/rubika/blob/main/rubika/methods.json)

* The list of methods is divided into 9 groups, which are:
    `users`,
    `chats`,
    `extras`,
    `groups`,
    `messages`,
    `channels`,
    `conracts`,
    `settings`,
    `stickers`,
    `authorisations`


## The output of all methods is a dictionary that you must give to the __call__ method

* # Example 

```python 
from rubithon import Client, methods

client = Client(...)
result = await Client(methods.users.GetUserInfo(user_guid='...'))
```

## Example to get the list of methods of a group

```python
from rubithon import methods
print(dir(methods.users))
```


* ## Example of getting the list of arguments of a method


```python
from rubithon import methods
print(methods.users.SetBlockUser)
```


## Raises
* TypeError: if the data type is inconsistent with the allowed values types
* ValueError: if the value does not exist in the allowed list


# [handlers](https://github.com/IRMilad/rubika/blob/main/rubika/structs/handlers.py) class

* Including 5 classes (may be increased) which are:
    `ChatUpdates`,
    `MessageUpdates`,
    `ShowActivities`,
    `ShowNotifications`,
    `RemoveNotifications`

* These are used to filter updates, whose names indicate what type of update they receive.

## The inputs of these classes are [models](https://github.com/IRMilad/rubika/blob/main/rubika/structs/models.py), If __any is true, OR operator is placed between the filters, otherwise AND


# Filters can be functions Example
```python
from rubithon import handlers


async def custom_filter(update, result):
    return update.raw_text

handlers.MessageUpdates(custom_filter)

```


## Tips
* Filters can be functions
* Between the filters you can use the operators `|`, `&`, `!=`, `==`, `>`, `>=`, `<`, `<=`  use
* To use the operators, the filter (model) must be called


# [models](https://github.com/IRMilad/rubika/blob/main/rubika/structs/models.py) class

* Including 3 classes,  which are:
    `Operator`,
    `BaseModels`,
    `RegexModel`

# You can use all the attributes of the update, the most important of which have already been written

# Examples 

```python

async def custom_filter(update, result):
    return result


handlers.MessageUpdates('hi' != models.raw_text())
handlers.MessageUpdates(custom_filter != models.raw_text())


handlers.MessageUpdates(custom_filter == models.time(func=int))


handlers.MessageUpdates(models.RegexModel(pattern=r'hi'))
```

# Multiple Filters (AND)

```python
handlers.MessageUpdates(
    (15 < models.time(func=int) > 10)
    &
    models.RegexModel(pattern=r'hi')
    &
    models.is_private
)

# or


handlers.MessageUpdates(
    15 < models.time(func=int) > 10,
    models.RegexModel(pattern=r'hi'),
    models.is_private
)

```

# Multiple Filters (OR)

```python
handlers.MessageUpdates(
    models.is_private
    |
    (models.author_guid() == 'GUID')
)

# or 

handlers.MessageUpdates(
    models.is_private,
    models.author_guid() == 'GUID',
    __any=True
)

```


## Get updates (add handler)

```python

async with Client(session='rubika') as client:
    @client.on(handler)
    async def updates(update):
        pass


# or

async with Client(session='rubika') as client:
    async def updates(update):
        pass
    
    client.add_handler(updates, handler)
    
```


## ✌ در آرزوی جهانی  ...


"""

setup(
    name="rubithon",
    version=version,
    description="ribithon created by milad heidary",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/irmilad/rubika",
    download_url="https://github.com/irmilad/rubika/releases/latest",
    author="milad heidary",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    keywords=["milad heidary","messenger","python","python3","api","self","Rubika","rubika","bot","robot","library","rubikalib","rubikalibrary","rubika.ir","web.rubika.ir","m.rubika.ir"],
    project_urls={
        "Tracker": "https://github.com/irmilad/rubika/issues",
        "Source": "https://github.com/irmilad/rubika",
        "Documentation": "https://github.com/irmilad/rubika/blob/main/README.md",
    },
    python_requires="~=3.5",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requires
)