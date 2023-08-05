from pprint import PrettyPrinter
import requests
from datetime import datetime

from enums import AppointmentType


class User:
    def __init__(
        self,
        firstName: str,
        lastName: str,
        dateOfBirth: str,
        ssnLastFour: str,
        appointmentType: AppointmentType
    ) -> None:
        self._BASE_URL = "https://publicapi.txdpsscheduler.com/api"
        self._HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
            'Referer': 'https://public.txdpsscheduler.com/',
            'Origin': 'https://public.txdpsscheduler.com',
            'Host': 'publicapi.txdpsscheduler.com',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json'
        }
        self._PP = PrettyPrinter(indent=4)

        self._resID = ""
        self._loggedIn = False
        self._firstName = firstName
        self._lastName = lastName
        self._dob = dateOfBirth
        self._ssn4 = ssnLastFour
        self._apmtType = appointmentType

    def login(self) -> bool:
        try:
            PAYLOAD = {
                "DateOfBirth": self._dob,
                "FirstName": self._firstName,
                "LastName": self._lastName,
                "LastFourDigitsSsn": self._ssn4
            }
            res = requests.post(url=self._BASE_URL + '/Eligibility',
                                data=str(PAYLOAD), headers=self._HEADERS)
            self._resID = res.json()[0]['ResponseId']
            self._loggedIn = True
            return True
        except requests.exceptions.HTTPError as e:
            print('[Error] Login failed: ', e.response.text)
            return False

    def switchAppointmentType(self, appointmentType: AppointmentType):
        self._apmtType = appointmentType

    def getAvailability(self, zipCode: str) -> list:
        if not self._loggedIn:
            print("[Error] Haven't logged in yet")
            return []

        return self._checkAvailability(zipCode)

    def getEarliestSlot(self, zipCode: str) -> tuple[int, dict]:
        if not self._loggedIn:
            print("[Error] Haven't logged in yet")
            return (0, {})

        availability = self._checkAvailability(zipCode)

        if len(availability) == 0:
            print('[Error] No timeslot available available')
            return (0, {})

        # sort the available locaitons by next available date
        availability.sort(key=lambda loca: datetime.strptime(loca['NextAvailableDate'], '%m/%d/%Y'))
        for location in availability:
            if location["Availability"]:
                return (
                    location['Id'],
                    location["Availability"]["LocationAvailabilityDates"][0]["AvailableTimeSlots"][0]
                )

        return (0, {})

    def getAppointmentState(self) -> list:
        if not self._loggedIn:
            print("[Error] Haven't logged in yet")
            return []

        try:
            PAYLOAD = {
                "DateOfBirth": self._dob,
                "FirstName": self._firstName,
                "LastName": self._lastName,
                "LastFourDigitsSsn": self._ssn4
            }
            res = requests.post(url=self._BASE_URL + '/Booking',
                                data=str(PAYLOAD), headers=self._HEADERS)
            appointments = res.json()
            self._PP.pprint(appointments)
            return appointments
        except requests.exceptions.HTTPError as e:
            print('[Error] Check availability failed: ', e.response.text)
            return []

    def book(self, locationId: int, slot: dict, email: str) -> None:
        if not self._loggedIn:
            print("[Error] Haven't logged in yet")
            return

        try:
            CREDENTIAL = {'FirstName': self._firstName, 'LastName': self._lastName,
                          'DateOfBirth': self._dob, 'Last4Ssn': self._ssn4}
            # hold the slot
            PAYLOAD_HOLD = {**CREDENTIAL, "SlotId": slot['SlotId']}
            res = requests.post(url=self._BASE_URL + "/HoldSlot",
                                data=str(PAYLOAD_HOLD), headers=self._HEADERS)
            if res.json()['SlotHeldSuccessfully']:
                PAYLOAD_BOOK = {
                    **CREDENTIAL,
                    'Email': email,
                    'ServiceTypeId': self._apmtType.value,
                    'BookingDateTime': slot["StartDateTime"],
                    'BookingDuration': slot['Duration'],
                    'SpanishLanguage': 'N',
                    'SiteId': locationId,
                    'ResponseId': self._resID,
                    'CardNumber': '',
                    'CellPhone': '',
                    'HomePhone': '',
                }

                try:
                    res = requests.post(url=self._BASE_URL + "/RescheduleBooking",
                                        data=str(PAYLOAD_BOOK), headers=self._HEADERS)
                    self._PP.pprint(res.json())
                    return
                except requests.exceptions.HTTPError as e:
                    print('[Error] Book appointment failed: ', e.response.text)
                    return
            else:
                print('[Error] Book appointment failed')
                return
        except requests.exceptions.HTTPError as e:
            print('[Error] Book appointment failed: ', e.response.text)
            return

    def _checkAvailability(self, zipCode: str) -> list:
        try:
            DATA = {'TypeId': self._apmtType.value, 'ZipCode': zipCode,
                    'CityName': '', 'PreferredDay': '0'}
            res = requests.post(url=self._BASE_URL + '/AvailableLocation',
                                data=str(DATA), headers=self._HEADERS)
            return res.json()
        except requests.exceptions.HTTPError as e:
            print('[Error] Check availability failed: ', e.response.text)
            return []


if __name__ == '__main__':
    user = User("Li-Niang", "Gan", "07/23/1994", "1234", AppointmentType.RENEW_LICENSE)
