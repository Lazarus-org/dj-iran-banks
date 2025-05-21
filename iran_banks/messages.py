"""
Language-specific messages for bank detection responses.
"""

MESSAGES = {
    'en': {
        'invalid_format': "Invalid card number format. Please enter 16 digits.",
        'unknown_bank': "Unknown bank code.",
        'checksum_failed': "Invalid card number (checksum failed).",
        'detected_bank': "Detected Bank: {}",
    },
    'fa': {
        'invalid_format': "فرمت شماره کارت نامعتبر است. لطفا ۱۶ رقم وارد کنید.",
        'unknown_bank': "کد بانک ناشناخته است.",
        'checksum_failed': "شماره کارت نامعتبر است (خطای checksum).",
        'detected_bank': "بانک شناسایی شده: {}",
    }
} 