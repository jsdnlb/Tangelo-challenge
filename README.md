## Tangelo Challenge

Technical tests done for the company  [Tangelo](https://www.tangelolatam.com/).

### Built With

This project is built in  [Python](https://www.python.org) and uses the following libraries:

* [Requests](https://docs.python-requests.org/en/latest/)
* [Pandas](https://pandas.pydata.org/)
* [SQLite](https://www.sqlite.org/index.html)

## Getting Started

This is an application that consumes a service exposed by [Rest Countries](https://restcountries.com/), then filters the information according to the requested requirements. It uses Pandas DataFrame to manipulate the information in a proper way, calculates time measurements and finally connects to a database and records the execution times. If the database or the table does not exist, it is created, additionally the app saves the data table in the DB in JSON format.

Below is the design of the solution:

![Untitled Diagram drawio (1)](https://user-images.githubusercontent.com/17171887/153727679-6dbefb8e-92fe-4686-856f-104fc6de37e8.png)


### Improvements

SHA1 encryption is not recommended for new designs, even in its own page it says so, I was investigating new methods and I found Fernet (symmetric encryption): Fernet guarantees that an encrypted message cannot be manipulated or read without the key.

With this update, the board looks like this:

![image](https://user-images.githubusercontent.com/17171887/153768524-ee86bc77-a2a6-46f2-94df-9f3f40c58ef6.png)


### Prerequisites

The program needs git to clone it and python to run it.

### Installation

Installation is really simple

1. Clone the repository
   ```sh
   git clone https://github.com/jsdnlb/tangelo-challenge
   ```
	Enter the folder
   ```sh
   cd tangelo-challenge/
   ```
2. Create the virtual environment
   ```sh
   python3 -m venv venv
   ```
	And then active the virtual environment
   ```sh
   source venv/bin/activate
   ```
4. Build the application, this was implemented to do the unit tests.
   ```sh
   pip install -e .
   ```
4. Install the dependencies   `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```
## Usage

To run the application you only have to run the file as follows:

 ```sh
   python3 app/bin/run.py
   ```

The answer will be similar to the following, depending on the quality of your internet.

![test3 (online-video-cutter com)](https://user-images.githubusercontent.com/17171887/153728428-84125d3b-ebaf-478c-b6df-1e8b071b8fb1.gif)

This is an example of the data saved by the app using SQLite and visualized in [Visual Studio Code](https://code.visualstudio.com/) with the SQLite Viewer extension.

![image](https://user-images.githubusercontent.com/17171887/153725399-8af11b75-05b5-4762-8b01-a4fbebe7444f.png)


## Unit test 

To use the unit tests you only have to run the files that are in the `test` folder, for example I will show the tests for encryption:


   ```sh
   # SHA1 method:
   python3 app/test/test_encrypt_sha1.py
   # Fernet method:
   python3 app/test/test_encrypt_fernet.py 
   ```

This is the result: 

![image](https://user-images.githubusercontent.com/17171887/153768221-70150b53-0fa3-4a57-9863-57080da1a4dc.png)


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
