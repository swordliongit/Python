


import requests
import json
import requests
from datetime import datetime

PAXIMUM_ID = 100826


def H2S_Login():
    user = "ARTIN_TP"
    passw = "RQUJFZAH"
    
    response = requests.get(
                url=f"https://admin.hotel2sejour.com/api/system/login?user={user}&pass={passw}"
            )
    cookie = json.loads(response.content)
    return cookie


def H2S_Push(cookie, resdata):
    
    url = "https://admin.hotel2sejour.com/api/pax/pushreservationsforthirdparty"
    
    headers = {
        "cookie": cookie,
        "content-type": "application/json"
    }
    
    # Define reservation data with all the fields (sample data)
    reservation_data = resdata
        

    # Convert the reservation data to JSON
    payload = json.dumps(reservation_data)

    # Make the POST request to push reservations
    response = requests.post(url, headers=headers, data=payload)
    print(response)
    print(response.text)

    # Check the response
    if response.status_code == 200:
        print('Reservation data successfully pushed.')
    else:
        print(f'Error: {response.status_code}')
 
 
def create_reservation_item(
    opcode, opname, resno, resorder, restype, resconf, hotel, hotelname,
    hotelpaximumid, cindate, coutdate, day, roomcode, roomname, roomcount,
    accomcode, accomname, boardcode, boardname, adl, extbed, chd, inf, totalpax, resnote,
    resamount, resamountcurr, sellingdate, allotmenttype, resuser, uid, dbname,
    chgdate, username
):
    return {
        'OperatorCode': opcode,
        'OperatorName': opname,
        'ResNo': resno,
        'ResOrder': resorder,
        'ResType': restype,
        'ResConf': resconf,
        'Hotel': hotel,
        'HotelName': hotelname,
        'HotelPaximumID': hotelpaximumid,
        'CinDate': cindate,
        'CoutDate': coutdate,
        'Day': day,
        'RoomCode': roomcode,
        'RoomName': roomname,
        'RoomCount': roomcount,
        'AccomCode': accomcode,
        'AccomName': accomname,
        'BoardCode': boardcode,
        'BoardName': boardname,
        'Adl': adl,
        'ExtBed': extbed,
        'Chd': chd,
        'Inf': inf,
        'TotalPax': totalpax,
        'ResNote': resnote,
        'ResAmount': resamount,
        'ResAmountCurr': resamountcurr,
        'SellingDate': sellingdate,
        'AllotmentType': allotmenttype,
        'ResUser': resuser,
        'UniqueID': uid,
        'DatabaseName': dbname,
        'ChgDate': chgdate,
        'UserName': username
    }


def create_customer_item(
    opcode, resno, resorder, custorder, namesurname, age, birthdate,
    nationalitycode, nationalityname, passportnum, arrival, arrivaltime,
    departure, departuretime, dbname, chgdate, uid, username
):
    return {
        'OperatorCode': opcode,
        'ResNo': resno,
        'ResOrder': resorder,
        'CustOrder': custorder,
        'NameSurname': namesurname,
        'Age': age,
        'BirthDate': birthdate,
        'NationalityCode': nationalitycode,
        'NationalityName': nationalityname,
        'PassportNr': passportnum,
        'Arrival': arrival,
        'ArrivalTime': arrivaltime,
        'Departure': departure,
        'DepartureTime': departuretime,
        'DatabaseName': dbname,
        'ChgDate': chgdate,
        'UniqueID': uid,
        'UserName': username
    }


def create_extra_item(
    extsrvprice, pax, extsrvcode, extsrvname, extsrvpricecurr,
    opcode, resno, resorder, dbname, chgdate, uid, username
):
    return {
        'ExtSrvPrice': extsrvprice,
        'Pax': pax,
        'ExtraServiceCode': extsrvcode,
        'ExtraServiceName': extsrvname,
        'ExtSrvPriceCurr': extsrvpricecurr,
        'OperatorCode': opcode,
        'ResNo': resno,
        'ResOrder': resorder,
        'DatabaseName': dbname,
        'ChgDate': chgdate,
        'UniqueID': uid,
        'UserName': username
    }


def create_email_item(
    username, dbname, uid, emailtype, emailaddr
):
    return {
        'UserName': username,
        'DatabaseName': dbname,
        'UniqueID': uid,
        'EMailType': emailtype,
        'EMailAddr': emailaddr
    }
    
    
def create_delete_item(
    username, tablename, uid, deletedate, dbname
):
    return {
        'UserName': username,
        'TableName': tablename,
        'UniqueID': uid,
        'DeleteDate': deletedate,
        'DatabaseName': dbname
    }


def create_hotel_item(
    uid, hotel, hotelname, region, pax, dbname, username
):
    return {
        'UniqueID': uid,
        'Hotel': hotel,
        'HotelName': hotelname,
        'Region': region,
        'HotelPaximumID': pax,
        'DatabaseName': dbname,
        'UserName': username
    }


def H2S_init():

    reservation_list = []
    customer_list = []
    extra_list = []
    email_list = []
    delete_list = []
    hotel_list = []

    # Construct list items
    reservation_item = create_reservation_item(
        opcode = "", # Sisteminizdeki rezervasyonun operator kodudur
        opname = "", # Sisteminizdeki rezervasyonun operator adıdır
        resno = "123abc", # Sisteminizdeki rezervasyonun voucher numarasıdır
        resorder = 1, # Sisteminizdeki rezervasyon ResNo ‘sunun sırasıdır
        restype = "Y", # Rezervasyon Tipi (Y : New , D : Modify , I : Cancel)
        resconf = "W", # Rezervasyon konfirme durumu (Y : Yes , N : No , W : Waiting)
        hotel = "H2S", # Sisteminizdeki otel kodu
        hotelname = "H2S Test Hotel", # Sisteminizdeki otel adı
        hotelpaximumid = PAXIMUM_ID, # Hotel2Sejour tarafından verilecek olan otel Id
        cindate = datetime(2023, 9, 15).strftime("%m.%d.%Y"), # Otel giriş tarihi
        coutdate = datetime(2023, 9, 16).strftime("%m.%d.%Y"), # Otel çıkış tarihi
        day = 2, # Konaklama gün sayısı,
        roomcode = "SNG", # Sisteminizdeki oda kodu
        roomname = "SINGLE", # Oda adı
        roomcount = 1, # Oda sayısı	
        accomcode = "STD", # Sisteminizdeki oda tipi
        accomname = "STANDART ODA", # Sisteminizdeki oda adı	
        boardcode = "ALL", # Sistemdeki pansiyon kodu
        boardname = "ALL INCLUSIVE (AI)", # Sistemdeki pansiyon adı	
        adl = 2, # Yetişkin sayısı
        extbed = 0, # Extra bed sayısı	
        chd = 0, # Çocuk sayısı	
        inf = 0, # Bebek sayısı	
        totalpax = 2, # Rezervasyondaki toplam kişi sayısı	
        resnote = "TEST NOTE", # Otelin Göreceği rezervasyon notu	
        resamount = 100.0, # Rezervasyon konaklama tutarı		
        resamountcurr = "TR", # Rezervasyon konaklama tutarı döviz cinsi	
        sellingdate = datetime(2023, 9, 15).strftime("%m.%d.%Y"), #Rezervasyon Satış tarihi	
        allotmenttype = "G", # Rezervasyon Kontenjan türü (N : Normal , G : Guarantee , S : OnRequest)	
        resuser = "Batuhan", # Rezervasyonu yapan kullanıcı kodu	
        uid = 1001, # Rezervasyon kartının sisteminizdeki unique numarası (ID)	
        dbname = "ARTINSYSTEMS", # Rezervasyona konfirme verileceği zaman kaydın hangi DB de olduğunu anlamak için gerekli alandır	
        chgdate = datetime(2023, 9, 15).strftime("%m.%d.%Y"), # Kaydın sisteminizdeki en son değişiklik tarihi	
        username = "ARTINSYSTEMS" # Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı
    )
    customer_item = create_customer_item(
        opcode = "TUROP", # Sisteminizdeki rezervasyonun operator kodudur	
        resno = "123abc", # Sisteminizdeki rezervasyonun voucher numarasıdır	
        resorder = 1, # Müşterinin bağlı olduğu rezervasyon sıra numarası	
        custorder = 1, # Müşteri sıra numarası	
        namesurname = "Batuhan Kalkan", # Adı soyadı	
        age = 30, # Yaşı
        birthdate = datetime(1990, 9, 16).strftime("%m.%d.%Y"), # Doğum tarihi	
        nationalitycode = "TR", # Milliyet kodu	
        nationalityname = "TURK", # milliyet adı
        passportnum = "123", # Pasaport Numarası ya da TC kimlik no gönderilebilir	
        arrival = "CAI040", # Müşterinin geliş yeri Örn : TK123 numarası uçuş	
        arrivaltime = datetime(2023, 9, 16).strftime("%m.%d.%Y"), # Müşteri geliş tarih ve saati	
        departure = "CAI041", # Müşteri dönüş yeri Örn : TK 456	
        departuretime = datetime(2023, 9, 25).strftime("%m.%d.%Y"), # Müşteri dönüş tarihi ve numarası	
        dbname = "ARTINSYSTEMS", # Hotel2Sejour tarafından verilir	
        chgdate = datetime(2023, 9, 25).strftime("%m.%d.%Y"), # Kaydın sisteminizdeki en son değişiklik tarihi	
        uid = 2101, # Müşterinin sisteminizdeki unique numarası, ID si	
        username = "ARTINSYSTEMS" # Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı
    )
    
    extra_item = create_extra_item(
        extsrvprice = 120.0, # Extra servis ücreti	
        pax = 2, # Extra servisi alan kişi sayısı	
        extsrvcode = "BB", # Extra servisin kodu	
        extsrvname = "Test", # Extra servisin adı	
        extsrvpricecurr = "TR", # Extra Servis döviz cinsi	
        opcode = "TUROP", # Sisteminizdeki rezervasyonun operator kodudur	
        resno = "123abc", # Sisteminizdeki rezervasyonun voucher numarasıdır	
        resorder = 1, # Sisteminizdeki rezervasyon ResNo ‘sunun sırasıdır	
        dbname = "ARTINSYSTEMS", # Hotel2Sejour tarafından verilir	
        chgdate = datetime(2023, 9, 16).strftime("%m.%d.%Y"), # Kaydın sisteminizdeki en son değişiklik tarihi	
        uid = 3201, # Kaydın sisteminizdeki unique değeri	
        username = "ARTIN_Hotel" # Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı	
    )
    
    email_item = create_email_item(
        username = "ARTINSYSTEMS", # Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı
        dbname = 	"ARTINSYSTEMS", # Hotel2Sejour tarafından verilir	
        uid = 4301, # Kaydın sisteminizdeki unique değeri
        emailtype = 3, # (Konfirme için 3 , NotKonfirme için 4) gönderilmesi gerekir	
        emailaddr = "batuhan.kalkan@paximum.com, muratkelekci@paximum.com" # E-mail adresidir. Birden fazla mail adresi girilmesi için aralarına virgül (,) konmalıdır	
    )
    
    delete_item = create_delete_item(
        username = "ARTINSYSTEMS", #Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı	
        tablename = "RezOtel", # Hotel2Sejour tarafından verilir, Örnek (RezOtel,Musteri,RezExt,SejDeleteLog)
        uid = 1003, # Kendi sisteminizdeki silinen kaydın unique değerini verir
        deletedate = datetime(2023, 9, 17).strftime("%m.%d.%Y"), # Sisteminizdeki kaydın silinme tarihini verir
        dbname = "ARTINSYSTEMS" # Hotel2Sejour tarafından verilir	
    )
    
    hotel_item = create_hotel_item(
        hotel = "H2S", # Sisteminizdeki otel kodu	
        hotelname = "H2S Test Hotel", # Sisteminizdeki otel adı	
        region = "AYT", # Sisteminizdeki otelin bölgesi	
        pax = PAXIMUM_ID, # Hotel2Sejour tarafından verilecek olan otel Id		
        dbname = "ARTINSYSTEMS", # Hotel2Sejour tarafından verilir	
        uid = 1,  # Kendi sisteminizdeki silinen kaydın unique değerini verir	
        username = "agave_stage_service_user" # Hotel2Sejour sistemi tarafından verilen servis kullanıcı adı	
    )
        
    # Add items to their lists
    reservation_list.append(reservation_item)
    customer_list.append(customer_item)
    extra_list.append(extra_item)
    email_list.append(email_item)
    delete_list.append(delete_item)
    hotel_list.append(hotel_item)

    # Construct the POST json data
    resdata = {
        'ReservationList': reservation_list,
        'CustomerList': customer_list,
        'ExtraList': extra_list,
        'EmailParamList': email_list,
        'DeleteList': delete_list,
        'HotelList': hotel_list
    }
    
    cookie = H2S_Login()
    
    # H2S_Push(cookie)
    H2S_Push(cookie, resdata)
    

H2S_init()