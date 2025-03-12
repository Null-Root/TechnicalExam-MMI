from datetime import datetime


"""
ValidatedInput

This is used for input validation.
This is inherited by UserInterface.
"""
class ValidatedInput:
    @staticmethod
    def get_string(prompt: str, default: str = "") -> str:
        value = input(f"{prompt} (Press enter to keep default: {default}): ").strip()
        return value if value else default

    @staticmethod
    def get_date(prompt: str, default: str = None) -> str:
        if default is None:
            default = datetime.now().strftime("%Y-%m-%d")  # Default to today's date
        while True:
            date_str = input(f"{prompt} (Press enter to keep default: {default}): ").strip()
            if not date_str:
                return default  # Use default if no input
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Validate format
                return date_obj.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")

    @staticmethod
    def get_selected_item(prompt: str, options: list, default) -> str:
        option_map = {str(i + 1): option for i, option in enumerate(options)}

        for num, item in option_map.items():
            print(f"{num}. {item}")

        while True:
            value = input(f"{prompt} (Press enter to keep default: {default}): ").strip().lower()
            if not value:
                return default  # Use default if no input
            if value in option_map:
                return option_map[value]
            if value in options:
                return value
            print("Invalid selection. Please enter a valid number or value.")
