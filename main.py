# main.py


# --------------------------------------------------
# 1. Import Service Layer function
# --------------------------------------------------


# IMPORT STATEMENT:
# Import update_pet_service() from pet_service.py.
from app.services.pet_service import update_pet_service


# --------------------------------------------------
# 2. Main function
# --------------------------------------------------


# FUNCTION DEFINITION:
def main():


    print("🐾 Happy Paws Pet Hotel")
    print("------------------------")


    # FUNCTION CALL:
    # Ask the Service Layer to update pet ID 1.
    #
    # rows_updated
    # → VARIABLE
    # → stores the value returned by the Service Layer
    rows_updated = update_pet_service(
        1,
        "maew",
        "Cat",
        "Thai",
        400,
        "Dang",
    )


    # FUNCTION CALL:
    # Display how many rows were updated.
    print(f"Rows updated: {rows_updated}")


# --------------------------------------------------
# 3. Run the program
# --------------------------------------------------


if __name__ == "__main__":
    main()
