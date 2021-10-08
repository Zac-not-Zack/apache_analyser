test_line="83.149.9.216 - - [17/May/2015:10:05:03 +0000] 'GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1' 200 203023 'http://semicomplete.com/presentations/logstash-monitorama-2013/' 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'"

#splitter : seperate the texts in a line to retrieve the time, ip address, request, response code, size, href, os
def splitter(line):
    line=line.split(' ')
    list=dict(
    time=line[3],
    remote_ip=line[0],
    request=line[6],
    response=line[8],
    size=line[9],
    href=line[10],
    os=' '.join(line[12:]),
    )
    return list

def cleaner(list):
    list[0]=list[1:]
    list[2]=list[3].split('/')
    #list[6]=

print(splitter(test_line))