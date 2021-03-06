"""
Close Service Module
===================
This package contains the close methods defined by Fedex's
CloseService WSDL file. Each is encapsulated in a class for easy access.
For more details on each, refer to the respective class's documentation.
"""
from .. base_service import FedexBaseService


class SmartPostCloseShipmentRequest(FedexBaseService):
    """
    This class allows you to process (create) a new FedEx close service. You will
    need to populate the data structures in self.RequestedShipment, then
    send the request. Label printing is supported and very configurable,
    returning an ASCII representation with the response as well.
    """
    def __init__(self, config_obj, *args, **kwargs):
        """
        The optional keyword args detailed on L{FedexBaseService}
        apply here as well.

        @type config_obj: L{FedexConfig}
        @param config_obj: A valid FedexConfig object.
        """
        self._config_obj = config_obj

        # Holds version info for the VersionId SOAP object.
        self._version_info = {'service_id': 'clos', 'major': '2',
                             'intermediate': '0', 'minor': '0'}

        # Call the parent FedexBaseService class for basic setup work.
        super(SmartPostCloseShipmentRequest, self).__init__(self._config_obj,
                                                         'CloseService_v2.wsdl',
                                                         *args, **kwargs)

    def _prepare_wsdl_objects(self):
        """
        This is the data that will be used to create your close service. Create
        the data structure and get it ready for the WSDL request.
        """
        # This is the primary data structure for processShipment requests.
        self.HubId = None
        self.DestinationCountryCode = 'US'
        self.PickUpCarrier = None
        # This is good to review if you'd like to see what the data structure
        # looks like.
        #self.logger.debug(self.SmartPostCloseRequest)

    def _assemble_and_send_request(self):
        """
        Fires off the Fedex request.

        @warning: NEVER CALL THIS METHOD DIRECTLY. CALL send_request(),
            WHICH RESIDES ON FedexBaseService AND IS INHERITED.
        """
        # Fire off the query.
        response = self.client.service.smartPostClose(WebAuthenticationDetail=self.WebAuthenticationDetail,
                                        ClientDetail=self.ClientDetail,
                                        TransactionDetail=self.TransactionDetail,
                                        Version=self.VersionId,
                                        HubId=self.HubId,
                                        DestinationCountryCode=self.DestinationCountryCode,
                                        PickUpCarrier=self.PickUpCarrier)
        return response
