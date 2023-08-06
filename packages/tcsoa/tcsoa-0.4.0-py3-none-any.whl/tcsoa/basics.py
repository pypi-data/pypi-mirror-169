from typing import List, Dict

from tcsoa.backend import RestBackend
from tcsoa.config import TcSoaConfig
from tcsoa.gen.BusinessObjects import BusinessObject
from tcsoa.gen.Core._2007_12.Session import StateNameValue
from tcsoa.gen.Core._2011_06.Session import Credentials
from tcsoa.gen.Core.services import DataManagementService, SessionService


class TcSoaBasics:
    NULLTAG = 'AAAAAAAAAAAAAA'

    # Login configuration
    username = None
    password = None
    group = ''
    role = ''
    locale = 'en_US'
    descrimator = 'TcSoa.py'

    # Server Information
    log_file: str = None
    server: str = None

    @classmethod
    def setCredentials(cls, username, password, group='', role=''):
        cls.username = username
        cls.password = password
        cls.group = group
        cls.role = role

    @classmethod
    def login(cls):
        login_response = SessionService().login3(
            credentials=Credentials(
                user=cls.username,
                password=cls.password,
                group=cls.group,
                role=cls.role,
                locale=cls.locale,
                descrimator=cls.descrimator,
            )
        )
        cls.log_file = login_response.serverInfo['LogFile']
        cls.server = login_response.serverInfo['HostName']
        return login_response

    @classmethod
    def logout(cls):
        return SessionService().logout()

    @classmethod
    def load_objects(cls, uids: List[str]) -> Dict[str, BusinessObject]:
        if not uids:
            return dict()
        load_objs_result = DataManagementService().loadObjects(uids=uids)
        model_objects = load_objs_result['modelObjects']
        return {p: model_objects[p] for p in load_objs_result['plain']}

    @classmethod
    def load_object(cls, uid: str):
        obj = None
        for obj in cls.load_objects([uid]).values():
            break
        return obj

    @classmethod
    def getProperties(cls, objects: List[BusinessObject], properties: List[str]) -> Dict[str, BusinessObject]:
        response = DataManagementService().getProperties(
            objects=objects,
            attributes=properties
        )
        return {uid: response['modelObjects'][uid] for uid in response['plain']}

    @classmethod
    def getProperty(cls, bo: BusinessObject, prop_name: str):
        return cls.getProperties([bo], [prop_name])[bo['uid']]['props'][prop_name]

    @classmethod
    def bool2property_str(cls, val: bool) -> str:
        return '1' if val else '0'

    @classmethod
    def setBypass(cls, enabled=True):
        return SessionService().setUserSessionState(
            pairs=[
                StateNameValue(
                    name='fnd0bypassflag',
                    value=cls.bool2property_str(enabled)
                )
            ]
        )

    @classmethod
    def set_object_load_policy(cls, bo_name: str, properties: List[str]):
        rest_backend: RestBackend = TcSoaConfig.backend
        rest_backend.set_object_load_policy(bo_name, properties)
