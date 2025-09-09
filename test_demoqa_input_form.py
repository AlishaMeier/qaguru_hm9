from pages.registration_page import RegistrationPage
from users import User


def test_form_submission():
    registration_page = RegistrationPage()
    alex = User(first_name='Alisha',
                 last_name='Meier',
                 email='alisha.meyerr@gmail.com',
                 gender="Female",
                 phone_number='7078083369',
                 birthday=('November', '1995', '03'),
                 first_subject='Computer Science',
                 hobby="Music",
                 file_name='test.txt',
                 address='Almaty',
                 user_location=('NCR', 'Delhi')
                 )

    registration_page.open()
    registration_page.register(alex)
    registration_page.should_have_registered(alex)
    print('Success')