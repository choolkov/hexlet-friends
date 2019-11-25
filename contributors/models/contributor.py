from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from contributors.models.base import NAME_LENGTH, CommonFields


class Contributor(CommonFields):
    """Model representing a contributor."""

    login = models.CharField(_('Login'), max_length=NAME_LENGTH)
    avatar_url = models.URLField(_('avatar url'))

    class Meta(object):
        verbose_name = _('Contributor')
        verbose_name_plural = _('Contributors')

    def __str__(self):
        """Represents an instance as a string."""
        return self.login

    def get_absolute_url(self):
        """Returns the url of an instance."""
        return reverse('contributors:contributor_details', args=[self.pk])