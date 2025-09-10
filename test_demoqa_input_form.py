from pages.registration_page import RegistrationPage
from users import User


def test_form_submission():
    registration_page = RegistrationPage()
    alisha = User(first_name='Alisha',
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
    registration_page.register(alisha)
    registration_page.should_have_registered(alisha)
    print('Success')