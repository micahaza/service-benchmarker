# Service Benchmarker

## Description
The task is to write a program which could stress test specific services.
* We want this program to be able to parse other services logfiles and run stress tests based on the data gathered.
* We want to be able to specify, how many requests per second we send to the specific service.
* We want to be able to specify, how long the test should run.
* We want this service to be able to send concurrent requests in order to simulate a real network load.
* We want to save HTTP response status codes for later analysis.

## Thoughts
* I've checked couple of testing stuffs, could not find suitable solution.
* I'm going to use threads instead of processes as starting a thread in python is much faster and cheaper than starting a new process.
* Because of threads I'm going to use Queue.
* Parsing a log file could be quite tedious so I'm going to do fake log file parsing.

## Test scenario assumptions, prerequisites
* We use python 3.7.3
* We want to test Important Service (IS) for 10 minutes and send approximately 100 requests every second.
* IS logfiles are available for our test environment with enough data to perform the test.
* We parse these logfiles, we build a Queue with data: 
  * URL
  * Request method
  * Headers
  * Request payload, parameters
* For testing the Service Benchmarker I'd use a simple Flask application which will send random HTTP codes back for every request with random response times.


## Service Benchmarker pseudo run
* Configure and initialize application.
* Build Queue for testing.
* Run test for 10 minutes and 100 requests every second by batching requests in bundles of 100 requests.
* Store results in Queue.
* Do some basic analysis on ~60K requests/responses

## Running the test
* Clone the repository
* bash$ virtualenv -p python3 env
* bash$ source env/bin/activate
* bash$ pip install -r requirements.txt
* bash$ python app.py

Then in another terminal

* bash$ cd service-benchmarker
* bash$ source env/bin/activate
* bash$ python service_benchmarker.py

## Future improvements
* Adding log file parsers
* Building Queue from real log files
* More real request distributions during tests
* Making the Service Benchmarker configurable
* Adding tests