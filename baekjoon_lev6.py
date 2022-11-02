##4673. 셀프넘버
# 시간 초과
nums=[]
for i in range (1,10001):
    nums.append(i) # nums에 10000까지 append

for i in range (1,10001): # 
    a=i
    for j in range(len(str(i))):
        a+=int(str(i)[j]) # 생성자로 d(n) 생성

    for j in range(len(nums)):
        try:    
            if a==nums[j]:
                nums.remove(a) # remove(d(n))
        except Exception:
            continue

for i in range(len(nums)):
    print(nums[i])

# 