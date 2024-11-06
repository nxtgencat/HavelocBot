from supabase import create_client

from config import load_config

# Load environment variables from .env file
_, supabase_url, supabase_key = load_config()

# Initialize the Supabase client
supabase = create_client(supabase_url, supabase_key)


def register_user(chat_id, reg_number):
    """Register or update the registration number for the given chat_id (only one reg_number per user)."""
    # Check if the user already has a registration number
    response = supabase.table('users').select('reg_number').eq('chat_id', chat_id).execute()

    if response.data:
        # If the user already has a registration number, do not allow updating
        return False  # User already has a reg_number
    else:
        # If the user doesn't exist, create a new entry
        data = {
            'chat_id': chat_id,
            'reg_number': reg_number,
            'shortlisted_companies': ""  # Assuming no companies shortlisted initially
        }
        response = supabase.table('users').insert(data).execute()

        # Check if the insert was successful by checking if data is returned
        if response.data:
            return True  # New registration successful
        else:
            return False  # Registration failed


def get_user_data(chat_id):
    """Retrieve user data based on chat_id."""
    response = supabase.table('users').select('reg_number', 'shortlisted_companies').eq('chat_id', chat_id).execute()
    return response.data[0] if response.data else None


def delete_user_data(chat_id):
    """Delete the user data for the given chat_id."""
    # Perform the delete operation
    response = supabase.table('users').delete().eq('chat_id', chat_id).execute()

    # Check if the deletion was successful based on response data
    if response.data:  # If response contains data, deletion was successful
        return True
    else:
        print("Error: Unable to delete data. Response data is empty.")
        return False


def get_shortlisted_companies(chat_id):
    # Query the users table for the chat_id to get reg_number and shortlisted_companies
    response = supabase.table("users").select("reg_number, shortlisted_companies").eq("chat_id", chat_id).execute()

    # Check if data is returned and access response data correctly
    if response.data:
        # Extract reg_number and shortlisted_companies
        reg_number = response.data[0].get("reg_number")
        shortlisted_companies = response.data[0].get("shortlisted_companies")

        # If the field is EMPTY, return an appropriate message
        if shortlisted_companies == "":
            return f"No companies shortlisted for registration number {reg_number}."

        # Otherwise, split the companies by comma and return them
        companies_list = shortlisted_companies.split(",") if shortlisted_companies else []
        return f"Shortlisted companies for {reg_number}: {', '.join(companies_list)}"
    else:
        return f"Error: Unable to retrieve data for registration number associated with chat ID {chat_id}"


def get_all_registered_numbers():
    """Retrieve all registered numbers from the users table."""
    response = supabase.table('users').select('reg_number').execute()
    return [reg['reg_number'] for reg in response.data] if response.data else []
