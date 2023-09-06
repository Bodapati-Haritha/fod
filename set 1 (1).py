# Create a dictionary to store the frequency of each weather condition
weather_data = {
    "Sunny": 50,       # Replace with your actual data
    "Rainy": 30,
    "Cloudy": 20,
    "Snowy": 5,
    # Add more weather conditions and their frequencies as needed
}

# Initialize variables to keep track of the most common weather type and its frequency
most_common_weather = ""
max_frequency = 0

# Iterate through the weather data and find the most common weather type
for condition, frequency in weather_data.items():
    if frequency > max_frequency:
        most_common_weather = condition
        max_frequency = frequency

# Print the results
print("Frequency distribution of weather conditions:")
for condition, frequency in weather_data.items():
    print(f"{condition}: {frequency} times")

print(f"The most common weather type is: {most_common_weather} ({max_frequency} times)")
