from django.test import TestCase, Client
from django.contrib.auth.models import User
import datetime
import time
from django.utils import timezone
from accounts.forms import EntryForm
from django.contrib.auth import authenticate
from .models import *
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Functional Test to check login functionality, user search functionality, location search and view more details functionalities on the site with Selenium
class FunctionalTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\snesh\\webdriver\\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        
    def test_login(self):
        # Login form
        self.driver.get('https://sts-app.azurewebsites.net/login/')
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('admin')
        password.send_keys('stsjf2020')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)

        # Accessing the 'Users' page to view details of registered users on the application
        users_link = self.driver.find_element_by_link_text('Users')
        users_link.click()
        time.sleep(5)
        # Searching for a user using the search by username filter
        username = self.driver.find_element_by_id('id_username')
        username.send_keys('ad')
        username.send_keys(Keys.ENTER)
        time.sleep(5)

        # Accessing the 'Locations' page to view details of All location entries created on the application
        locations_link = self.driver.find_element_by_link_text('All Locations')
        locations_link.click()
        time.sleep(5)
        # Searching for a location using the search by location name filter
        locations = self.driver.find_element_by_id('id_locations')
        locations.send_keys('Mald')
        locations.send_keys(Keys.ENTER)
        time.sleep(5)

        # Accessing 'More details page' of the searched location
        more_details_link = self.driver.find_element_by_link_text('View more details')
        more_details_link.click()
        time.sleep(5)

        # Accessing the 'Audit logs' page to view a list of modifications made to the Location entries, Blacklisted users and User accounts
        audit_log_link = self.driver.find_element_by_link_text('Audit logs')
        audit_log_link.click()
        time.sleep(5)

        # Accessing the 'Admin panel' page to manage the user accounts, location entries, etc.
        admin_link = self.driver.find_element_by_link_text('Admin')
        admin_link.click()
        time.sleep(5)

        # Accessing the 'Users' page on the Admin panel to manage user accounts
        admin_users_link = self.driver.find_element_by_link_text('Users')
        admin_users_link.click()
        time.sleep(5)

        # Accessing the 'Add user' page on the Admin panel to add a user account
        add_admin_users_link = self.driver.find_element_by_class_name('addlink')
        add_admin_users_link.click()
        time.sleep(5)
        add_admin_username = self.driver.find_element_by_id('id_username')
        add_admin_username.send_keys('Alice')
        add_admin_password1 = self.driver.find_element_by_id('id_password1')
        add_admin_password1.send_keys('university@123')
        add_admin_password2 = self.driver.find_element_by_id('id_password2')
        add_admin_password2.send_keys('university@123')
        save = self.driver.find_element_by_name('_save')
        save.send_keys(Keys.RETURN)
        time.sleep(10)


# Integration Test to login as a user, search for a location, view more details of the location and download the pdf with location information
class IntegrationTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\snesh\\webdriver\\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Login form
        self.driver.get('https://sts-app.azurewebsites.net/login/')
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('admin')
        password.send_keys('stsjf2020')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)

        # Accessing the 'Locations' page to view details of All location entries created on the application
        locations_link = self.driver.find_element_by_link_text('All Locations')
        locations_link.click()
        time.sleep(5)
        # Searching for a location using the search by location name filter
        locations = self.driver.find_element_by_id('id_locations')
        locations.send_keys('Mald')
        locations.send_keys(Keys.ENTER)
        time.sleep(5)

        # Accessing 'More details page' of the searched location
        more_details_link = self.driver.find_element_by_link_text('View more details')
        more_details_link.click()
        time.sleep(5)
        download_pdf_link = self.driver.find_element_by_link_text('Generate PDF')
        download_pdf_link.click()
        time.sleep(5)



# Unit Test to check incorrect password attempts. After 3 attempts the user should get blacklisted
class PasswordLockoutTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\snesh\\webdriver\\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_blacklist(self):
        # Login form
        self.driver.get('https://sts-app.azurewebsites.net/login/')
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('Bob')
        password.send_keys('123')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('Bob')
        password.send_keys('1234')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('Bob')
        password.send_keys('123')
        submit.send_keys(Keys.RETURN)
        time.sleep(5)


# Unit test to check redirection for Admin and normal users after Login
class checkLoginTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\\Users\\snesh\\webdriver\\chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Test to check redirection to Dashboard page for Admin users after logging in
    def test_login_redirect_admin(self):
        self.driver.get('https://sts-app.azurewebsites.net/login/')
        assert 'Login' in self.driver.title
        time.sleep(2)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('admin')
        password.send_keys('stsjf2020')
        submit.send_keys(Keys.RETURN)
        assert 'STS Application' in self.driver.title
        time.sleep(5)
        logout_link = self.driver.find_element_by_link_text('Logout')
        logout_link.click()

    # Test to check redirection to Profile page for normal users after logging in
    def test_login_redirect_user(self):
        self.driver.get('https://sts-app.azurewebsites.net/login/')
        assert 'Login' in self.driver.title
        time.sleep(2)
        username = self.driver.find_element_by_name('username')
        password = self.driver.find_element_by_name('password')
        submit = self.driver.find_element_by_tag_name('button')
        # Enter credentials on the login form
        username.send_keys('user')
        password.send_keys('stsjf2020')
        submit.send_keys(Keys.RETURN)
        assert 'User Profile' in self.driver.title
        time.sleep(5)



# Unit Tests to check login functionality on the site with correct and incorrect combinations of username and password
class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_username_and_password(self):
        user = authenticate(username='wrong', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_no_username_and_wrong_password(self):
        user = authenticate(username='', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


# Unit Tests to create a user in the admin panel and login with the credentials
class TestAdminPanel(TestCase):
    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200



# Unit Tests to check whether the Location entries have been published in the past, recent time or in the future
class EntryModelTests(TestCase):

    def test_was_published_recently_with_future_entry(self):
        """
        was_published_recently() returns False for locations whose date_created
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
        was_published_recently() returns True for locations whose date_created
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_entry = Entry(date_created=time)
        self.assertIs(recent_entry.was_published_recently(), True)

# Unit Test to check whether the Dashboard view page is restricted to just logged in users
class HomeView(TestCase):
    model = Entry
    template_name ='accounts/dashboard.html'

    def test_redirect_home_if_not_logged_in(self):
        client = Client()
        response = self.client.get('https://sts-app.azurewebsites.net/')
        self.assertRedirects(response, '/login/?next=/')

# Unit Test to check whether the Locations view page is restricted to just logged in users
class LocationsView(TestCase):
    model = Entry
    template_name ='accounts/locations.html'

    def test_redirect_locations_if_not_logged_in(self):
        client = Client()
        response = self.client.get('https://sts-app.azurewebsites.net/locations/')
        self.assertRedirects(response, '/login/?next=/locations/')


# Unit Test to check whether the Audit logs view page is restricted to just logged in users
class AuditLogsView(TestCase):
    model = Entry
    template_name ='accounts/auditlogs.html'

    def test_redirect_auditlogs_if_not_logged_in(self):
        client = Client()
        response = self.client.get('https://sts-app.azurewebsites.net/auditlogs/')
        self.assertRedirects(response, '/login/?next=/auditlogs/')


# Unit Test to check whether the Audit logs view page is restricted to just logged in users
class usersView(TestCase):
    model = User
    template_name ='accounts/users.html'

    def test_redirect_users_if_not_logged_in(self):
        client = Client()
        response = self.client.get('https://sts-app.azurewebsites.net/users/')
        self.assertRedirects(response, '/login/?next=/users/')

