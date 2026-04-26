# Networking Tracker (CRUD Application)
Author: Colin Meersman

Purpose: A modular, command-line interface (CLI) application built in Python to manage professional networking contacts. This tool uses a local SQLite database to persist data, allowing users to track names, companies, roles, emails, and contextual notes from professional encounters. 

## Project Architecture
To ensure clean, maintainable, and reusable code, this project is divided into two distinct modules:
* `database.py`: Handles all SQLite database connections and executes the core CRUD (Create, Read, Update, Delete) SQL queries.
* `main.py`: Drives the user interface, processing command-line inputs and routing them to the appropriate database functions.

## Features
* **Create:** Add new contacts with detailed fields (Name, Company, Role, Email, Notes).
* **Read:** View a formatted list of all saved contacts and their unique database IDs.
* **Update:** Modify existing contact profiles. Features intelligent input handling that preserves existing data if a field is intentionally left blank during an update.
* **Delete:** Permanently remove a contact from the database via their unique ID.

## Setup and Installation

1. **Prerequisites:** Ensure you have Python 3 installed on your system. SQLite3 is included in the standard Python library, so no external database installation is required.
2. **Clone the Repository:**
   ```bash
   git clone <https://github.com/colinmeersman-uga/CRUD_Project.git>
   cd <CRUD_Project>

Initialize the Application:
1. Run the main script.
2. The application will automatically generate the records.db SQLite file and build the necessary tables on its first run.
3. In Bash run python main.py


Usage
Upon running main.py, you will be presented with an interactive menu:

--- Networking Tracker ---
1. Add a new contact
2. View all contacts
3. Update a contact
4. Delete a contact
5. Exit
--------------------------

Type the number corresponding to your desired action and follow the on-screen prompts. Note: When updating or deleting, always refer to the database ID number displayed inside the brackets [ ] next to the contact's name.

## Development Process & Git Workflow

This project was developed using a standard Git feature-branch workflow to maintain a clean commit history:

Created an isolated branch (setup-database-schema) to build the initial SQLite architecture.

Committed modular updates (e.g., separating SQL execution from UI logic).

Merged features back into main after verifying functionality.

## Challenges & Learnings
Building this application presented several learning opportunities regarding command-line environments and relational databases:

Terminal vs. Editor Context: Encountered syntax errors (e.g., bash: return: rows: numeric argument required) when accidentally pasting Python code directly into the Bash terminal instead of the script file.

The "Blank Update" Overwrite Bug: Initially, when updating a contact, pressing "Enter" to skip a field captured an empty string (""), which overwrote the existing database data. This was solved by implementing a get_contact() read function and using Python's or operator to gracefully fall back to the existing data if the user input was blank.

Database Primary Keys vs. Indexing: Discovered that deleting a record (e.g., ID 1 or 2) permanently retires that ID due to SQLite's AUTOINCREMENT behavior. This was an important lesson in relational database integrity—Primary Keys are permanent identifiers tied to the data, not just standard list row numbers.

Git Directory Navigation: Overcame fatal: pathspec did not match any files errors by learning to use ls and cd to ensure the terminal was pointing to the correct root directory before staging and committing files.

