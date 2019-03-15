# coding: utf-8

"""
    Pulp3 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FilePublisher(object):
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
        'href': 'str',
        'created': 'datetime',
        'type': 'str',
        'name': 'str',
        'last_updated': 'datetime',
        'distributions': 'list[str]',
        'manifest': 'str'
    }

    attribute_map = {
        'href': '_href',
        'created': '_created',
        'type': '_type',
        'name': 'name',
        'last_updated': '_last_updated',
        'distributions': 'distributions',
        'manifest': 'manifest'
    }

    def __init__(self, href=None, created=None, type=None, name=None, last_updated=None, distributions=None, manifest='PULP_MANIFEST'):  # noqa: E501
        """FilePublisher - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._created = None
        self._type = None
        self._name = None
        self._last_updated = None
        self._distributions = None
        self._manifest = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if created is not None:
            self.created = created
        if type is not None:
            self.type = type
        self.name = name
        if last_updated is not None:
            self.last_updated = last_updated
        if distributions is not None:
            self.distributions = distributions
        if manifest is not None:
            self.manifest = manifest

    @property
    def href(self):
        """Gets the href of this FilePublisher.  # noqa: E501


        :return: The href of this FilePublisher.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FilePublisher.


        :param href: The href of this FilePublisher.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created(self):
        """Gets the created of this FilePublisher.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this FilePublisher.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FilePublisher.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this FilePublisher.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def type(self):
        """Gets the type of this FilePublisher.  # noqa: E501


        :return: The type of this FilePublisher.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FilePublisher.


        :param type: The type of this FilePublisher.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this FilePublisher.  # noqa: E501

        A unique name for this publisher.  # noqa: E501

        :return: The name of this FilePublisher.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilePublisher.

        A unique name for this publisher.  # noqa: E501

        :param name: The name of this FilePublisher.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def last_updated(self):
        """Gets the last_updated of this FilePublisher.  # noqa: E501

        Timestamp of the most recent update of the publisher configuration.  # noqa: E501

        :return: The last_updated of this FilePublisher.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this FilePublisher.

        Timestamp of the most recent update of the publisher configuration.  # noqa: E501

        :param last_updated: The last_updated of this FilePublisher.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def distributions(self):
        """Gets the distributions of this FilePublisher.  # noqa: E501


        :return: The distributions of this FilePublisher.  # noqa: E501
        :rtype: list[str]
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """Sets the distributions of this FilePublisher.


        :param distributions: The distributions of this FilePublisher.  # noqa: E501
        :type: list[str]
        """

        self._distributions = distributions

    @property
    def manifest(self):
        """Gets the manifest of this FilePublisher.  # noqa: E501

        Name of the file manifest, the full path will be url/manifest  # noqa: E501

        :return: The manifest of this FilePublisher.  # noqa: E501
        :rtype: str
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """Sets the manifest of this FilePublisher.

        Name of the file manifest, the full path will be url/manifest  # noqa: E501

        :param manifest: The manifest of this FilePublisher.  # noqa: E501
        :type: str
        """
        if manifest is not None and len(manifest) < 1:
            raise ValueError("Invalid value for `manifest`, length must be greater than or equal to `1`")  # noqa: E501

        self._manifest = manifest

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
        if not isinstance(other, FilePublisher):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other