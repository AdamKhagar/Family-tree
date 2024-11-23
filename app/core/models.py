from django.db import models
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    """Gender"""

    MALE = 'male', _('Male')
    FEMALE = 'female', _('Female')


class Human(models.Model):
    """Human model"""

    first_name = models.CharField(_('First name'), max_length=255)
    last_name = models.CharField(_('Last name'), max_length=255)
    gender = models.CharField(
        _('Gender'), max_length=6, choices=Gender.choices,
    )
    father = models.ForeignKey(
        'self',
        verbose_name=_('Father'),
        related_name='fathers_children',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'gender': Gender.MALE},
    )
    mother = models.ForeignKey(
        'self',
        verbose_name=_('Mother'),
        related_name='mothers_children',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'gender': Gender.FEMALE},
    )

    def __str__(self) -> str:
        return f'#{self.pk} {self.first_name} {self.last_name}'

    @property
    def children(self) -> models.QuerySet:
        return (
            self.fathers_children.all()
            if self.gender == Gender.MALE
            else self.mothers_children.all()
        )