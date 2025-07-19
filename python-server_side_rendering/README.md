# 0x00. Server-side rendering

This project focuses on understanding and implementing server-side rendering (SSR) using Python and Flask. It covers concepts like templating with Jinja2, handling dynamic content, and integrating data from various sources such as JSON, CSV, and SQLite databases.

## Task 0: Creating a Simple Templating Program

This task involves creating a Python function `generate_invitations` that generates personalized invitation files from a template and a list of attendee objects. It also includes robust error handling for various edge cases.

### How to Use

1.  **Save the template:** Create a file named `template.txt` with the following content:

    ```
    Hello {name},

    You are invited to the {event_title} on {event_date} at {event_location}.

    We look forward to your presence.

    Best regards,
    Event Team
    ```

2.  **Save the Python script:** Create a file named `task_00_intro.py` with the `generate_invitations` function.

3.  **Run the main script:** Create a `main.py` file to test the function:

    ```python
    # Main file content
    from task_00_intro import generate_invitations

    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)
    ```

    Execute `python3 main.py` in the same directory.

### Error Handling

The `generate_invitations` function handles the following error conditions:

-   **Invalid Input Types:** Checks if `template` is a string and `attendees` is a list of dictionaries. Logs an error and terminates if types are incorrect.
-   **Empty Template:** Logs an error message and terminates if the template string is empty.
-   **Empty List of Objects:** Logs an error message and terminates if the `attendees` list is empty.
-   **Missing Data in Object:** Replaces missing data for placeholders with "N/A" in the output file.

### Output

Upon successful execution, the script will generate `output_X.txt` files (e.g., `output_1.txt`, `output_2.txt`), each containing a personalized invitation.
