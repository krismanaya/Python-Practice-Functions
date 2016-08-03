class instruments(object): 
    def __init__(self,name,year):
        self.name = name
        self.year = year 

guitar = instruments('guitar',None)
year = instruments(None,'1973')
print (guitar.name,year.year)