import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# print("This script is for taking out info about any phone number
# print("Be sure to have country code or else it'll take 44(Canada) as Country Code
# Also carrier name may not be able to fetch due to some restrictions

number = input("Enter the phone number with country code: ")

my_number = phonenumbers.parse(number, "GB")
print(my_number)
print("Number is Valid: ", phonenumbers.is_valid_number(my_number))
print("Carrier name of number:", carrier.name_for_number(my_number, "en"))
print("Timezone of the number:", timezone.time_zones_for_number(my_number))
print("Geo-location of the number:", geocoder.description_for_number(my_number, 'en'))
