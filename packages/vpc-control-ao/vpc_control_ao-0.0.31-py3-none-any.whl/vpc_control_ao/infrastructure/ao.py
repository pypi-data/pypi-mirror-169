from ddd_objects.infrastructure.ao import exception_class_dec
from ddd_objects.infrastructure.repository_impl import error_factory
from ddd_objects.domain.exception import return_codes
import json, requests
from typing import List
from .do import (
    CommandItemDO,
    CommandRequestDO,
    ConditionDO,
    DNSRecordDO,
    InstanceCreationItemDO,
    InstanceCreationRequestDO,
    InstanceInfoDO,
    InstanceTypeUserSettingDO,
    InstanceTypeWithStatusDO,
    InstanceUserSettingDO,
    CommandResultDO,
    CommandSettingDO,
    OSSObjectDO,
    OSSOperationInfoDO
)

class VPCController:
    def __init__(self, ip:str, port:str, token:str) -> None:
        self.url = f"http://{ip}:{port}"
        self.header = {"api-token":token}

    def _check_error(self, status_code, info):
        if status_code>299:
            if isinstance(info['detail'], str):
                return_code = return_codes['OTHER_CODE']
                error_traceback = info['detail']
            else:
                return_code = info['detail']['return_code']
                error_traceback = info['detail']['error_traceback']
            raise error_factory.make(return_code)(error_traceback)

    @exception_class_dec()
    def check_connection(self, timeout=3):
        response=requests.get(f'{self.url}', headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        if info['message']=='Hello World':
            return True
        else:
            return False

    @exception_class_dec()
    def new_instance(self, condition:ConditionDO, setting:InstanceUserSettingDO, timeout=1200):
        data = {
            "condition": condition.dict(),
            "setting": setting.dict()
        }
        data = json.dumps(data)
        response=requests.post(f'{self.url}/instances', 
            headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        if infos is None:
            return None
        else:
            return [InstanceInfoDO(**info) for info in infos]

    @exception_class_dec()
    def get_instance(self, region_id: str, timeout=60):
        response=requests.get(f'{self.url}/instances/region_id/{region_id}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [InstanceInfoDO(**info) for info in infos]

    @exception_class_dec()
    def get_instance_by_name(self, region_id: str, name: str, timeout=60):
        response=requests.get(f'{self.url}/instances/region_id/{region_id}/name/{name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [InstanceInfoDO(**info) for info in infos]

    @exception_class_dec()
    def get_instance_type_status(self, settings: List[InstanceTypeUserSettingDO], timeout=60):
        data = [setting.to_json() for setting in settings]
        data = json.dumps(data)
        response=requests.get(f'{self.url}/instance_types/status', 
            headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [InstanceTypeWithStatusDO(**r) for r in infos]

    @exception_class_dec()
    def release_instances(self, instance_infos: List[InstanceInfoDO], timeout=60):
        instance_infos = [info.dict() for info in instance_infos]
        data = json.dumps(instance_infos)
        response=requests.delete(f'{self.url}/instances', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec()
    def run_command(
        self, 
        instance_infos: List[InstanceInfoDO], 
        settings: List[CommandSettingDO]
    ):
        timeout = 0
        for s in settings:
            timeout += s.timeout
        instance_infos = [info.dict() for info in instance_infos]
        settings = [setting.to_json() for setting in settings]
        data = {
            "instance_infos": instance_infos,
            "command_settings": settings
        }
        data = json.dumps(data)
        response=requests.post(f'{self.url}/instances/command', 
            headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [CommandResultDO(**r) if r else None for r in infos]

    @exception_class_dec()
    def oss_operate(self, 
        instance_infos: List[InstanceInfoDO], 
        oss_operation_info: OSSOperationInfoDO,
        command_setting: CommandSettingDO,
        timeout=60
    ):
        instance_infos = [info.dict() for info in instance_infos]
        data = {
            "instance_infos": instance_infos,
            "oss_operation_info": oss_operation_info.to_json(),
            "command_setting": command_setting.to_json()
        }
        data = json.dumps(data)
        response=requests.post(f'{self.url}/instances/oss', 
            headers=self.header, data=data, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [CommandResultDO(**r) for r in infos]

    @exception_class_dec()
    def create_dns_record(
        self,
        record: DNSRecordDO,
        timeout=30
    ):
        data = record.to_json()
        data = json.dumps(data)
        response = requests.post(f'{self.url}/dns_record',
            headers = self.header, data=data, timeout=timeout
        )
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return DNSRecordDO(**info)

    @exception_class_dec()
    def get_dns_records(
        self,
        domain_name: str,
        timeout=20
    ):
        response = requests.get(f'{self.url}/dns_records/domain_name/{domain_name}', 
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [DNSRecordDO(**info) for info in infos]

    @exception_class_dec()
    def update_dns_record(self, record: DNSRecordDO, timeout=30):
        data = json.dumps(record.to_json())
        response = requests.put(f'{self.url}/dns_record', 
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return DNSRecordDO(**info)

    @exception_class_dec()
    def delete_dns_record(self, record_id: str, timeout=30):
        response = requests.delete(f'{self.url}/dns_record/record_id/{record_id}',
            headers=self.header, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec()
    def list_oss_objects(self, bucket_name:str, endpoint:str, timeout=3):
        response = requests.get(f'{self.url}/oss_objects/bucket_name/{bucket_name}/endpoint/{endpoint}',
            headers=self.header, timeout=timeout)
        infos = json.loads(response.text)
        self._check_error(response.status_code, infos)
        return [OSSObjectDO(**r) for r in infos]

    @exception_class_dec()
    def delete_oss_object(self, oss_object: OSSObjectDO, timeout=3):
        data = json.dumps(oss_object.to_json())
        response = requests.delete(f'{self.url}/oss_object',
            headers=self.header, data=data, timeout=timeout)
        info = json.loads(response.text)
        self._check_error(response.status_code, info)
        return info

    @exception_class_dec()
    def send_instance_creation_request(self, request: InstanceCreationRequestDO, timeout=3):
        data = json.dumps(request.dict())
        response=requests.post(f'{self.url}/instance/request', 
            headers=self.header, data=data, timeout=timeout)
        id = json.loads(response.text)
        self._check_error(response.status_code, id)
        if id is None:
            return None
        else:
            return id

    @exception_class_dec()
    def find_instance_creation_item(self, id: str, timeout=3):
        response=requests.get(f'{self.url}/instance/item/id/{id}', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return InstanceCreationItemDO(**item)

    @exception_class_dec()
    def find_unprocessed_instance_creation_item(self, timeout=3):
        response=requests.get(f'{self.url}/instance/item/unprocessed', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return InstanceCreationItemDO(**item)

    @exception_class_dec()
    def update_instance_creation_item(self, item:InstanceCreationItemDO, timeout=10):
        data = json.dumps(item.dict())
        response=requests.put(f'{self.url}/instance/item', 
            headers=self.header, data=data, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

    @exception_class_dec()
    def clear_instance_creation_item(self, timeout=3):
        response=requests.get(f'{self.url}/instance/item/clear', 
            headers=self.header, timeout=timeout)
        n = json.loads(response.text)
        self._check_error(response.status_code, n)
        return n

    @exception_class_dec()
    def delete_instance_creation_item(self, item_id:str, timeout=3):
        response=requests.delete(f'{self.url}/instance/item/id/{item_id}', 
            headers=self.header, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

    @exception_class_dec()
    def send_command_request(self, request: CommandRequestDO, timeout=3):
        data = json.dumps(request.dict())
        response=requests.post(f'{self.url}/command/request', 
            headers=self.header, data=data, timeout=timeout)
        id = json.loads(response.text)
        self._check_error(response.status_code, id)
        if id is None:
            return None
        else:
            return id

    @exception_class_dec()
    def find_command_item(self, id: str, timeout=3):
        response=requests.get(f'{self.url}/command/item/id/{id}', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return CommandItemDO(**item)

    @exception_class_dec()
    def find_unprocessed_command_item(self, timeout=3):
        response=requests.get(f'{self.url}/command/item/unprocessed', 
            headers=self.header, timeout=timeout)
        item = json.loads(response.text)
        self._check_error(response.status_code, item)
        if item is None:
            return None
        else:
            return CommandItemDO(**item)

    @exception_class_dec()
    def update_command_item(self, item:CommandItemDO, timeout=10):
        data = json.dumps(item.dict())
        response=requests.put(f'{self.url}/command/item', 
            headers=self.header, data=data, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

    @exception_class_dec()
    def clear_command_item(self, timeout=3):
        response=requests.get(f'{self.url}/command/item/clear', 
            headers=self.header, timeout=timeout)
        n = json.loads(response.text)
        self._check_error(response.status_code, n)
        return n

    @exception_class_dec()
    def delete_command_item(self, item_id:str, timeout=3):
        response=requests.delete(f'{self.url}/command/item/id/{item_id}', 
            headers=self.header, timeout=timeout)
        succeed = json.loads(response.text)
        self._check_error(response.status_code, succeed)
        return succeed

repo_info = \
{
    "DNSRepository":{
        "create_dns_record":{
            "args":[["record", True, "DNSRecord", None, False, False, "dns_record_converter"]],
            "ret":["record", True, "DNSRecord", None, False, True, "dns_record_converter"]
        },
        "delete_dns_record":{
            "args":[["record_id", False]]
        },
        "get_dns_records":{
            "args":[["domain_name", False]],
            "ret":["records", True, "DNSRecord", None, True, True, "dns_record_converter"],
            "key":"{domain_name}:dns_records"
        },
        "update_dns_record":{
            "args":[["record", True, "DNSRecord", None, True, True, "dns_record_converter"]],
            "ret":["record", True, "DNSRecord", None, False, True, "dns_record_converter"]
        }
    },
    "VPCRepository":{
        "get_instance":{
            "args":[["region_id", False]],
            "ret":["instance_info", True, None, None, True, True],
            "key":"{region_id}:instances"
        },
        "get_instance_by_name":{
            "args":[["region_id", False], ["name", False, "Name", None]],
            "ret":["instance_info", True, None, None, True, True],
            "key":"{region_id}:{name}:instances"
        },
        "get_instance_type_status":{
            "args":[["settings", True, "InstanceTypeUserSetting", None, True]],
            "ret":["instance_type_with_status", True, None, None, True, True],
            "key":"{settings}:instance_type_status"
        },
        "new_instance":{
            "args":["condition", ["setting", True, "InstanceUserSetting"]],
            "ret":["instance_info", True, None, None, True, True]
        },
        "oss_operate":{
            "args":[["instance_infos", True, "InstanceInfo", None, True], ["oss_operation_info", True, "OSSOperationInfo", None, False, False, "oss_operation_info_converter"], "command_setting"],
            "ret":["command_result", True, None, None, True, True]
        },
        "release_instances":{
            "args":[["instance_infos", True, "InstanceInfo", None, True]]
        },
        "run_command":{
            "args":[["instance_infos", True, "InstanceInfo", None, True], "command_setting"],
            "ret":["command_result", True, None, None, True, True]
        }
    }
}