class Error:
    ERROR_CREATE_TRAIL = 2009
    ERROR_CREATE_STUDY = 2008
    NOT_FOUND_ALGO = 2007
    ERROR_CREATE_ALGO = 2006
    ERROR_CREATE_USER = 2005
    USERNAME_LENGTH = 2004
    EXIST_USERNAME = 2003
    NOT_FOUND_USERNAME = 2001
    ERROR_PASSWORD = 2000

    ERROR_METHOD = 1004
    REQUIRE_LOGIN = 1003
    REQUIRE_JSON = 1002
    REQUIRE_PARAM = 1001
    NOT_FOUND_ERROR = 1000
    OK = 0

    ERROR_TUPLE = (
        (ERROR_CREATE_TRAIL, "Error Create Trail"),
        (ERROR_CREATE_STUDY, "Error Create Study"),
        (NOT_FOUND_ALGO, "Algorithm Not Exist"),
        (ERROR_CREATE_ALGO, "Error Create Algorithm"),
        (ERROR_CREATE_USER, "Error Create User"),
        (USERNAME_LENGTH, "Too Long Username Length"),
        (EXIST_USERNAME, "Exist Username"),
        (NOT_FOUND_USERNAME, "Username Not Exist"),
        (ERROR_PASSWORD, "Error Username Or Password"),

        (ERROR_METHOD, 'Error HTTP Request Method'),
        (REQUIRE_LOGIN, "Require Login"),
        (REQUIRE_JSON, "Require JSON"),
        (REQUIRE_PARAM, "Require Parameter: "),
        (NOT_FOUND_ERROR, "Error Not Exist"),
        (OK, "ok"),
    )