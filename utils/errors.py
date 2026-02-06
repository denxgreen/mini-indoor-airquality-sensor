ERROR_CODES = {
    501: {'message': 'SettingsError: Configuration is invalid.', 'blinks_number': 1},
    502: {'message': 'DiagnosticsError: One of the sensors is corrupted.', 'blinks_number': 2},
    110: {'message': 'SensorError: One of the sensors is not functional.', 'blinks_number': 3}
}

class DeviceError(Exception):
    ...

class SettingsError(DeviceError):
    errno = 501

    def __init__(self, message=ERROR_CODES[errno]['message']) -> None:
        super().__init__(message)

class DiagnosticsError(DeviceError):
    errno = 502

    def __init__(self, message=ERROR_CODES[errno]['message']) -> None:
        super().__init__(message)