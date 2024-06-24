class GLDPMException(Exception):
    """
    Exception that is raised when the communication response contains a Fault
    element. The fault information will be included in the Exception.
    """
    def __init__(self, fault):
        message = f"{fault.faultcode} - {fault.faultstring}"
        super().__init__(message)
        self.fault = fault


class HTTPException(Exception):
    """
    Raised when there is a non-200 HTTP Status.
    """


class ParsingException(Exception):
    """
    Exception that is raised when the response message could not be parsed.
    """
