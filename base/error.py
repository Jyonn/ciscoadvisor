class Error:
    FINISHED = 2019
    STUDY_IS_NOT_RUNNING = 2018
    STUDY_PAUSED = 2017
    NOT_FOUND_TRAIL = 2016
    METRIC_FLOAT = 2015
    NO_RIGHT_MODIFY_STUDY = 2014
    NO_SERVER_AVAILABLE = 2013
    ERROR_CREATE_ALGO_SERVER = 2012
    STUDY_IS_RUNNING_OR_FINISHED = 2011
    NOT_FOUND_STUDY = 2010
    ERROR_CREATE_TRAIL = 2009
    ERROR_CREATE_STUDY = 2008
    NOT_FOUND_ALGO = 2007
    ERROR_CREATE_ALGO = 2006
    ERROR_CREATE_USER = 2005
    USERNAME_LENGTH = 2004
    EXIST_USERNAME = 2003
    NOT_FOUND_USER = 2001
    ERROR_PASSWORD = 2000

    STRANGE = 1005
    ERROR_METHOD = 1004
    REQUIRE_LOGIN = 1003
    REQUIRE_JSON = 1002
    REQUIRE_PARAM = 1001
    NOT_FOUND_ERROR = 1000
    OK = 0

    ERROR_TUPLE = (
        (FINISHED, "Study Finished"),
        (STUDY_IS_NOT_RUNNING, "Study Is Not Running"),
        (STUDY_PAUSED, "Study Paused"),
        (NOT_FOUND_TRAIL, "Trail Not Exist"),
        (METRIC_FLOAT, "Metric Should Be An Integer Or Float"),
        (NO_RIGHT_MODIFY_STUDY, "No Right To Modify This Study"),
        (NO_SERVER_AVAILABLE, "No Server Available"),
        (ERROR_CREATE_ALGO_SERVER, "Error Create Algo Server"),
        (STUDY_IS_RUNNING_OR_FINISHED, "Study Is Running Or Finished"),
        (NOT_FOUND_STUDY, "Study Not Exist"),
        (STRANGE, "Strange Error"),
        (ERROR_CREATE_TRAIL, "Error Create Trail"),
        (ERROR_CREATE_STUDY, "Error Create Study"),
        (NOT_FOUND_ALGO, "Algorithm Not Exist"),
        (ERROR_CREATE_ALGO, "Error Create Algorithm"),
        (ERROR_CREATE_USER, "Error Create User"),
        (USERNAME_LENGTH, "Too Long Username Length"),
        (EXIST_USERNAME, "Exist Username"),
        (NOT_FOUND_USER, "Username Not Exist"),
        (ERROR_PASSWORD, "Error Username Or Password"),

        (ERROR_METHOD, 'Error HTTP Request Method'),
        (REQUIRE_LOGIN, "Require Login"),
        (REQUIRE_JSON, "Require JSON"),
        (REQUIRE_PARAM, "Require Parameter: "),
        (NOT_FOUND_ERROR, "Error Not Exist"),
        (OK, "ok"),
    )