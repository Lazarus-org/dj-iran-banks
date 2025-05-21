from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Bank(models.Model):
    """Model for storing bank information."""
    code = models.CharField(
        max_length=6,
        unique=True,
        help_text=_("Bank identification number (BIN)"),
        verbose_name=_("Bank Code"),
        db_comment="The 6-digit BIN (Bank Identification Number) used in card numbers"
    )
    name = models.CharField(
        max_length=100,
        help_text=_("Name of the bank in Persian"),
        verbose_name=_("Bank Name"),
        db_comment="The official name of the bank in Persian script"
    )
    active = models.BooleanField(
        default=True,
        help_text=_("Whether this bank is currently active in the banking system"),
        verbose_name=_("Active Status"),
        db_comment="Indicates if the bank is currently active in the Iranian banking system"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation Date"),
        db_comment="Timestamp when this bank record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Last Update"),
        db_comment="Timestamp when this bank record was last updated"
    )

    class Meta:
        verbose_name = _("Bank")
        verbose_name_plural = _("Banks")
        ordering = ['name']
        db_table = 'iran_banks'
        db_table_comment = "Stores information about Iranian banks and their identification codes"
        indexes = [
            models.Index(fields=['code'], name='bank_code_idx'),
            models.Index(fields=['name'], name='bank_name_idx'),
            models.Index(fields=['active', 'code'], name='bank_active_code_idx'),
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_card_prefix(self) -> str:
        """Returns the card number prefix for this bank."""
        return self.code

    def is_active_bank(self) -> bool:
        """Returns whether this bank is currently active."""
        return self.active
