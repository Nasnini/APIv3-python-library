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


class CreateContact(object):
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
        'email': 'str',
        'attributes': 'object',
        'email_blacklisted': 'bool',
        'sms_blacklisted': 'bool',
        'list_ids': 'list[int]',
        'update_enabled': 'bool',
        'smtp_blacklist_sender': 'list[str]'
    }

    attribute_map = {
        'email': 'email',
        'attributes': 'attributes',
        'email_blacklisted': 'emailBlacklisted',
        'sms_blacklisted': 'smsBlacklisted',
        'list_ids': 'listIds',
        'update_enabled': 'updateEnabled',
        'smtp_blacklist_sender': 'smtpBlacklistSender'
    }

    def __init__(self, email=None, attributes=None, email_blacklisted=None, sms_blacklisted=None, list_ids=None, update_enabled=False, smtp_blacklist_sender=None):  # noqa: E501
        """CreateContact - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._attributes = None
        self._email_blacklisted = None
        self._sms_blacklisted = None
        self._list_ids = None
        self._update_enabled = None
        self._smtp_blacklist_sender = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if attributes is not None:
            self.attributes = attributes
        if email_blacklisted is not None:
            self.email_blacklisted = email_blacklisted
        if sms_blacklisted is not None:
            self.sms_blacklisted = sms_blacklisted
        if list_ids is not None:
            self.list_ids = list_ids
        if update_enabled is not None:
            self.update_enabled = update_enabled
        if smtp_blacklist_sender is not None:
            self.smtp_blacklist_sender = smtp_blacklist_sender

    @property
    def email(self):
        """Gets the email of this CreateContact.  # noqa: E501

        Email address of the user. Mandatory if `attributes.sms` is not passed  # noqa: E501

        :return: The email of this CreateContact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateContact.

        Email address of the user. Mandatory if `attributes.sms` is not passed  # noqa: E501

        :param email: The email of this CreateContact.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def attributes(self):
        """Gets the attributes of this CreateContact.  # noqa: E501

        Values of the attributes to fill. The attributes must exist in you contact database  # noqa: E501

        :return: The attributes of this CreateContact.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CreateContact.

        Values of the attributes to fill. The attributes must exist in you contact database  # noqa: E501

        :param attributes: The attributes of this CreateContact.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def email_blacklisted(self):
        """Gets the email_blacklisted of this CreateContact.  # noqa: E501

        Blacklist the contact for emails (emailBlacklisted = true)  # noqa: E501

        :return: The email_blacklisted of this CreateContact.  # noqa: E501
        :rtype: bool
        """
        return self._email_blacklisted

    @email_blacklisted.setter
    def email_blacklisted(self, email_blacklisted):
        """Sets the email_blacklisted of this CreateContact.

        Blacklist the contact for emails (emailBlacklisted = true)  # noqa: E501

        :param email_blacklisted: The email_blacklisted of this CreateContact.  # noqa: E501
        :type: bool
        """

        self._email_blacklisted = email_blacklisted

    @property
    def sms_blacklisted(self):
        """Gets the sms_blacklisted of this CreateContact.  # noqa: E501

        Blacklist the contact for SMS (smsBlacklisted = true)  # noqa: E501

        :return: The sms_blacklisted of this CreateContact.  # noqa: E501
        :rtype: bool
        """
        return self._sms_blacklisted

    @sms_blacklisted.setter
    def sms_blacklisted(self, sms_blacklisted):
        """Sets the sms_blacklisted of this CreateContact.

        Blacklist the contact for SMS (smsBlacklisted = true)  # noqa: E501

        :param sms_blacklisted: The sms_blacklisted of this CreateContact.  # noqa: E501
        :type: bool
        """

        self._sms_blacklisted = sms_blacklisted

    @property
    def list_ids(self):
        """Gets the list_ids of this CreateContact.  # noqa: E501

        Ids of the lists to add the contact to  # noqa: E501

        :return: The list_ids of this CreateContact.  # noqa: E501
        :rtype: list[int]
        """
        return self._list_ids

    @list_ids.setter
    def list_ids(self, list_ids):
        """Sets the list_ids of this CreateContact.

        Ids of the lists to add the contact to  # noqa: E501

        :param list_ids: The list_ids of this CreateContact.  # noqa: E501
        :type: list[int]
        """

        self._list_ids = list_ids

    @property
    def update_enabled(self):
        """Gets the update_enabled of this CreateContact.  # noqa: E501

        Facilitate to update existing contact in same request (updateEnabled = true)  # noqa: E501

        :return: The update_enabled of this CreateContact.  # noqa: E501
        :rtype: bool
        """
        return self._update_enabled

    @update_enabled.setter
    def update_enabled(self, update_enabled):
        """Sets the update_enabled of this CreateContact.

        Facilitate to update existing contact in same request (updateEnabled = true)  # noqa: E501

        :param update_enabled: The update_enabled of this CreateContact.  # noqa: E501
        :type: bool
        """

        self._update_enabled = update_enabled

    @property
    def smtp_blacklist_sender(self):
        """Gets the smtp_blacklist_sender of this CreateContact.  # noqa: E501

        SMTP forbidden sender for contact. Use only for email Contact ( only available if updateEnabled = true )  # noqa: E501

        :return: The smtp_blacklist_sender of this CreateContact.  # noqa: E501
        :rtype: list[str]
        """
        return self._smtp_blacklist_sender

    @smtp_blacklist_sender.setter
    def smtp_blacklist_sender(self, smtp_blacklist_sender):
        """Sets the smtp_blacklist_sender of this CreateContact.

        SMTP forbidden sender for contact. Use only for email Contact ( only available if updateEnabled = true )  # noqa: E501

        :param smtp_blacklist_sender: The smtp_blacklist_sender of this CreateContact.  # noqa: E501
        :type: list[str]
        """

        self._smtp_blacklist_sender = smtp_blacklist_sender

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
        if not isinstance(other, CreateContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
