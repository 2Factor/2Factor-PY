# -*- coding: utf-8 -*-

"""
   M2Factor.Models.VerifyVoiceOtpInputModel
 
   This file was automatically generated for 2Factor by APIMATIC BETA v2.0 on 02/18/2016
"""
from M2Factor.APIHelper import APIHelper

class VerifyVoiceOtpInputModel(object):

    """Implementation of the 'verify-voice-otp-input-model' model.

    TODO: type model description here.

    Attributes:
        status (string): TODO: type description here.
        details (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the VerifyVoiceOtpInputModel class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    Status -- string -- Sets the attribute status
                    Details -- string -- Sets the attribute details
        
        """
        # Set all of the parameters to their default values
        self.status = None
        self.details = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "Status": "status",
            "Details": "details",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "status": "Status",
            "details": "Details",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)