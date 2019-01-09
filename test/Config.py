
class Config:

    def __init__( self ):
        self.url='http://192.168.11.186/Migracion-Web/admin/login'
        self.pathChromeDriver='/usr/local/bin/chromedriver'
        
    def getUrl(self):
		#print("Iniciando en getUrl.....");
        return self.url;
        
        
    def getPathChromeDriver(self):
		#print("Iniciando en getPathChromeDriver.....");
        return self.pathChromeDriver;
                
        
    def hola( self ):
		print("hola.....");
