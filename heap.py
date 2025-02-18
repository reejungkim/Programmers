def solution(scoville, K):
    
    from heapq import heappush, heappop
    heap = []  #    힙생성
    heappush( heap, 4)  #힙원소 생성
    heappush( heap, 1)
    heappush( heap, 7)
    heappush( heap, 11)
    print(heap)   #output --> [1,4,7]
    
    heappop(heap)  #루트의 가장 작은 원소 삭제
    print(heap)
    heappop(heap)  #루트의 가장 작은 원소 삭제
    print(heap)
    
    #최소값 삭제하지 않고 접근하기
    print(heap[0])  #<-루트에서 값을 가져옴으로 index가 0인것만 사용가능. 리스트를 프린트 했을때에도 정렬이 되어있지 않고. 첫번째 인덱스에만 가장 작은 수가 들어있게 됨. 
    
    heappush(heap,1)
    print(heap)
    
    #리스트에서 힙으로 변환   *주의: 리스트에서 힙으로 변환시 인덱스가 힙기준으로 바뀜.
    from heapq import heapify
    heap = [4,1,7,3,8,5]
    heapify(heap)
    print(heap)
    
    nums = [4,1,7,3,8,5]
    heap = nums[:]
    heapify(heap)
    print("nums: ", nums)
    print("heap: ", heap)
    
    
    
    #응용: 쵀대힙
    nums =[4,1,7,3,8,5]
    heap =[]
    for num in nums:
        heappush(heap, (-num, num))  #<- 튜플을 넣어줌   
    
    from heapq import heappush, heappop 
    while heap:
        print(heappop(heap)) #<- 마이너스 맥스값, 맥스값이 출력
        print(heappop(heap)[1]) #<- 맥스값 출력되도록함.
        
        
        
    #응용: n번째 최소값/ 최대값 
    def nth_smallest(nums, n):
        
        heap=[]
        for num in nums:
            heappush(heap, num)
            
        nth_min = None
        for _ in range(n):
            nth_min = heappop(heap)
        
        return nth_min
    
    from heapq import nsmallest, nlargest
    print(nsmallest(3, [4,1,7,3,8,5])[-1])
    print(nlargest(1, [4,1,7,3,8,5])[-1])
    
    
    