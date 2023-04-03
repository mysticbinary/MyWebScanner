import requests


def XSSengine(domain, method, parameters):
    print("start xss.")
    parameters = parameters.split(",")
    counter = 0
    vuln = "XSS"
    payload = [
               "<h4>444<h4>",
               "\"><script>alert(2)</script>"
               ]

    for i in payload:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("current scanner domain :", domain)
        print("current scanner payload :", i)
        data = {}
        print("----------------------------------------------------------------------")
        for j in range(len(parameters)):
            data[parameters[j]] = i
            print("data : ", data)
            if method == "GET":
                r = requests.get(domain, data)
                print("r.status_code : ", r.status_code)
                if str(i) in r.text:
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter += 1
                    # reporter.ReportIt(domain, method, parameters[j], payload, vuln, counter)
                    print("domain is:", domain)
                    print("method is:", method)
                    print("parameters[j] is:", parameters[j])
                    print("payload is:", payload)
                    print("vuln is:", vuln)
                    print("counter is:", counter)
                    print("######################")
            elif method == "POST":
                r = requests.post(domain, data)
                print("r.status_code is ", r.status_code)
                if str(i) in r.text:
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter += 1
                    # reporter.ReportIt(domain, method, parameters[j], payload, vuln, counter)
                    print("domain is:", domain)
                    print("method is:", method)
                    print("parameters[j] is:", parameters[j])
                    print("payload is:", payload)
                    print("vuln is:", vuln)
                    print("counter is:", counter)
                    print("######################")
