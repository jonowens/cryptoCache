# CryptoCache Store
Project3 for Rice University FinTech Bootcamp

---

## Table of contents
* [General Information](#general-information)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Installation Guide](#installation-guide)
* [Code Examples](#code-examples)
* [Usage](#usage)
* [Sources](#sources)
* [Status](#status)
* [Contributors](#contributors)

---

## General Information

The purpose of this project is to design a webstore which will accept information from a user via a browser interface processing the information through Javascript into a Smart Contract located on the Ethereum blockchain.  Javascript will then initiate an orderPrint transaction which will process through Python code via Flask allowing for the user information to be sent on to a 3D printing company to print a desired Pink or Blue Token.

---

## Screenshots



---

## Technologies

Python 3.7.7
See [requirements.txt](requirements.txt) for a list of libraries to create a cryptocache environment.

---

## Installation Guide

1. Download the entire repository
2. Open Git Terminal
3. Navigate into the repository file path where you stored the files during the download.
5. Make sure to create a separate virtual environment for the ethereum technologies (cryptocacheenv).
6. Use [requirements.txt](requirements.txt) in the repository to install the libraries using the following commands:

    - conda deactivate
    - conda create -n cryptocacheenv python=3.7
    - conda activate cryptocacheenv
    - pip install -r requirements.txt
    - If the previous command has errors try:
        - conda install -r requirements.txt

*See the [Usage](#usage) section below for instructions to run the notebook.

---

## Code Examples

### HTML Code

```

```

### Solidity Contract Code

```
function orderPrint(
        address buyer,
        string memory country,
        string memory state,
        string memory city,
        string memory streetAddress,
        uint zipCode
        ) public payable returns(uint) {

        uint price = 10000000000000;
        uint pricePaid = msg.value;

        require (pricePaid >= price, “You need to deposit exactly 10000000000000 wei!“);
```

### 


---

## Usage

Info here

---

## Sources

- [1] https://developers.shapeways.com/quick-start

- [2] https://oneclickdapp.com/

- [3] 

---

## Status

Project is: _in progress_

---

## Contributors

* Carolina Benzaquen
* Dragan Bogatic
* Jonathan Owens
