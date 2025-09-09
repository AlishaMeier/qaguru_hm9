from pages.registration_page import RegistrationPage

def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Alisha')
        .fill_last_name('Meier')
        .fill_email('alisha.meyer@gmail.com')
        .set_gender("Female")
        .fill_phone_number('7078083333')
        .fill_birthday('November', '1995', '03')
        .set_subject_by_enter('Computer Science')
        .set_hobby("Music")
        .upload_picture('test_check.txt')
        .fill_current_address('ул.Назарбаева, 69')
        .choose_location('NCR', 'Delhi')
        .submit_form()
    )

    registration_page.should_have_registered_user_with(
            'Alisha Meier',
            'alisha.meyer@gmail.com',
            'Female',
            '7078083333',
            '03 November,1995',
            'Computer Science',
            'Music',
            'test_check.txt',
            'ул.Назарбаева, 69',
            'NCR Delhi'
                                                 )
    print('Success')
