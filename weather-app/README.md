Live Weather App
A command-line application built with Python that fetches and displays real-time weather data from a live API on the internet. The user can enter any city name, and the application will return the current weather conditions for that location.

This project marks a significant step from working with local data to interacting with external web services, a fundamental skill in modern software and data science.

Features
Live Data: Connects to the wttr.in public API to get up-to-the-minute weather information.

User-Friendly Interface: Prompts the user for a city and displays the weather data in a clean, readable format.

Dynamic API Requests: Uses f-strings to dynamically build the API URL based on the user's input.

Robust Error Handling: Implements try-except blocks to gracefully handle common issues like invalid city names, network connection problems, or unexpected data formats, preventing the application from crashing.

Key Concepts Learned
API Integration: Mastered the use of the requests library to make HTTP GET requests to an external API and retrieve data.

JSON Data Handling: Learned to parse JSON data returned from an API into a Python dictionary, making it easy to access and use specific pieces of information.
--   Exception Handling: Implemented robust try-except blocks to manage different types of potential errors (HTTPError, RequestException), a crucial skill for building reliable applications that depend on external services.

External Libraries: Gained more experience with pip to install and use third-party packages (requests), expanding the capabilities of standard Python.