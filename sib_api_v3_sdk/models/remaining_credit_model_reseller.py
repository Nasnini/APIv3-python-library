# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RemainingCreditModelReseller(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sms': 'int',
        'email': 'int'
    }

    attribute_map = {
        'sms': 'sms',
        'email': 'email'
    }

    def __init__(self, sms=None, email=None):  # noqa: E501
        """RemainingCreditModelReseller - a model defined in Swagger"""  # noqa: E501

        self._sms = None
        self._email = None
        self.discriminator = None

        self.sms = sms
        self.email = email

    @property
    def sms(self):
        """Gets the sms of this RemainingCreditModelReseller.  # noqa: E501

        SMS Credits remaining for reseller account  # noqa: E501

        :return: The sms of this RemainingCreditModelReseller.  # noqa: E501
        :rtype: int
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this RemainingCreditModelReseller.

        SMS Credits remaining for reseller account  # noqa: E501

        :param sms: The sms of this RemainingCreditModelReseller.  # noqa: E501
        :type: int
        """
        if sms is None:
            raise ValueError("Invalid value for `sms`, must not be `None`")  # noqa: E501

        self._sms = sms

    @property
    def email(self):
        """Gets the email of this RemainingCreditModelReseller.  # noqa: E501

        Email Credits remaining for reseller account  # noqa: E501

        :return: The email of this RemainingCreditModelReseller.  # noqa: E501
        :rtype: int
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RemainingCreditModelReseller.

        Email Credits remaining for reseller account  # noqa: E501

        :param email: The email of this RemainingCreditModelReseller.  # noqa: E501
        :type: int
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RemainingCreditModelReseller):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
