from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import requests
from behave import given, when, then

load_dotenv()


@given("I have the NASA API key")
def step_impl(context):
    context.api_key = os.getenv("NASA_API")
    if not context.api_key:
        raise AssertionError("API key not loaded")
    context.base_url = "https://api.nasa.gov/planetary/apod"


@when('I query the API for "{date}"\'s picture')
def step_impl(context, date):
    if date == "yesterday":
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    context.date_requested = date
    params = {"api_key": context.api_key, "date": date}
    context.response = requests.get(context.base_url, params=params)


@then("the HTTP status code is 200")
def validate_response_status(context):
    status_code = context.response.status_code
    if status_code != 200:
        raise AssertionError(
            f"Expected status code 200, but got {status_code}. "
            f"Response text: {context.response.text}"
        )
    try:
        context.response_data = context.response.json()
    except ValueError as e:
        raise AssertionError(f"Failed to parse JSON response: {str(e)}")


@then('the response should include keys "{keys}"')
def check_response_keys(context, keys):
    expected_keys = [key.strip() for key in keys.split(",")]
    missing_keys = [key for key in expected_keys if key not in context.response_data]

    if missing_keys:
        raise AssertionError(f"Missing required keys in response: {missing_keys}")


@then('the "{field}" should be either "{value1}" or "{value2}"')
def check_field_value(context, field, value1, value2):
    actual_value = context.response_data.get(field)
    if actual_value not in [value1, value2]:
        raise AssertionError(
            f"Invalid {field}: {actual_value}. Expected either '{value1}' or '{value2}'"
        )


@then('the "{field}" in the response should match the requested date')
def check_date_match(context, field):
    response_date = context.response_data.get(field)
    if response_date != context.date_requested:
        raise AssertionError(
            f"Date mismatch: expected {context.date_requested}, got {response_date}"
        )
