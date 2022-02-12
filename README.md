## Tangelo Challenge

Technical tests done for the company  [Tangelo](https://www.tangelolatam.com/).

### Built With

This project is built in  [Python](https://www.python.org) and uses the following libraries:

* [Requests](https://docs.python-requests.org/en/latest/)
* [Pandas](https://pandas.pydata.org/)
* [SQLite](https://www.sqlite.org/index.html)

<!-- GETTING STARTED -->
## Getting Started

This is an application that consumes a service exposed by [Rest Countries](https://restcountries.com/), then filters the information according to the requested requirements. It uses Pandas DataFrame to manipulate the information in a proper way, calculates time measurements and finally connects to a database and records the execution times. If the database or the table does not exist, it creates it, additionally it saves in json format the information hosted in the database table.

Below is the design of the solution:

![Untitled Diagram drawio (1)](https://user-images.githubusercontent.com/17171887/153727679-6dbefb8e-92fe-4686-856f-104fc6de37e8.png)


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

This is an example of the information he has saved with SQLite and visualized in [Visual Studio Code](https://code.visualstudio.com/) with the SQLite Viewer extension.

![image](https://user-images.githubusercontent.com/17171887/153725399-8af11b75-05b5-4762-8b01-a4fbebe7444f.png)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
