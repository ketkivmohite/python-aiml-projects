Day 3: Python Contact Book
A command-line application for managing contacts, built to learn how to handle structured data in Python. This version can now save and load contacts, so your data is remembered between sessions.

Contacts are stored in a contacts.json file in a human-readable format.

Features
Add new contacts (name, phone, email).

View all contacts in a formatted list.

Data Persistence: Contacts are automatically saved to contacts.json and reloaded when the app starts.

 Concepts Learned
Dictionaries & Lists: For storing structured contact data.

File I/O with JSON: Learned to use the json library to dump (save) and load (read) complex data like lists of dictionaries. This is a crucial skill for working with APIs and configuration files.

Error Handling (try...except): Used to gracefully handle the case where the contacts.json file doesn't exist on the first run.