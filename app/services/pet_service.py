# app/services/pet_service.py


# --------------------------------------------------
# 1. Import Repository Layer functions
# --------------------------------------------------


# IMPORT STATEMENT:
# Import functions from pet_repository.py.
#
# get_all_pets
# → FUNCTION in the Repository Layer
#
# get_pet_by_id
# → FUNCTION in the Repository Layer
#
# add_pet
# → FUNCTION in the Repository Layer
#
# update_pet
# → FUNCTION in the Repository Layer
from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
)


# --------------------------------------------------
# 2. Get all pets through the Service Layer
# --------------------------------------------------


# FUNCTION DEFINITION:
# list_pets() is a Service Layer function.
def list_pets():


    # FUNCTION CALL:
    # Call get_all_pets() in the Repository Layer.
    #
    # pets
    # → VARIABLE
    # → stores all pet rows returned from MariaDB
    pets = get_all_pets()


    # RETURN STATEMENT:
    # Return all pets to the caller.
    return pets


# --------------------------------------------------
# 3. Get one pet through the Service Layer
# --------------------------------------------------


# FUNCTION DEFINITION:
# get_pet() is a Service Layer function.
#
# pet_id
# → PARAMETER
# → identifies which pet we want
def get_pet(pet_id):


    # FUNCTION CALL:
    # Call get_pet_by_id() in the Repository Layer.
    #
    # pet_id
    # → ARGUMENT
    #
    # pet
    # → VARIABLE
    # → stores one pet row returned from MariaDB
    pet = get_pet_by_id(pet_id)


    # RETURN STATEMENT:
    # Return the pet to the caller.
    return pet


# --------------------------------------------------
# 4. Add a pet through the Service Layer
# --------------------------------------------------


# FUNCTION DEFINITION:
# create_pet() is a Service Layer function.
#
# name, pet_type, breed, age, owner_name
# → PARAMETERS
def create_pet(
    name,
    pet_type,
    breed,
    age,
    owner_name,
):


    # FUNCTION CALL:
    # Call add_pet() in the Repository Layer.
    #
    # new_pet_id
    # → VARIABLE
    # → stores the ID of the newly created pet
    new_pet_id = add_pet(
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )


    # RETURN STATEMENT:
    # Return the new pet ID.
    return new_pet_id


# --------------------------------------------------
# 5. Update a pet through the Service Layer
# --------------------------------------------------




# FUNCTION DEFINITION:
# update_pet_service() is a Service Layer function.
#
# pet_id, name, pet_type, breed, age, owner_name
# → PARAMETERS
def update_pet_service(
    pet_id,
    name,
    pet_type,
    breed,
    age,
    owner_name,
):


    # FUNCTION CALL:
    # Call update_pet() in the Repository Layer.
    #
    # rows_updated
    # → VARIABLE
    # → stores how many rows were updated
    rows_updated = update_pet(
        pet_id,
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )


    # RETURN STATEMENT:
    # Return the number of rows updated.
    return rows_updated
