import os
import pytest

if __name__ == '__main__':
    pytest.main(["-v", "-s", "./testcase/", '--alluredir', './allure-result/'])
    os.system('allure serve ./allure-result/')
    # os.system("allure generate --clean allure-result -o  reports/html")
