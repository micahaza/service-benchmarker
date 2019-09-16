# Service Benchmarker

## Description
The task is to write a program which could stress test specific services.
* We want this program to be able to parse other services logfiles and run stress tests based on the data gathered.
* We want to be able to specify, how many requests per second we send to the specific service.
* We want to be able to specify, how long the test should run.
* We want this service to be able to send concurrent requests in order to simulate a real network load.
* We want to save HTTP response status codes for later analysis.

## Test scenario assumptions, prerequisites
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
* Run test for 10 minutes and 100 requests every second.
* Store results in Queue.
* Do some basic analysis on ~60K requests/responses
