import subprocess
twitter_ip_route = ['192.168.0.1', '174.109.176.1', '174.111.105.48', '24.25.41.106', '24.93.64.184', '66.109.6.80', '66.109.5.117', '199.59.151.92', '104.244.42.1'] 
# get 3 sets of ip addresses for the three hosts. twitter.com, cam.ac.uk, and seattleu.edu
cam_ac_uk_ip_route = ['192.168.0.1', '174.109.176.1', '174.111.105.50','24.25.41.108', '24.93.64.186', '66.109.6.34','66.109.5.125' ,'4.68.37.73','4.69.143.198','212.187.216.238','146.97.35.193','146.97.33.62','146.97.33.29','146.97.35.246','146.97.41.38','193.60.88.6','193.60.88.6','128.232.128.6','128.232.128.10','128.232.132.8']
seattle_u_ip_route = ['192.168.0.1','174.109.176.1','174.111.105.48','24.25.41.106','24.93.64.184','66.109.10.176','66.109.6.151','66.109.6.36','107.14.19.49','66.109.5.228','66.109.5.247','99.82.176.54']

def runPingExperiment1(ips_to_ping, output_file):
    new_file = open(output_file, 'a+')
    for ip in ips_to_ping:
        process = subprocess.Popen(['ping', '-n', '60', ip], stdout = subprocess.PIPE,universal_newlines=True)
        while True:
            output = process.stdout.readline()
            # Do something else
            return_code = process.wait()
            if return_code is not None:
                print('RETURN CODE', return_code)
                 # Process has finished, read rest of the output 
                out = ""
                for output in process.stdout.readlines():
                    out += output
                break
        if return_code == 0:
            parsed = parsePing(out)
            parsed_string = parsed[0] + ": average is " + parsed[1]+ ", loss is + " + parsed[2] + "\n"
            new_file.write(parsed_string)
        else:
            new_file.write("Error at " + ip + "\n")
        # add loss to results. 

    return True


def parsePing(out):
    # parse for loss. 
    ip = out.split('for')[1]
    ip = ip[1:]
    ip = ip.split(':')[0]
    average = out.split('Average')
    average = average[1].split(' ')
    average = average[2].split('ms')
    average = average[0]
    loss = out.split(')')
    loss = loss[0].split(' ')
    loss = loss[len(loss) - 2]
    return [ip, average, loss]

runPingExperiment1(twitter_ip_route, 'early_morning_twitter.txt')
runPingExperiment1(cam_ac_uk_ip_route, 'early_morning_cam.txt')
runPingExperiment1(seattle_u_ip_route, 'early_morning_seattle.txt')