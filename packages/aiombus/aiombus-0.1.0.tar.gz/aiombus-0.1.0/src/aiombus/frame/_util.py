"""Helper functions."""


def calculate_checksum(body):
    """Calculate checksum of the message body."""
    return sum([int(byte) for byte in body]) % 256
