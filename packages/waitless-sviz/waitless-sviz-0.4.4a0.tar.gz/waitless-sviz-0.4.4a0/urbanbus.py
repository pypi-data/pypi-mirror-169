
def url(stopid): 
    url_welbits = f'https://api.interurbanos.welbits.com/v1/stop/{stopid}'    
    url_crtm    = f'https://www.crtm.es/widgets/api/GetStopsTimes.php?codStop=8_{stopid}&type=1&orderBy=2&stopTimesByIti=3'
    
    return url_crtm


#Call to API and get json data
def call_for_data(url):
    try:
        import urequests as requests
    except ImportError:       
        import requests
        
    r               = requests.get(url = url)   
    try:
        json_data   = r.json() #r.text.json()
        status_code     = r.status_code
        
    except ValueError:
        status_code = 500
        json_data = {}
        
    status_code = r.status_code
    #print('Testeo si ejecuta r.close')
    r.close()
    return json_data, status_code


def how_much_to(value):
    import utime as time
    
    h, m     = int(value[0]), int(value[1])
    now      = time.localtime()
    after    = list(now)

    if now[3] >= h:
        if now[4] >= m:
            after[2] = after[2] + 1
    after[3],after[4] = h, m
    
    return time.mktime(tuple(after)) - time.time()


def date_ticks_from_date_str(date_str):
    import utime as time
    
   #0    5    10   15   20   25#
   #:....:....:....:....:....: 
   # 2022-09-19T17:29:16+02:00
   # YYYY-MM-DDThh:mm:ss+xx:xx
   
    now = time.localtime()
    
    Y         = int(date_str[0:4])
    M         = int(date_str[5:7])
    D         = int(date_str[8:10])
    h         = int(date_str[11:13])
    m         = int(date_str[14:16])
    s         = int(date_str[17:19])
    w         = now[6]
    y         = now[7]
    
    date_time = (Y,M,D,h,m,s,w,y)   
    return time.mktime((Y,M,D,h,m,s,w,y))
    

#Filter for the next arrival for each line
def sel_next_bus_each_line(api_data): #sel_next_bus_each_line_crtm
    
    actual_date       = api_data['stopTimes']['actualDate']
    ticks_actual_date = date_ticks_from_date_str(actual_date)
    try:
        data              = api_data['stopTimes']['times']['Time']
    except:
        data = []
    print('hay ' + str(len(data))+ ' regristros')
    
    next_bus = [] ; control = []
    
    for i in data:
        if i['line']['shortDescription'] not in control:
            wait_time = int ((date_ticks_from_date_str(i['time']) - ticks_actual_date) / 60 )
            if wait_time < 60: ### relacionar con delay en manage_time_out_of_service
                wait_time = str(wait_time) + ' min'
            else:
                wait_time = i['time'][11:16]
            
            next_bus.append([i['line']['shortDescription'],wait_time])
            control.append(i['line']['shortDescription'])
            
            #manage_time_out_of_service(next_bus)
                
    return next_bus  # output: list


def sel_next_bus_each_line_welbits(api_data):
    import utime as time
    
    next_bus = [] ; control = []
    
    for i in api_data['lines']:
        if i['lineNumber'] not in control:
            next_bus.append([i['lineNumber'],i['waitTime']])
            control.append(i['lineNumber'])
            manage_time_out_of_service(next_bus)
    return next_bus  # output: list


def manage_time_out_of_service(next_bus):

    delay          = 0
      
    if all(list(map(lambda a: ':' in a[1], next_bus))):
        next_bus.sort(key = lambda x: int(x[1].replace(':','')))
        first_bus_time    = next_bus[0][1].split(':')
        delay             = how_much_to(first_bus_time) - 30 * 60
        out_of_service    = True
        
    return delay


def maintenance_window(out_of_service_time):
    import utime as time
    import machine,os, random
    import upip as pip
    from lcd_i2c_printer import waiting_message, print_on_lcd
    
    if out_of_service_time == 0:
        pass
    else:
        courtesy_time = 5 * 60
        print('Going to sleep')
        #clock = bytearray([0x00, 0x0E, 0x15, 0x17, 0x11, 0x0E, 0x00, 0x00])
        # custom_icon(0, clock)
        print_on_lcd('Servicio diario', 'finalizado', False)
        time.sleep(random.randint(courtesy_time,out_of_service_time))
        mtime = time.localtime(os.stat('configure.py')[7])
        print(mtime)
        if mtime[:3] != time.localtime()[:3]:
            waiting_message('Actualizando    dispositivo')
            pip.install('waitless-sviz','/')
            waiting_message('Reiniciando     dispositivo')
            time.sleep(2)
            machine.reset()

#Manage the behaivor according to the API response
def handle_api_responses(schedule, HTTPResponseCode): # Llamar con callForData(url(stopid))
    import utime as time
    from lcd_i2c_printer import show_wait_time, waiting_message, moving_message
    
    global count_500
    break_while = False
    
    if HTTPResponseCode == 200:
        count_500 = 0
        delay = 60

        arrivals            = sel_next_bus_each_line(schedule)
        delay               = show_wait_time(arrivals, delay)
        out_of_service_time = manage_time_out_of_service(arrivals)
        
        print (schedule)
        print(arrivals)
        
        maintenance_window(out_of_service_time)
        
    elif HTTPResponseCode == 404:
        print("Connection Failed. Code: " + str(HTTPResponseCode))
        moving_message('Reinicie el dispositivo y configure parada',
                       1,
                       0.2,
                       'Parada erronea!',
                       10
                      )
        break_while = True
        
    elif HTTPResponseCode == 500:
        
        print("Connection Failed. Code: " + str(HTTPResponseCode))
        
        if count_500 < 10:               
            delay = 10
                
        else:
        
            waiting_message('Server Error:   Espere')
            delay = 300
        
        count_500 += 1
    
    else:
        waiting_message('Error. Reinicie')
        #break_while = True
           
    time.sleep(delay)
    return break_while

#Launch the bus service
def bus_service():
    import machine
    #import utime as time
    from configure import read_config_file
    from lcd_i2c_printer import background_light_off, background_light_on
 
    global count_500

    count_500             = 0
    activity_control_time = 15
    sensor_pir            = machine.Pin(28, machine.Pin.IN)
    led                   = machine.Pin('LED', machine.Pin.OUT)
    stopid                = read_config_file()['settings']['stopid']
    
    
    def pir_handler(pin):   
        print('Detectado movimiento')
        nonlocal activity_control_time
        activity_control_time = 15

    sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
    
    
    while True:
        if activity_control_time == 0:
            background_light_off()
        else:    
            background_light_on()
            schedule, HTTPResponseCode = call_for_data(url(stopid))
            break_while                = handle_api_responses(schedule, HTTPResponseCode)

            activity_control_time      -= 1      
        
        if break_while == True:
            break
            

