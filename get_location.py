import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
      
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)  
  
# Driver function 
if __name__=="__main__": 
      
    # Coorinates tuple.Can contain more than one pair. 
    coordinates =(26.8467088, 80.9461592) 
      
    reverseGeocode(coordinates)
