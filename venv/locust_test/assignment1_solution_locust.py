# Complete booking flow
####Launch new tours demo page - Create on_start task with get request
####Login with registered credential - task name login_demotour with post request
    ##verify through resp.text that user is on find flight page with post request
####Click continue with default value - task name find_flight with post request
   ##verify through resp.text that user is on select flight page with post request
####Click continue with default value - task name select_flight with post request
   ##verify through resp.text that user is on book flight page with post request
####Fill form with data & click secure purchase- task name book_flight with post request
   ##verify through resp.text that user gets booking confirmation with post request
#Run test with --logfile option to generate log file

from locust import HttpLocust,TaskSet,task

UserName=[
    ("qamile1@gmail.com","qamile"),
    ("qamile2@gmail.com", "qamile"),
    ("qamile3@gmail.com", "qamile"),
    ("qamile4@gmail.com", "qamile"),
    ("qamile5@gmail.com", "qamile")
 ]


formdata1 = {
    "tripType": "roundtrip",
    "passCount": "1",
    "fromPort": "Acapulco",
    "fromMonth": "10",
    "fromDay": "24",
    "toPort": "Acapulco",
    "toMonth": "10",
    "toDay": "24",
    "servClass": "Coach",
    "airline": "No" "Preference",
    "findFlights.x": "43",
    "findFlights.y": "11"
}
formdata2 = {
    "fromPort": "Acapulco",
    "toPort": "Acapulco",
    "passCount": "1",
    "toDay": "24",
    "toMonth": "10",
    "fromDay": "24",
    "fromMonth": "10",
    "servClass": "Coach",
    "outFlight": "Blue Skies Airlines$360$270$5:03",
    "inFlight": "Blue Skies Airlines$630$27012:23",
    "reserveFlights.x": "57",
    "reserveFlights.y": "7"
}

formdata3 = {
    "outFlightName": "Blue Skies Airlines",
    "outFlightNumber": "360",
    "outFlightPrice": "270",
    "outFlightTime": "5:03",
    "inFlightName": "Blue Skies Airlines",
    "inFlightNumber": "630",
    "inFlightPrice": "270",
    "inFlightTime": "12:23",
    "fromPort": "Acapulco",
    "toPort": "Acapulco",
    "passCount": "1",
    "toDay": "24",
    "toMonth": "10",
    "fromDay": "24",
    "fromMonth": "10",
    "servClass": "Coach",
    "subtotal": "540",
    "taxes": "44",
    "passFirst0": "qa",
    "passLast0": "mile",
    "pass.0.meal": "",
    "creditCard": "AX",
    "creditnumber": "12234567",
    "cc_exp_dt_mn": "None",
    "cc_exp_dt_yr": "None",
    "cc_frst_name": "qa",
    "cc_mid_name": "",
    "cc_last_name": "mile",
    "billAddress1": "test1,test2",
    "billAddress2": "",
    "billCity": "sss",
    "billState": "Hawaii",
    "billZip": "0000000",
    "billCountry": "215",
    "delAddress1": "1325 Borregas Ave",
    "delAddress2": "",
    "delCity": "Sunnyvale",
    "delState": "CA",
    "delZip": "94089",
    "delCountry": "215",
    "buyFlights.x": "81",
    "buyFlights.y": "10",
}

class UserBehaviour(TaskSet):

    def on_start(self):
        self.userName="Not_exist"
        self.password="Not_exist"
        if len(UserName) >0:
            self.userName, self.password = UserName.pop()
            
        res1=self.client.post("/login.php", data={"action": "process", "userName": self.userName, "password": self.password
            , "login.x": "16", "login.y": "9"})
        print(res1.text)

    @task(4)
    def find_flight(self):
        res2=self.client.post("/mercuryreservation2.php",data=formdata1)
        print(res2.text)

    @task(2)
    def select_flight(self):
        res3=self.client.post("/mercurypurchase.php", data=formdata2)
        print(res3.text)

    @task(1)
    def book_flight(self):
        res4=self.client.post("/mercurypurchase2.php", data=formdata3)
        print(res4.text)


class User(HttpLocust):
    task_set=UserBehaviour
    min_wait=5000
    max_wait = 10000
    host="http://newtours.demoaut.com"
