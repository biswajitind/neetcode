class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        # pair the position and speed together for sorting them together based on 
        # position.
        for i in range(len(position)):
            time_to_dest = (target - position[i]) / speed[i]
            cars.append([position[i], speed[i], time_to_dest])

        # sort
        cars.sort(key=lambda x: x[0])
        
        fleetCount = 0
        while cars:
            fleetCount += 1
            fleetTime = cars.pop()[2]
            while cars and cars[-1][2] <= fleetTime:
                cars.pop()
    
        return(fleetCount)