# NASA API Test Automation

This project is an automation of test cases to validate the NASA Astronomy Picture of the Day (APOD) API using Behave and Docker. The tests check the status of the API response and validate specific data points returned for a given date.

## Requirements

- Python 3.12
- Docker (for running the tests in a containerized environment)
- Git
- `pip` or `pipenv` (for managing dependencies)

## Getting Started

To set up the project and run the tests, follow these steps:

### 1. Clone the repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/MaksimLiV/nasa_api.git
cd nasa_api
```

2. Set up your API key
	•	Create a .env file by copying the provided example.env file:
cp example.env .env
	•	Open the .env file and insert your NASA API key:
NASA_API=YOUR_API_KEY

3. Run the tests using Docker
To run the tests in a Docker container, use the provided run-tests.sh script:

```bash
chmod +x run-tests.sh
./run-tests.sh
```

4. Test Results
After running the tests, you will see the output in the terminal, which indicates whether all tests passed or if there were any failures.
Feature: NASA API Interaction
This project validates the response from the NASA Astronomy Picture of the Day API.
Scenario: Validate Astronomy Picture of the Day API for defined date

The test checks the following:

	1.	Ensure the API returns a 200 status code.
	2.	Validate that the response contains certain keys: title, explanation, url, media_type, and date.
	3.	Ensure that the media type is either image or video.
	4.	Check that the date in the response matches the requested date.

Example of Dates Tested:

	•	Yesterday’s picture
	•	Specific dates (e.g., 2024-10-13, 2024-09-13)

Notes

	•	Make sure Docker is installed on your machine to run the tests in a containerized environment.
	•	If you encounter issues with the tests, ensure that the .env file is properly set up with your NASA API key.

### Steps to run the project:
1. **Clone the repository.**
2. **Insert your API key into the `example.env` file as `YOUR_API_KEY` and save it as `.env`.**
3. **Run the tests using the `run-tests.sh` script after copying and setting the execute permissions.**
