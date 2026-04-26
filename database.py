import logging
import sqlite3

logger = logging.getLogger(__name__)
DB_NAME = "records.db"

def init_db() -> None:
    """Create the database and contacts table if needed."""
    logger.info("Initializing database")
    conn = sqlite3.connect(DB_NAME)
    # Updated table structure for a networking tracker
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            company TEXT,
            role TEXT,
            email TEXT,
            notes TEXT
        )
        """
    )
    conn.commit()
    conn.close()
    logger.info("Database setup complete")

def add_contact(name: str, company: str, role: str, email: str, notes: str) -> None:
    """CREATE: Add a new contact to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, company, role, email, notes) VALUES (?, ?, ?, ?, ?)",
        (name, company, role, email, notes)
    )
    conn.commit()
    conn.close()
    logger.info(f"Added new contact: {name}")

def get_all_contacts() -> list:
    """READ: Retrieve all contacts from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, company, role, email, notes FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_contact(contact_id: int, name: str, company: str, role: str, email: str, notes: str) -> None:
    """UPDATE: Modify an existing contact's details."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # The WHERE clause is critical here; without it, you would update every row in the table!
    cursor.execute(
        """
        UPDATE contacts 
        SET name = ?, company = ?, role = ?, email = ?, notes = ?
        WHERE id = ?
        """,
        (name, company, role, email, notes, contact_id)
    )
    conn.commit()
    conn.close()
    logger.info(f"Updated contact ID {contact_id}")

def delete_contact(contact_id: int) -> None:
    """DELETE: Remove a contact from the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
    logger.info(f"Deleted contact ID {contact_id}")

def get_contact(contact_id: int) -> tuple:
    """READ: Retrieve a single contact by ID to help with updates."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Notice we only select the fields we need to update, not the ID
    cursor.execute("SELECT name, company, role, email, notes FROM contacts WHERE id = ?", (contact_id,))
    row = cursor.fetchone()
    conn.close()
    return row