# Discord Reminder Bot

This Python script allows you to set reminders on Discord using a webhook. You can input a reminder and a timer, and the script will send the reminder message to a Discord channel after the specified time.

## Installation

1. Clone the repository to your local machine:

2. Navigate to the project directory:

    ```bash
    cd discord-reminder-bot
    ```

3. Install the required dependencies. You can use `pip` to install the `requests` module:

    ```bash
    pip install requests
    ```

## Usage

1. Run the script:

    ```bash
    python reminder_bot.py
    ```

2. Enter your reminder message when prompted.

3. Enter the timer duration in the format `<number> <unit>` (e.g., `5 seconds`, `10 minutes`).

4. The script will wait for the specified duration and then send the reminder message to the Discord channel configured in the script.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
