# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import sib_api_v3_sdk
from sib_api_v3_sdk.api.transactional_sms_api import TransactionalSMSApi  # noqa: E501
from sib_api_v3_sdk.rest import ApiException


class TestTransactionalSMSApi(unittest.TestCase):
    """TransactionalSMSApi unit test stubs"""

    def setUp(self):
        self.api = sib_api_v3_sdk.api.transactional_sms_api.TransactionalSMSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sms_events(self):
        """Test case for get_sms_events

        Get all the SMS activity (unaggregated events)  # noqa: E501
        """
        pass

    def test_get_transac_aggregated_sms_report(self):
        """Test case for get_transac_aggregated_sms_report

        Get your SMS activity aggregated over a period of time  # noqa: E501
        """
        pass

    def test_get_transac_sms_report(self):
        """Test case for get_transac_sms_report

        Get your SMS activity aggregated per day  # noqa: E501
        """
        pass

    def test_send_transac_sms(self):
        """Test case for send_transac_sms

        Send the SMS campaign to the specified mobile number  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
