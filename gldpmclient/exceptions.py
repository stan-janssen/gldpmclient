class GLDPMException(Exception):
    """
    Exception that is raised when the communication response contains a Fault
    element. The fault information will be included in the Exception.
    """
    def __init__(self, fault):
        message = f"{fault.faultcode} - {fault.faultstring}"
        super().__init__(message)
        self.fault = fault
