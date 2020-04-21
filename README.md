This is a Toy example of a Blockchain built with Python.

*TODO*: 
* Functionalities for a Wallet and a Crypto Currency.
* Frontend with Javascript and Vue.

The code is based on:
https://github.com/15Dkatz/python-blockchain-tutorial/tree/7bd90f944e8b78bddd1d3c5b781787c1a513bf36

The mine rate can be adjusted in the config.py file
Based on this mine rate the block difficulty is adjusted when a new block is mined.

**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**

```
pip3 install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment.

```
python3 -m pytest backend/tests
```