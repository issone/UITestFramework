pytest -s -q test_iscloud.py --alluredir allure-result
将test_iscloud.py 测试结果写入到allure-result目录

allure generate allure-result -o allure-report/html
将allure-result中的测试结果生成静态文件


allure serve allure-result
将allure-result中的测试结果生成临时文件并打开测试结果页面

