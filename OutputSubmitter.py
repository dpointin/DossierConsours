# coding: utf-8
# !/usr/bin/env python
import os
import shutil
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import autoit
import time


def get_parent_path(path):
    return os.path.abspath(os.path.join(path, os.pardir))


def zip_folder(zip_name, folder_to_zip):
    shutil.make_archive(zip_name, 'zip', folder_to_zip)
    return os.path.join(os.getcwd(), zip_name + '.zip')


class OutputSubmitter:
    LOGIN_PATH = "https://accounts.google.com/ServiceLogin/signinchooser"
    SUBMISSION_PATH = 'https://hashcodejudge.withgoogle.com/#/rounds/5736842779426816/submissions/'
    LOGIN = "matthias.larre"
    PASSWORD = "XXXXXXXXX"  # set your google password here

    def __init__(self, project_name):
        self.web_browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.web_browser, 10)
        self.project_name = project_name

    def google_log_in(self):
        self.web_browser.get(self.LOGIN_PATH)
        for (element_name, value, validation) in [("identifier", self.LOGIN, "identifierNext"),
                                                  ("password", self.PASSWORD, "passwordNext")]:
            self.wait.until(expected_conditions.element_to_be_clickable((By.ID, validation)))
            self.web_browser.find_element_by_name(element_name).send_keys(value)
            self.web_browser.find_element_by_id(validation).click()
        # Wait until welcome zone is displayed on the screen
        self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ZrQ9j")))

    def find_by_ng_click(self, ng_click_pattern):
        return self.web_browser.find_elements_by_xpath("//*[@ng-click='{}']".format(ng_click_pattern))

    def safe_ng_click(self, ng_click_pattern, button=None):
        xpath_pattern = "//*[@ng-click='{}']".format(ng_click_pattern)
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath_pattern)))
        if not button:
            self.find_by_ng_click(ng_click_pattern)[0].click()
        else:
            button.click()

    def get_output_files(self):
        output_folder = os.path.join(os.getcwd(), self.project_name, "output")
        output_folder_list = os.listdir(output_folder)
        output_current_id = 0
        output_files = []
        for i, input_file in enumerate(xrange(len(os.listdir(os.path.join(os.getcwd(), self.project_name, "input"))))):
            output_current_file = output_folder_list[output_current_id] \
                if output_current_id < len(output_folder_list) else ""
            if str(i) in output_current_file:
                output_files.append(os.path.join(output_folder, output_current_file))
                output_current_id += 1
            else:
                output_files.append("")
        return output_files

    def submit_output(self):
        output_files = [zip_folder('source_code', os.path.join(os.getcwd(), self.project_name, "source"))]
        output_files += self.get_output_files()

        self.web_browser.get(self.SUBMISSION_PATH)
        self.safe_ng_click("submissionsCtrl.showCreateSubmissionDialog()")
        upload_buttons = self.find_by_ng_click("ctrl.onUploadClick($event)")
        for i, file_to_upload in enumerate(output_files):
            if not file_to_upload:
                continue
            self.safe_ng_click("ctrl.onUploadClick($event)", upload_buttons[i])
            time.sleep(1)
            autoit.win_wait_active("[CLASS:#32770;TITLE:Ouvrir]", 60)
            autoit.control_send("[CLASS:#32770;TITLE:Ouvrir]", "Edit1", file_to_upload)
            autoit.control_click("[CLASS:#32770;TITLE:Ouvrir]", "Button1")
        time.sleep(2)
        self.find_by_ng_click("submissionsCtrl.createSubmission()")[0].click()

    def close(self):
        self.web_browser.close()
