main_url = "http://localhost:3001"

# AuthAndHealthCheck
health_check_url = main_url + "/ping"
auth_token_url = main_url + "/auth"

# GetAndCreateBooking
get_all_ids_or_create_booking_url = main_url + "/booking"
get_or_update_and_delete_booking_url = main_url + "/booking/"

# DemoTestDatabase
database_connection = "dbname=postgres user=postgres password=mysecretpassword host=localhost port=6432"
