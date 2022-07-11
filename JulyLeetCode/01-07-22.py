
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        
        
        ## sort the array based on unit 
        # the more unit the less bozexs:
        
        
        boxTypes.sort(key = lambda x:-x[1])
        #3 1,3, 22, 3,1 
        # (5, 10), (3,9), (4,7), (2,5)
        
        max_unit =0
        
        for number_of_boxes, numberof_unit_per_boxes in boxTypes:
            
            if truckSize <0:
                break
            else:

                max_unit += min(truckSize, number_of_boxes)*numberof_unit_per_boxes
                truckSize -=number_of_boxes
                
            
            
        return max_unit
    
