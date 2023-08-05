from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Generic, List, Tuple, TypeVar


@dataclass
class FieldItem:
    name: str
    caption: str
    visible: bool = True


@dataclass
class FullName:
    last_name: str = None
    first_name: str = None
    middle_name: str = None


@dataclass
class ActionValue:
    caption: str
    value: str


@dataclass
class LoginPasswordPair:
    login: str = None
    password: str = None

@dataclass
class ServiceRoleValue:
    name: str
    description: str
    host: str
    port: str
    commands: List = field(default_factory=list)
    libs: List[str] = field(default_factory=list)
    service_path: str = None
    pid: int = -1
    ppid: int = -1

class FieldItemList:

    list: List[FieldItem]

    def __init__(self, *args):
        self.list = []
        arg_list = list(args)
        for arg_item in arg_list:
            if isinstance(arg_item, FieldItem):
                item: FieldItem = FieldItem(
                    arg_item.name, arg_item.caption, arg_item.visible)
                self.list.append(item)
            elif isinstance(arg_item, FieldItemList):
                for item_list in arg_item.list:
                    item: FieldItem = FieldItem(
                        item_list.name, item_list.caption, item_list.visible)
                    self.list.append(item)
            elif isinstance(arg_item, list):
                self.list.extend(arg_item)

    def get_list(self) -> List[FieldItem]:
        return self.list

    def get_item_and_index_by_name(self, value: str) -> Tuple[FieldItem, int]:
        index: int = -1
        result: FieldItem = None
        for item in self.list:
            index += 1
            if item.name == value:
                result = item
                break
        return result, -1 if result is None else index

    def get_item_by_name(self, value: str) -> FieldItem:
        result, _ = self.get_item_and_index_by_name(value)
        return result

    def position(self, name: str, position: int):
        _, index = self.get_item_and_index_by_name(name)
        if index != -1:
            self.list.insert(position, self.list.pop(index))
        return self

    def get_name_list(self):
        return list(map(lambda x: str(x.name), self.list))

    def get_caption_list(self):
        return list(map(lambda x: str(x.caption), filter(lambda y: y.visible, self.list)))

    def visible(self, name: str, value: bool):
        item, _ = self.get_item_and_index_by_name(name)
        if item is not None:
            item.visible = value
        return self

    def length(self) -> int:
        return len(self.list)


T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    fields: FieldItemList
    data: T


@dataclass
class UserContainer:
    name: str = None
    description: str = None
    distinguishedName: str = None


@dataclass
class User(UserContainer):
    samAccountName: str = None
    mail: str = None
    telephoneNumber: str = None
    userAccountControl: int = None


@dataclass
class MarkBase:
    FullName: str = None
    TabNumber: str = None
    DivisionName: str = None


@dataclass
class Patient:
    FullName: str = None
    Comment: str = None


@dataclass
class Mark(MarkBase):
    pID: int = None
    mID: int = None
    GroupName: str = None
    GroupID: int = None
    Comment: str = None
    telephoneNumber: str = None


@dataclass
class MarkDivision:
    id: int = None
    name: str = None


@dataclass
class TimeTrackingEntity(MarkBase):
    TimeVal: str = None
    Mode: int = None


@dataclass
class TimeTrackingResultByDate:
    date: str = None
    enter_time: str = None
    exit_time: str = None
    duration: int = None


@dataclass
class TimeTrackingResultByPerson():
    tab_number: str = None
    full_name: str = None
    duration: int = 0
    list: List[TimeTrackingResultByDate] = field(
        default_factory=list)


@dataclass
class TimeTrackingResultByDivision():
    name: str
    list: List[TimeTrackingResultByPerson] = field(
        default_factory=list)


@dataclass
class PrinterADInformation:
    driverName: str = None
    adminDescription: str = None
    description: str = None
    portName: str = None
    serverName: str = None
    name: str = None


@dataclass
class InventoryReportItem:
    name: str = None
    inventory_number: str = None
    row: str = None
    quantity: int = None
    name_column: int = None
    inventory_number_column: int = None
    quantity_column: int = None

@dataclass
class PrinterReport:
    ip: str = None
    desc: str = None
    variant: str = None
    port: int = None
    community: str = None
    name: str = None
    po_printer: str = None
    accessable: bool = None
    model: str = None
    serial: int = None
    meta: str = None
    printsOverall: int = None
    printsColor: int = None
    printsMonochrome: int = None
    fuserType: int = None
    fuserCapacity: int = None
    fuserRemaining: int = None
    wasteType: int = None
    wasteCapacity: int = None
    wasteRemaining: int = None
    cleanerType: int = None
    cleanerCapacity: int = None
    cleanerRemaining: int = None
    transferType: int = None
    transferCapacity: int = None
    transferRemaining: int = None
    blackTonerType: str = None
    blackTonerCapacity: int = None
    blackTonerRemaining: int = None
    cyanTonerType: int = None
    cyanTonerCapacity: int = None
    cyanTonerRemaining: int = None
    magentaTonerType: int = None
    magentaTonerCapacity: int = None
    magentaTonerRemaining: int = None
    yellowTonerType: int = None
    yellowTonerCapacity: int = None
    yellowTonerRemaining: int = None
    blackDrumType: str = None
    blackDrumCapacity: int = None
    blackDrumRemaining: int = None
    cyanDrumType: int = None
    cyanDrumCapacity: int = None
    cyanDrumRemaining: int = None
    magentaDrumType: int = None
    magentaDrumCapacity: int = None
    magentaDrumRemaining: int = None
    yellowDrumType: int = None
    yellowDrumCapacity: int = None
    yellowDrumRemaining: int = None


@dataclass
class MarkGroup:
    GroupName: str = None
    GroupID: int = None
    Count: int = None


@dataclass
class MarkGroupStatistics(MarkGroup):
    Comment: str = None


@dataclass
class PasswordSettings:
    length: int
    special_characters: str
    order_list: List[str]
    special_characters_count: int
    alphabets_lowercase_count: int
    alphabets_uppercase_count: int
    digits_count: int = 1
    shuffled: bool = False


@dataclass
class LogCommand:
    message: str
    log_channel: Enum
    log_level: int
    params: Tuple = None


@dataclass
class ParamItem:
    name: str
    caption: str
    description: str = None
