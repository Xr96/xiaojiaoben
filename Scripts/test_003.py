# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 11:32
# @Author  : Fighter.Wu
import allure

class Test003:

    @allure.severity(allure.severity_level.BLOCKER)   # 很严重的
    def test0031(self):
        assert True

    @allure.severity(allure.severity_level.CRITICAL)   # 严重的
    def test0032(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)   # 普通的
    def test0033(self):
        assert True

    @allure.severity(allure.severity_level.MINOR)   # 轻微的
    def test0034(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)  # 可略过
    def test0035(self):
        assert True