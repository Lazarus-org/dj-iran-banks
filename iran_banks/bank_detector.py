"""
Bank card detection and validation functionality for Iranian banks.
"""
from typing import Dict, Optional, Tuple
from django.utils.translation import get_language
from .messages import MESSAGES

class BankDetector:
    # Dictionary mapping bank BIN codes to bank names
    BANKS: Dict[str, str] = {
        '603799': 'بانک ملی',
        '603770': 'بانک صادرات',
        '603769': 'بانک کشاورزی',
        '589210': 'بانک سپه',
        '610433': 'بانک ملت',
        '628023': 'بانک مسکن',
        '627648': 'بانک توسعه صادرات',
        '627961': 'بانک صنعت و معدن',
        '627353': 'بانک تجارت',
        '589463': 'بانک رفاه',
        '639347': 'بانک پاسارگاد',
        '627412': 'بانک اقتصاد نوین',
        '622106': 'بانک پارسیان',
        '627488': 'بانک کارآفرین',
        '621986': 'بانک سامان',
        '639346': 'بانک سینا',
        '639607': 'بانک سرمایه',
        '502806': 'بانک شهر',
        '502938': 'بانک دی',
        '627381': 'بانک انصار',
        '639599': 'بانک قوامین',
    }

    @classmethod
    def get_message(cls, key: str, *args) -> str:
        """Get the appropriate message based on current language setting."""
        current_lang = get_language() or 'en'
        # Default to English if language not supported
        lang_messages = MESSAGES.get(current_lang, MESSAGES['en'])
        message = lang_messages.get(key, MESSAGES['en'][key])
        if args:
            return message.format(*args)
        return message

    @classmethod
    def detect_bank(cls, card_number: str) -> Tuple[bool, str, Optional[str]]:
        """
        Detect the bank from a card number.
        
        Args:
            card_number: The card number to check
            
        Returns:
            Tuple containing:
            - bool: Whether the card number is valid
            - str: Error message if invalid, or bank name if valid
            - Optional[str]: Bank code if valid, None if invalid
        """
        # Clean the input
        card_number = cls.clean_card_number(card_number)
        
        # Validate the card number format
        if not cls.is_valid_format(card_number):
            return False, cls.get_message('invalid_format'), None

        # Get the BIN (first 6 digits)
        bin_code = card_number[:6]
        
        # Check if it's a valid bank
        bank_name = cls.BANKS.get(bin_code)
        if not bank_name:
            return False, cls.get_message('unknown_bank'), None
            
        # Validate the checksum
        if not cls.validate_card_checksum(card_number):
            return False, cls.get_message('checksum_failed'), None
            
        return True, cls.get_message('detected_bank', bank_name), bin_code

    @staticmethod
    def clean_card_number(card_number: str) -> str:
        """Remove any spaces or special characters from the card number."""
        return ''.join(c for c in card_number if c.isdigit())

    @staticmethod
    def is_valid_format(card_number: str) -> bool:
        """Check if the card number has the correct format (16 digits)."""
        return len(card_number) == 16 and card_number.isdigit()

    @staticmethod
    def validate_card_checksum(card_number: str) -> bool:
        """
        Validate card number using the Luhn algorithm.
        """
        if not card_number.isdigit():
            return False
            
        digits = [int(d) for d in card_number]
        checksum = 0
        
        for i in range(len(digits)-1, -1, -1):
            d = digits[i]
            if i % 2 == len(digits) % 2:  # Alternate digits
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d
            
        return checksum % 10 == 0

    @classmethod
    def get_all_banks(cls) -> Dict[str, str]:
        """Return all supported banks and their codes."""
        return cls.BANKS.copy() 