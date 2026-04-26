import sys
from database import (
    init_db, 
    add_contact, 
    get_all_contacts, 
    update_contact, 
    delete_contact,
    get_contact
)

def display_menu():
    """Prints the main menu options to the terminal."""
    print("\n--- Cortado Group Networking Tracker ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Exit")
    print("----------------------------------------")

def main():
    """Main application loop."""
    # Ensure the database and tables exist before doing anything else
    init_db()
    
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            print("\n-- Add New Contact --")
            name = input("Name: ")
            company = input("Company (e.g., Cortado Group): ")
            role = input("Role: ")
            email = input("Email: ")
            notes = input("Notes/Context: ")
            
            add_contact(name, company, role, email, notes)
            print(f"\n✅ Successfully added {name} to your network!")

        elif choice == '2':
            print("\n-- Your Network --")
            contacts = get_all_contacts()
            if not contacts:
                print("Your network is currently empty. Go meet some people!")
            else:
                for contact in contacts:
                    # contact is a tuple: (id, name, company, role, email, notes)
                    print(f"[{contact[0]}] {contact[1]} - {contact[3]} at {contact[2]}")
                    print(f"    Email: {contact[4]} | Notes: {contact[5]}")

        elif choice == '3':
            print("\n-- Update Contact --")
            try:
                contact_id = int(input("Enter the ID of the contact to update: "))
                
                # Fetch the existing contact data
                current_contact = get_contact(contact_id)
                
                if not current_contact:
                    print(f"\n❌ Error: No contact found with ID {contact_id}.")
                    continue  # Skips the rest of the loop and shows the menu again
                
                # Unpack the tuple into variables
                c_name, c_company, c_role, c_email, c_notes = current_contact

                print("\nEnter new details. (Leave blank and press Enter to keep current value)")
                
                # The 'or' operator is the magic here. If input() is "", it uses the variable on the right.
                name = input(f"New Name [{c_name}]: ") or c_name
                company = input(f"New Company [{c_company}]: ") or c_company
                role = input(f"New Role [{c_role}]: ") or c_role
                email = input(f"New Email [{c_email}]: ") or c_email
                notes = input(f"New Notes [{c_notes}]: ") or c_notes
                
                update_contact(contact_id, name, company, role, email, notes)
                print(f"\n✅ Contact ID {contact_id} updated successfully.")
            except ValueError:
                print("\n❌ Error: Please enter a valid numerical ID.")

        elif choice == '4':
            print("\n-- Delete Contact --")
            try:
                contact_id = int(input("Enter the ID of the contact to delete: "))
                # Add a simple confirmation
                confirm = input(f"Are you sure you want to delete ID {contact_id}? (y/n): ").lower()
                if confirm == 'y':
                    delete_contact(contact_id)
                    print(f"\n✅ Contact ID {contact_id} deleted.")
                else:
                    print("\nDeletion cancelled.")
            except ValueError:
                print("\n❌ Error: Please enter a valid numerical ID.")

        elif choice == '5':
            print("\nExiting Networking Tracker. Good luck with your internship!")
            sys.exit(0)

        else:
            print("\n❌ Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()