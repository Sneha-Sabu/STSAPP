from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Entry
# Create your tests here.

class EntryModelTests(TestCase):

    def test_was_published_recently_with_future_entry(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_entry = Entry(date_created=time)
        self.assertIs(future_entry.was_published_recently(), False)

def test_was_published_recently_with_old_entry(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_entry = Entry(date_created=time)
    self.assertIs(old_entry.was_published_recently(), False)

def test_was_published_recently_with_recent_entry(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_entry = Entry(date_created=time)
    self.assertIs(recent_entry.was_published_recently(), True)