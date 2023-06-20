from setup import init
from validation import validate
from data import extract
from web import scrapping
from table import builder

def main():
    init.updateRequirements()
    validate.checkUrl()
    #web = scrapping.getWeb()
    data = extract.getData()
    builder.buildExcelTable(data)
    return

if __name__ == "__main__":
    main()