from selene.support.shared import browser
from selene import have
import os


def test_demo_tools(window_configurate_chrome):
    browser.element('#firstName').type('Alisha')
    browser.element('#lastName').type('Meier')
    browser.element('#userEmail').type('alisha.meyer@gmail.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').set_value('9969878866')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="10"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1995"]').click()
    browser.element('[aria-label="Choose Friday, November 3rd, 1995"]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../image/wolf_tester.jpeg'))
    browser.element('#currentAddress').type('Kaliningrad')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter()
    browser.element('#submit').scroll_to().press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.modal-body td+td').should(have.texts(
        'Alisha Meier',
        'alisha.meyer@gmail.com',
        'Female',
        '9969878866',
        '03 November,1995',
        'Computer Science',
        'Reading, Music',
        'wolf_tester.jpeg',
        'Kaliningrad',
        'NCR Gurgaon'))
