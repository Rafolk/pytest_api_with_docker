main_url = "http://localhost:3001"

# AuthAndHealthCheck
health_check_url = main_url + "/ping"
auth_token_url = main_url + "/auth"

# GetAndCreateBooking
get_or_create_booking_url = main_url + "/booking"
get_or_update_and_delete_booking_url = main_url + "/booking/"

# DemoTestDatabase
database_connection = "dbname=MB4 user=postgres password=mysecretpassword host=localhost port=6532"