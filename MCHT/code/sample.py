import pywifi
from time import sleep
import sys
from os import listdir

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

#raw data
def scan(delay=2):
    """
    scan(delay=1):
        delay is the scan time interval.
        retrun a list of scan_result item.(with .bssid and .signal).
    """
    global iface
    iface.scan()
    sleep(delay)
    return iface.scan_results()

#read bssid.csv
def bssid_list():
    """
    def bssid_list():
        return bssid_list
    """
    with open('bssid.csv', 'r') as f:
        return f.readline()[:-1].split(',')

#scan wifi which in the bssid.csv
def scan_inlist(delay=2):
    """
    scan_inlist(delay=1):
        delay is the scan time interval.
        retrun a list of signals in the order as bssid.csv.
        #signal is dB
    """
    result = scan(delay=delay)
    result = {i.bssid: i.signal for i in result}
    return [result[i] if i in result.keys() else 0 for i in bssid_list()]


def setup():
    """
    setup():
        save the list of bssids in bssid.csv.
        #remove repeated bssid 
    """
    """
    with open('bssid.csv', 'w') as f:
        data = [i.bssid for i in scan()]
        f.write(",".join(data))
    """
    #insure sthe file exist.
    with open("bssid.csv", 'a') as f:
        pass

    while True:
        for x in range(10):
            sleep(1)
            with open("bssid.csv", 'r') as f:
                data_pre = f.read().split(',')

            with open("bssid.csv", 'w+') as f:
                data = [i.bssid for i in scan()]
                data = list(set(data+data_pre))
                f.write(",".join(data))
                print(x)

        ans = input("Continue?(y/[n]): ")
        if ans == 'n':
            break


def sample(filename, point):
    """
    sample(filename, point):
        filename is the file saved data.
        point is the name of this point.
        save data in 'a+' mode in (filename).
    """
    with open(filename, 'a+') as f:
        f.write('\n')
        f.write(str(point) + ',')
        f.write(",".join([str(i) for i in scan_inlist()]))


def list_all(mode='a'):
    """
    list_all(mode='a'):
        mode is the print mode.
        'a' >> print all wifi.
        'l' >> print those in bssid.csv. 
    """
    if mode == 'a':
        result = scan()
        for i in range(len(result)):
            # bssid is name,signal is signal magnitude
            print("{0:3}. {1:20}: {2:3}".format(
                i, result[i].bssid, result[i].signal))
    elif mode == 'l':
        bssids = bssid_list()
        result = scan_inlist()
        for i in range(len(bssids)):
            print("{0:3}. {1:20}: {2:3}".format(i, bssids[i], result[i]))


def select_file():
    """
    select_file():
        Go through root dir. and list all csv file.
        Then print a list for choice.
        return the filename choiced.
        #no such file >> repeat
    """
    file_list = listdir()
    check_list = ['.csv' in i for i in file_list]
    i = 1
    select_dict = {}
    for x in range(len(file_list)):
        if check_list[x]:
            if 'bssid.csv' == file_list[x]:
                continue

            print('{0:2}. {1}'.format(i, file_list[x]))
            select_dict[str(i)] = file_list[x]
            i += 1
    while True:
        try:
            return select_dict[input("select the filename: ")]
        except:
            pass


def select_mode():
    mode_dict = {'0': "quit", '1': "setup", '2': "sample", '3': "list all"}
    for i in range(4):
        print("{0:2}: {1:10}".format(i, mode_dict[str(i)]))
    while True:
        num = input("select mode: ")
        try:
            return mode_dict[num]
        except:
            pass


def act_mode(mode):
    if mode == 'setup':
        setup()

    elif mode == 'sample':
        filename = select_file()
        point = input('Which point: ')
        while True:
            try:
                time = int(input('How many points: '))
                break
            except:
                pass
        for t in range(time):
            sample(filename, point)
            print("sample_{0:03} is completed.".format(t+1))

    elif mode == 'list all':
        list_all(input("input mode(all:'a'/inlist:'l'): "))
    else:
        print("The mode is wrong.")


def main():
    act_mode(select_mode())


if __name__ == "__main__":
    main()
