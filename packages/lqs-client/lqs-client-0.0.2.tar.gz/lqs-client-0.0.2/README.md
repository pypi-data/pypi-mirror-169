<p align="center">
  <br/>
  <img src="misc/images/logqs_logo.png?raw=true" alt="LogQS Logo" width="250"/>
</p>

# LogQS Client


## Setup

The LogQS Client module source is located in `lqs-client` and it's Python requirements are listed in the `requirements.txt` file.  You can install it locally with `pip install .`.

#### Development

The project uses Python 3.9, which may require some dependencies to be required.  In one go,

    sudo apt install python3.9 python3.9-dev python3.9-distutils python3.9-venv

To run the application from this directory (i.e., for development):

1. Create a virtual environment:

    `python3.9 -m venv venv`

2. Source the environment:

    `source venv/bin/activate`

3. Install the requirements:
    
    `pip install -r requirements.txt`

4. Install LogQS Client in develop mode:
    
    `pip install -e .`

5. Run the module:
    
    `python -m lqs-client`
