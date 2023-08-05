import errno
import os
import re
import socket
import sys
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.servers.basehttp import WSGIServer, get_internal_wsgi_application, run
from django.utils import autoreload
from django.utils.regex_helper import _lazy_re_compile

naiveip_re = _lazy_re_compile(
    r"""^(?:
(?P<addr>
    (?P<ipv4>\d{1,3}(?:\.\d{1,3}){3}) |         # IPv4 address
    (?P<ipv6>\[[a-fA-F0-9:]+\]) |               # IPv6 address
    (?P<fqdn>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*) # FQDN
):)?(?P<port>\d+)$""",
    re.X,
)

from celery.bin import worker, celery


class Command(BaseCommand):
    help = "Starts a lightweight web server for development."

    # def execute(self, *args, **options):
    #     if options["no_color"]:
    #         # We rely on the environment because it's currently the only
    #         # way to reach WSGIRequestHandler. This seems an acceptable
    #         # compromise considering `runserver` runs indefinitely.
    #         os.environ["DJANGO_COLORS"] = "nocolor"
    #     super().execute(*args, **options)

    # def get_handler(self, *args, **options):
    #     """Return the default WSGI handler for the runner."""
    #     return get_internal_wsgi_application()

    def add_arguments(self, parser):
        parser.add_argument(
            "--noreload",
            action="store_false",
            dest="use_reloader",
            help="Tells Django to NOT use the auto-reloader.",
        )

    def handle(self, *args, **options):
        self.run(**options)

    def run(self, **options):
        """Run the server, using the autoreloader if needed."""
        if options["use_reloader"]:
            autoreload.run_with_reloader(self.inner_run, *sys.argv[2:], **options)
        else:
            self.inner_run(None, *sys.argv[2:], **options)

    def inner_run(self, *args, **options):
        sys.argv = [
            'celery',
            '-A',
            getattr(settings, 'CELERY_APPLICATION', ''),
            'worker',
            '-l', 'DEBUG',
            *args
        ]

        celery.main()