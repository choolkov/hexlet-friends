from django.utils.translation import gettext_lazy as _
from django.views import generic

from contributors.models import Contributor, Repository
from contributors.views.mixins import TableSortSearchAndPaginationMixin


class ListView(TableSortSearchAndPaginationMixin, generic.ListView):
    """A list of pull requests of a contributor."""

    template_name = 'contributor_settings.html'
    sortable_fields = (  # noqa: WPS317
        'name',
        'organization',
        'project',
        'pull_requests',
        'issues',
        ('contributors_count', _("Contributors")),
    )
    searchable_fields = ('name', 'organization__name', 'project__name')
    ordering = sortable_fields[0]

    def get_queryset(self):  # noqa: WPS615
        """Get user repositories.

        Returns:
            Queryset.
        """
        self.queryset = Repository.objects.select_related(
            'organization').filter(
            owner=Contributor.objects.get(user=self.request.user),
        )
        """Add to context contributor hidded repositories."""
        return super().get_queryset()
