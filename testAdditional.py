"""
Additional Tests
Each file that starts with test... in this directory is scanned for subclasses of unittest.TestCase or testLib.RestTestCase
"""

import unittest
import os
import testLib

class TestFuncs(testLib.RestTestCase):
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    """Test Login"""
    def testGoodLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'newuser', 'password' : 'pass' } )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'newuser', 'password' : 'pass' } )
        self.assertResponse(respData, count = 2)

    def testBadLogin(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'pass' } )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user', 'password' : 'wrongpass' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    def testNoUserLogin(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'nonexist', 'password' : '' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    """Test Add"""
    def testAddNoUser(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'wrongpass' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    def testAddExistUser(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'herealready', 'password' : '' } )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'herealready', 'password' : 'hereagain' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_USER_EXISTS)

    def testAddLongUser(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'somethingthatistoolongandatleastonehundredcharacterslongsomethingthatistoolongandatleastonehundredcharacterslongsomethingthatistoolongandatleastonehundredcharacterslong', 'password' : '' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    def testAddLongPass(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'somethingthatistoolongandatleastonehundredcharacterslongsomethingthatistoolongandatleastonehundredcharacterslongsomethingthatistoolongandatleastonehundredcharacterslong' } )
        self.assertResponse(respData, count = None, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)
