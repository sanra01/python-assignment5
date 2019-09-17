"""The output module, containing the Output class."""

class Output:
    """The Output class, containing functions related to terminal output."""

    @classmethod
    def print_bold(cls, text):
        """Print text in bold."""
        start = "\033[1m"
        end = "\033[0;0m"
        print(f"{start}{text}{end}")

    @classmethod
    def print_error(cls, text):
        """Print text in red and bold."""
        start = "\033[31;1m"
        end = "\033[0;0m"
        print(f"{start}{text}{end}")
