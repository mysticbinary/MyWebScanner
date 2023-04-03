from scanner import xss_scanner

# Analog data cleaning
def formatData():
    print("start formatting data.")
    domain = "http://php.testsparker.com/artist.php"
    method = "GET"
    parameters = "name,id"
    xss_scanner.XSSengine(domain, method, parameters)


if __name__ == '__main__':
    formatData()
