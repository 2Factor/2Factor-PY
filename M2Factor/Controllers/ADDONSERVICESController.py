# -*- coding: utf-8 -*-

"""
   M2Factor.Controllers.ADDONSERVICESController

   This file was automatically generated for 2Factor by APIMATIC BETA v2.0 on 02/18/2016
"""
import unirest

from M2Factor.APIHelper import APIHelper
from M2Factor.Configuration import Configuration
from M2Factor.APIException import APIException
from M2Factor.Models.CheckBalanceAddonServicesModel import CheckBalanceAddonServicesModel
from M2Factor.Models.SendTransactionalSmsModel import SendTransactionalSmsModel


class ADDONSERVICESController(object):


    """A Controller to access Endpoints in the M2Factor API."""

    def get_check_balance_addon_services(self,
                                         api_key,
                                         service_name):
        """Does a GET request to /V1/{api_key}/ADDON_SERVICES/BAL/{service_name}.

        Check Balance For Addon Services

        Args:
            api_key (string): 2Factor account API Key
            service_name (string): Name of the addon service

        Returns:
            CheckBalanceAddonServicesModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/V1/{api_key}/ADDON_SERVICES/BAL/{service_name}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "api_key": api_key,
            "service_name": service_name
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "2Factor",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            try:
                return CheckBalanceAddonServicesModel(**response.body)
            except TypeError:
                raise APIException("Invalid JSON returned", response.code, response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body)

    def get_pull_delivery_report(self,
                                 api_key,
                                 session_id):
        """Does a GET request to /V1/{api_key}/ADDON_SERVICES/RPT/TSMS/{session_id}.

        Pull Delivery Report - Transactional SMS

        Args:
            api_key (string): API Obtained From 2Factor.in
            session_id (string): Session Id Returned By Send SMS Step

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/V1/{api_key}/ADDON_SERVICES/RPT/TSMS/{session_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "api_key": api_key,
            "session_id": session_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "2Factor",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_send_transactional_sms(self,
                                      api_key,
                                      from,
                                      msg,
                                      to,
                                      send_at=None,
                                      $fieldParameters=None):
        """Does a POST request to /V1/{api_key}/ADDON_SERVICES/SEND/TSMS.

        Send Single / Bulk Transactional Messages / Schedule SMS

        Args:
            api_key (string): API Obtained From 2Factor.in
            from (string): 6 Character Alphabet Sender Id
            msg (string): SMS Body To Be Sent
            to (string): Comma Separated list Of Phone Numbers
            send_at (string, optional): This Parameter Is Used For Scheduling
                SMS - Optional parameter
            fieldParameters (Array, optional): Additional optional form
                parameters are supported by this endpoint

        Returns:
            SendTransactionalSmsModel: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/V1/{api_key}/ADDON_SERVICES/SEND/TSMS"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "api_key": api_key
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "2Factor",
            "accept": "application/json",

        }

        # Prepare parameters
        parameters = {
            "From": from,
            "Msg": msg,
            "To": to,
            "SendAt":  send_at if send_at is not None else "2019-01-01 00:00:01"
        }
        # The body will be multipart data, so set the header
        headers['Content-Type'] = 'multipart/form-data'

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params=parameters)

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            try:
                return SendTransactionalSmsModel(**response.body)
            except TypeError:
                raise APIException("Invalid JSON returned", response.code, response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body)
