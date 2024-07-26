
class ValueVD:
    @staticmethod
    def time_out() -> int:
        return 15
    
    @staticmethod
    def time_out_milli_seconds() -> int:
        return 15000

    @staticmethod
    def bold(message: str) -> str:
        return f"\033[1m{message}\033[0m"

    @staticmethod
    def color_red(message: str) -> str:
        return f"\033[91m{message}\033[0m"

    @staticmethod
    def color_blue(message: str) -> str:
        return f"\033[94m{message}\033[0m"

    @staticmethod
    def color_yellow(message: str) -> str:
        return f"\033[93m{message}\033[0m"

    @staticmethod
    def color_green(message: str) -> str:
        return f"\033[92m{message}\033[0m"

    @staticmethod
    def color_cyan(message: str) -> str:
        return f"\033[96m{message}\033[0m"

    @staticmethod
    def color_magenta(message: str) -> str:
        return f"\033[95m{message}\033[0m"

    @staticmethod
    def test_result_d_t_format() -> str:
        return "%d/%m/%y %H:%M:%S"

