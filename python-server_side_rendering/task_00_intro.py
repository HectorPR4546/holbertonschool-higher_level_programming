
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees):
        output_filename = f"output_{i+1}.txt"
        
        processed_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
