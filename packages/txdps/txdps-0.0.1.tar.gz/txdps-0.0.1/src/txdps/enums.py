import enum


@enum.unique
class AppointmentType(enum.Enum):
    NEW_LICENSE = 71
    RENEW_LICENSE = 81
    ROAD_TEST = 21
