def get_positive_int(prompt, min_val, max_val, msg=""):
    """Read an integer within given bounds."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"{msg} Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_positive_float(prompt, min_val, max_val, msg=""):
    """Read a float within given bounds."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"{msg} Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Weather-Based Harvest Advisory System")
    print("-" * 50)

    # Number of days (3–7)
    n_days = get_positive_int(
        "Enter number of days (3–7): ",
        3, 7,
        "N must be between 3 and 7."
    )

    rainfalls = []
    humidities = []

    print(f"\nEnter data for {n_days} days:")
    for i in range(n_days):
        day = i + 1

        rainfall = get_positive_float(
            f"Rainfall on day {day} (0–50 mm): ",
            0.0, 50.0,
            "Rainfall must be between 0 and 50 mm."
        )
        humidity = get_positive_float(
            f"Humidity on day {day} (0–100 %): ",
            0.0, 100.0,
            "Humidity must be between 0 and 100 %."
        )

        rainfalls.append(rainfall)
        humidities.append(humidity)

    # Compute averages
    avg_rainfall = sum(rainfalls) / len(rainfalls)
    avg_humidity = sum(humidities) / len(humidities)

    # Decide advice (based on average trends)
    # Tune these thresholds as needed by your instructor
    if avg_rainfall < 5 and avg_humidity < 70:
        advisory = "Harvest Now"
    else:
        advisory = "Delay Harvest"

    # Display output
    print("\nOutput:")
    print(f"Average Rainfall (last {n_days} days): {avg_rainfall:.1f} mm")
    print(f"Average Humidity (last {n_days} days): {avg_humidity:.1f} %")
    print(f"Harvest Advisory: {advisory}")

if __name__ == "__main__":
    main()
